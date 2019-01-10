class MultiMap:
    def __init__(self):
        self.dct = {}  
        
    def get(self, k):
        if k in self.dct:
            return self.dct[k]
        else:
            return set()
        
    def __getitem__(self, k):
        return self.get(k)
    def add(self, k, v):
        if k not in self.dct:
            s = set() 
            self.dct[k] = s
            set.add(s,v)
            
        else:
            s=self.dct[k]
            set.add(s,v)
            
        
    def remove(self, k, v):
        if k in self.dct:
            s = self.dct[k] 
            set.remove(s,v)
            if  not bool(s):
                del self.dct[k]

class coreRBAC:
    def __init__(self):
        self.OBJS = set()  
        self.OPS = set()   # an operation-object pair is called a permission
        self.USERS = set()
        self.ROLES = set()
        self.PR = set()    # PR subset (OPS * OBJS) * ROLES, for PA in std
        self.UR = set()    # UR subset USERS * ROLES,        for UA in std
        self.SESSIONS = set()
        self.SU = set()    # SU subset SESSIONS * USERS
        self.SR = set()    # SR subset SESSIONS * ROLES
        self.SsdNAMES = set()
        self.SsdNR = set()    # SsdNR subset SsdNAMES * ROLES
        self.SsdNC = set()    # SsdNC subset SsdNAMES * int
        # forall n in SsdNAMES:
        # 1<=self.SsdRoleSetCardinality(n)<=len(self.SsdRoleSetRoles(n))-1
        self.DsdNAMES = set()
        self.DsdNR = set()    # DsdNR subset DsdNAMES * ROLES
        self.DsdNC = set()    # DsdNC subset DsdNAMES * int 

# administrative commands

    def AddUser(self, user):
        assert user not in self.USERS
        self.USERS.add(user)

    def DeleteUser(self, user):
        assert user in self.USERS
        self.UR -= set((user,r) for r in self.ROLES)    # maintain UR
        for s in set(s for s in self.SESSIONS if (s,user) in self.SU):
            self.DeleteSession(user,s)                     # maintain sessions
        self.USERS.remove(user)                 # delete user last

    def AddRole(self, role):
        assert role not in self.ROLES
        self.ROLES.add(role)

    def DeleteRole(self, role):
        assert role in self.ROLES
        self.ROLES.remove(role)
        self.PR -= set(((op,obj),role) for op in self.OPS for obj in self.OBJS)
        self.UR -= set((u,role) for u in self.USERS)    # maintain PR and UR
        for (s,u) in set((s,u) for s in self.SESSIONS for u in self.USERS
            if (s,u) in self.SU and (s,role) in self.SR):
                self.DeleteSession(u,s)            # maintain sessions

    def DeassignUser(self, user, role):
        assert user in self.USERS
        assert role in self.ROLES
        assert (user,role) in self.UR
        self.UR.remove((user,role))
        for s in set(s for s in self.SESSIONS 
            if (s,user) in self.SU and (s,role) in self.SR):
                self.DeleteSession(user,s)            # maintain sessions

    def GrantPermission(self, operation, object, role):
        assert operation in self.OPS and object in self.OBJS
        assert role in self.ROLES
        assert ((operation,object),role) not in self.PR  #+
        self.PR.add(((operation,object),role))

    def RevokePermission(self, operation, object, role):
        assert operation in self.OPS and object in self.OBJS
        assert role in self.ROLES
        assert ((operation,object),role) in self.PR
        self.PR.remove(((operation,object),role))

# supporting system functions

    def CreateSession(self, user, session, ars):
        # to check DSD, but self.checkDSD(self.DsdNR,self.DsdNC) is no good
        added=set()
        for role in ars:
            if (session,role) not in self.SR:
                self.SR.add((session,role))
                added.add((session,role))
        good = self.checkDSD() 
        for k in added:
            self.SR.remove((k[0],k[1]))
        assert good
        assert user in self.USERS
        assert session not in self.SESSIONS
        assert ars.issubset(self.AssignedRoles(user))
        self.SU.add((session,user))
        for r in ars:
            self.SR.add( (session,r) )
        self.SESSIONS.add(session)

    def AddActiveRole(self, user, session, role):
        # to check DSD, as in CreateSession except to | one pair
        added=set()
        if (session,role) not in self.SR:
            self.SR.add((session,role))
            added.add((session,role))
        good=self.CheckDSD() 
        for k in added:
            self.SR.remove((k[0],k[1]))
        assert good
        assert user in self.USERS
        assert session in self.SESSIONS
        assert role in self.ROLES
        assert (session,user) in self.SU
        assert (session,role) not in self.SR
        assert role in self.AssignedRoles(user)
        self.SR.add((session,role))


    def DeleteSession(self, user, session):
        assert user in self.USERS
        assert session in self.SESSIONS
        assert (session,user) in self.SU
        self.SU.remove((session,user))
        self.SR -= set((session,r) for r in self.ROLES)    # maintain SR
        self.SESSIONS.remove(session)            # maintain SESSIONS


    def DropActiveRole(self, user, session, role):
        assert user in self.USERS
        assert session in self.SESSIONS
        assert role in self.ROLES
        assert (session,user) in self.SU
        assert (session,role) in self.SR

        self.SR.remove((session,role))

    def CheckAccess(self, session, operation, object):
        assert session in self.SESSIONS
        assert operation in self.OPS
        assert object in self.OBJS
        return bool(set(r for r in self.ROLES if (session,r) in self.SR and ((operation,object),r) in self.PR))
        

