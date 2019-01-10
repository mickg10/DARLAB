class MultiMap: 
    def __init__ (self):
        self.dct={}
    def get(self, k):
        if k in self.dct:
            return self.dct[k]
        else:
            return set()

    def add(self, k, v):
        if k not in self.dct: 
            self.dct[k] = s = set()
            s.add(v) 
        else: 
            self.dct[k].add(v)
 
    def remove(self, k, v):
        if k in self.dct:
            s = self.dct[k]
            s.remove(v)
            if not s:
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

    def AssignUser(self, user, role):
        assert user in self.USERS
        assert role in self.ROLES
        assert (user,role) not in self.UR
        self.UR.add((user,role))

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
        assert user in self.USERS
        assert session not in self.SESSIONS
        assert ars.issubset(self.AssignedRoles(user))
        self.SU.add((session,user))
        for r in ars:
            self.SR.add( (session,r) )
        self.SESSIONS.add(session)

    def DeleteSession(self, user, session):
        assert user in self.USERS
        assert session in self.SESSIONS
        assert (session,user) in self.SU
        self.SU.remove((session,user))
        self.SR -= set((session,r) for r in self.ROLES)    # maintain SR
        self.SESSIONS.remove(session)            # maintain SESSIONS

    def AddActiveRole(self, user, session, role):
        assert user in self.USERS
        assert session in self.SESSIONS
        assert role in self.ROLES
        assert (session,user) in self.SU
        assert (session,role) not in self.SR
        assert role in self.AssignedRoles(user)
        self.SR.add((session,role))

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

    def UserOperationsOnObject(self, user, obj):
        assert user in self.USERS
        assert obj in self.OBJS
        return set(op for op in self.OPS for r in self.ROLES if (user,r) in self.UR and ((op,obj),r) in self.PR)

    def AddOperation (self,operation):
        self.OPS.add(operation)
    def AddObject (self,OBJ):
        self.OBJS.add(OBJ)
    def AddPermission(self,operation,obj):
        pass