# review functions

    def AssignedUsers(self, role):
        assert role in self.ROLES
        return set(u for u in self.USERS if (u,role) in self.UR)

    def AssignedRoles(self, user):
        assert user in self.USERS
        return set(r for r in self.ROLES if (user,r) in self.UR)

# advanced review functions

    def RolePermissions(self, role):
        assert role in self.ROLES
        return set((op,obj) for op in self.OPS for obj in self.OBJS
           if ((op,obj),role) in self.PR)
    def UserPermissions(self, user):
        assert user in self.USERS
        return set((op,obj)  for r in self.ROLES for op in self.OPS for obj in self.OBJS 
                    if (user,r) in self.UR and ((op,obj),r) in self.PR)

    def SessionRoles(self, session):
        assert session in self.SESSIONS
        return set(r for r in self.ROLES if (session,r) in self.SR)

    def SessionPermissions(self, session):
        assert session in self.SESSIONS
        return set((op,obj) for r in self.ROLES for op in self.OPS for obj in self.OBJS 
            if (session,r) in self.SR and ((op,obj),r) in self.PR)

    def RoleOperationsOnObject(self, role, obj):
        assert role in self.ROLES 
        assert obj in self.OBJS
        return set(op for op in self.OPS if ((op,obj),role) in self.PR)

    def UserOperationsOnObject(self, user, object):
        assert user in self.USERS
        assert object in self.OBJS
        return set(op for r in self.ROLES for op in self.OPS
                   if (user,r) in self.UR and ((op,object),r) in self.PR)

    def AddOperation (self,operation):
        self.OPS.add(operation)
    def AddObject (self,OBJ):
        self.OBJS.add(OBJ)
    def AddPermission(self,operation,obj):
        pass

    # SSD constraint
    def checkSSD(self):
        return not bool(set(u for u in self.USERS for (name,c) in self.SsdNC
                            if len(set(r for r in set(r for r in self.ROLES if (u,r) in self.UR)
                                           if (name,r) in self.SsdNR))
                                   > c))

# administrative commands: 1 redefined, but just add check for SSD;
# and 5 new ones defined, where non-deletion ones check SSD

    def AssignUser(self, user, role):
        # to check SSD, but self.checkSSD(self.SsdNR,self.SsdNC) is no good
        assert user in self.USERS
        assert role in self.ROLES
        assert (user,role) not in self.UR
        self.UR.add((user,role))
        good=self.checkSSD()
        if not good:
            self.UR.remove((u,r))
        assert good

    def CreateSsdSet(self, name, roles, c):
        assert name not in self.SsdNAMES
        assert roles.issubset(self.ROLES)
        assert 1<=c<=len(roles)-1
        AddedSsdNR=set()
        for r in roles:
            if (name,r) not in self.SsdNR:
                AddedSsdNR.add((name,r))
                self.SsdNR.add((name,r))
        AddedSsdNC=set()
        if (name,c) not in self.SsdNC:
            AddedSsdNC.add((name,c))
            self.SsdNC.add((name,c))
          
        good=self.checkSSD()
        if not good:
            for (name,r) in AddedSsdNR:
                self.SsdNR.remove((name,r))
            for (name,c) in AddedSsdNC:
                self.SsdNC.remove((name,c))
        assert good

        self.SsdNC.add((name,c))

    def DeleteSsdSet(self, name):
        assert name in self.SsdNAMES
        self.SsdNR -= set((name,r) for r in self.SsdRoleSetRoles(name))
        self.SsdNC.remove((name,self.SsdRoleSetCardinality(name)))
        self.SsdNAMES.remove(name)                      # delete ssd name last

    def AddSsdRoleMember(self, name, role):
        assert name in self.SsdNAMES
        assert role in self.ROLES
        assert role not in self.SsdRoleSetRoles(name)
        AddedSsdNR=set()
        if (name,role) not in self.SsdNR:
            AddedSsdNR.add((name,role))
            self.SsdNR.add((name,role))
        good=self.checkSSD()
        if not good:
            for (name,r) in AddedSsdNR:
                self.SsdNR.remove((name,r))
        assert good

    def DeleteSsdRoleMember(self, name, role):
        assert name in self.SsdNAMES
        assert role in self.SsdRoleSetRoles(name)
        assert self.SsdRoleSetCardinality(name)<=len(self.SsdRoleSetRoles(name))-2
        self.SsdNR.remove((name,role))

    def SetSsdSetCardinality(self, name, c):
        assert name in self.SsdNAMES
        assert 1<=c<=len(self.SsdRoleSetRoles(name))-1
        NegSsdNC=set()
        for (name,c) in set((name,self.SsdRoleSetCardinality(name))):
            if (name,c) in self.SsdNC:
                self.SsdNC.remove((name,c))
                NegSsdNC.add((name,c))
        PosSsdNC=set()
        if (name,c) not in self.SsdNC:
            self.SsdNC.add((name,c))
            PosSsdNC.add((name,c))
        good=self.checkSSD()
        if not good:
            for (name,c) in PosSsdNC:
                self.SsdNC.remove((name,c))
            for (name,c) in NegSsdNC:
                self.SsdNC.add((name,c))
        assert good
        pass

# review functions: 3 new ones defined

    def SsdRoleSets(self):
        return self.SsdNAMES

    def SsdRoleSetRoles(self, name):
        assert name in self.SsdNAMES
        return set(r for (n,r) in self.SsdNR if n==name)
#alt    return set(r for r in self.ROLES if (name,r) in self.SsdNR)

    def SsdRoleSetCardinality(self, name):
        assert name in self.SsdNAMES
        return set(c for (n,c) in self.SsdNC if n==name).pop()
   
   # DSD constraint, as in CoreRBACwithSSD and GeneralHierRBACwithSSD,
    # except to use SESSIONS, SessionRoles, and use Dsd/DSD instead of Ssd/SSD
    def checkDSD(self):
        return not bool(set(s for s in self.SESSIONS for (name,c) in self.DsdNC
                            if len(set(r for r in set(r for r in self.ROLES if (s,r) in self.SR)
                                           if (name,r) in self.DsdNR))
                                   > c))

# administrative commands: 5 new ones added, where non-deletion ones check DSD,
# same as in CoreRBACwithSSD, except to use Dsd/DSD instead of Ssd/SSD

    def CreateDsdSet(self, name, roles, c):
        assert name not in self.DsdNAMES
        assert roles.issubset(self.ROLES)
        assert 1<=c<=len(roles)-1
        negDsdNR=set()
        for r in roles:
            if (name,r) not in self.DsdNR:
                self.DsdNR.add( (name,r) )
                negDsdNR.add( (name,r))
        negDsdNC=set()
        if (name,c) not in self.DsdNC:
            self.DsdNC.add( (name,c))
            negDsdNC.add( (name,c))
        assert self.checkDSD()
        self.DsdNAMES.add(name)

    def DeleteDsdSet(self, name):
        assert name in self.DsdNAMES
        self.DsdNR -= set((name,r) for r in self.DsdRoleSetRoles(name))
        self.DsdNC.remove((name,self.DsdRoleSetCardinality(name)))
        self.DsdNAMES.remove(name)                      # delete dsd name last

    def AddDsdRoleMember(self, name, role):
        assert name in self.DsdNAMES
        assert role in self.ROLES
        assert role not in self.DsdRoleSetRoles(name)
        self.DsdNR.add( (name,role) )
        assert self.checkDSD()

    def DeleteDsdRoleMember(self, name, role):
        assert name in self.DsdNAMES
        assert role in self.DsdRoleSetRoles(name)
        assert self.DsdRoleSetCardinality(name)<=len(self.DsdRoleSetRoles(name))-2
        self.DsdNR.remove((name,role))

    def SetDsdSetCardinality(self, name, c):
        assert name in self.DsdNAMES
        assert 1<=c<=len(self.DsdRoleSetRoles(name))-1
        self.DsdNC.remove((name,self.DsdRoleSetCardinality(name)))
        self.DsdNC.add((name,c))
        assert self.checkDSD()
  
# review functions: 3 new ones defined, same as in CoreRBACwithSSD, except
# to use Dsd instead of Ssd

    def DsdRoleSets(self):
        return self.DsdNAMES

    def DsdRoleSetRoles(self, name):
        assert name in self.DsdNAMES
        return set(r for (n,r) in self.DsdNR if n==name)

    def DsdRoleSetCardinality(self, name):
        assert name in self.DsdNAMES
        return set(c for (n,c) in self.DsdNC if n==name).pop() 

