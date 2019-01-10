class MultiMap:
    def __init__(self):
        self.dct = {}  
        
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
            if  not s:
                del self.dct[k]
                
            
        
    
class coreRBAC:
    def __init__(self):
        self.OBJS = set() 
        self.MapR2P_8_0_1__EXPR__ = MultiMap() 
        self.OPS = set() 
        self.MapRO2A_9_1_1__EXPR__ = MultiMap() 
        self.MapRO2A_9_0_1__EXPR__ = MultiMap() 
        self.MapR2P_8_0_1__EXPR__ = MultiMap() 
        self.USERS = set() 
        self.MapR2SU_12_0_1__EXPR__ = MultiMap() 
        self.MapR2U_7_0_1__EXPR__ = MultiMap() 
        self.ROLES = set() 
        self.MapS2P_14_0_1__EXPR__ = MultiMap() 
        self.SRMapR2S_14_0_1__EXPR__ = MultiMap() 
        self.PRMapR2P_14_0_1__EXPR__ = MultiMap() 
        self.MapU2P_13_0_1__EXPR__ = MultiMap() 
        self.URMapR2U = MultiMap() 
        self.PRMapR2P_13_0_1__EXPR__ = MultiMap() 
        self.MapS2R_6_0_1__EXPR__ = MultiMap() 
        self.MapU2R_5_0_1__EXPR__ = MultiMap() 
        self.MapSP2R = MultiMap() 
        self.PR = set() 
        self.MapS2P_14_0_1__EXPR__ = MultiMap() 
        self.PRMapR2P_14_0_1__EXPR__ = MultiMap() 
        self.MapU2P_13_0_1__EXPR__ = MultiMap() 
        self.PRMapR2P_13_0_1__EXPR__ = MultiMap() 
        self.MapRO2A_9_1_1__EXPR__ = MultiMap() 
        self.MapRO2A_9_0_1__EXPR__ = MultiMap() 
        self.MapR2P_8_0_1__EXPR__ = MultiMap() 
        self.MapSP2R = MultiMap() 
        self.PRMapR2P = MultiMap() 
        self.UR = set() 
        self.MapU2P_13_0_1__EXPR__ = MultiMap() 
        self.URMapR2U = MultiMap() 
        self.MapR2U_7_0_1__EXPR__ = MultiMap() 
        self.URMapU2R_7_0_1__EXPR__ = MultiMap() 
        self.MapU2R_5_0_1__EXPR__ = MultiMap() 
        self.URMapR2U = MultiMap() 
        self.SESSIONS = set() 
        self.MapR2SU_12_0_1__EXPR__ = MultiMap() 
        self.MapUR2S_11_0_1__EXPR__ = MultiMap() 
        self.MapU2S_10_0_1__EXPR__ = MultiMap() 
        self.SU = set() 
        self.SUMapS2U_12_0_1__EXPR__ = MultiMap() 
        self.SUMapU2S_12_0_1__EXPR__ = MultiMap() 
        self.MapR2SU_12_0_1__EXPR__ = MultiMap() 
        self.MapUR2S_11_0_1__EXPR__ = MultiMap() 
        self.SUMapS2U_11_0_1__EXPR__ = MultiMap() 
        self.MapU2S_10_0_1__EXPR__ = MultiMap() 
        self.SUMapS2U_10_0_1__EXPR__ = MultiMap() 
        self.SR = set() 
        self.MapU2P_14_0_1__EXPR__ = MultiMap() 
        self.SRMapR2S_14_0_1__EXPR__ = MultiMap() 
        self.SRMapS2R = MultiMap() 
        self.MapR2SU_12_0_1__EXPR__ = MultiMap() 
        self.MapUR2S_11_0_1__EXPR__ = MultiMap() 
        self.SRMapS2R = MultiMap() 
        self.MapS2R_6_0_1__EXPR__ = MultiMap() 
        self.SRMapR2S_6_0_1__EXPR__ = MultiMap() 
        self.MapSP2R = MultiMap() 
        self.SRMapR2S = MultiMap() 
        
    def AddUser(self, user):
        assert user not in self.USERS
        self.USERS.add(user)
        for s in self.SUMapU2S_12_0_1__EXPR__.get(user):
            if s in self.SESSIONS:
                for r in self.SRMapS2R.get(s):
                    if (s,user) not in self.MapR2SU_12_0_1__EXPR__.get(r):
                        self.MapR2SU_12_0_1__EXPR__.add(r, (s,user))
                        
                    
                
            
        for r in self.URMapU2R_7_0_1__EXPR__.get(user):
            if user not in self.MapR2U_7_0_1__EXPR__.get(r):
                self.MapR2U_7_0_1__EXPR__.add(r, user)
                
            
        
    def DeleteUser(self, user):
        assert user in self.USERS
        for r in self.URMapU2R.get(user).copy():
            if r in self.ROLES:
                if r in self.MapU2R_5_0_1__EXPR__.get(user):
                    self.MapU2R_5_0_1__EXPR__.remove(user, r)
                    
                
            self.URMapR2U.remove(r, user)
            if user in self.USERS:
                if user in self.MapR2U_7_0_1__EXPR__.get(r):
                    self.MapR2U_7_0_1__EXPR__.remove(r, user)
                    
                
            self.URMapU2R_7_0_1__EXPR__.remove(user, r)
            for (op,obj,) in self.PRMapR2P_13_0_1__EXPR__.get(r):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) in self.MapU2P_13_0_1__EXPR__.get(user):
                            self.MapU2P_13_0_1__EXPR__.remove(user, (op,obj))
                            
                        
                    
                
            self.URMapR2U.remove(r, user)
            self.UR.remove((user,r))
            
        for s in self.MapU2S_10_0_1__EXPR__.get(user):
            self.DeleteSession(user, s)
            
        for r in self.URMapU2R_7_0_1__EXPR__.get(user):
            if user in self.MapR2U_7_0_1__EXPR__.get(r):
                self.MapR2U_7_0_1__EXPR__.remove(r, user)
                
            
        for s in self.SUMapU2S_12_0_1__EXPR__.get(user):
            if s in self.SESSIONS:
                for r in self.SRMapS2R.get(s):
                    if (s,user) in self.MapR2SU_12_0_1__EXPR__.get(r):
                        self.MapR2SU_12_0_1__EXPR__.remove(r, (s,user))
                        
                    
                
            
        self.USERS.remove(user)
        
    def AddRole(self, role):
        assert role not in self.ROLES
        self.ROLES.add(role)
        for (op,obj,) in self.PRMapR2P_14_0_1__EXPR__.get(role):
            for s in self.SRMapR2S_14_0_1__EXPR__.get(role):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) not in self.MapS2P_14_0_1__EXPR__.get(s):
                            self.MapS2P_14_0_1__EXPR__.add(s, (op,obj))
                            
                        
                    
                
            
        for (op,obj,) in self.PRMapR2P_13_0_1__EXPR__.get(role):
            for u in self.URMapR2U.get(role):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) not in self.MapU2P_13_0_1__EXPR__.get(u):
                            self.MapU2P_13_0_1__EXPR__.add(u, (op,obj))
                            
                        
                    
                
            
        for s in self.SRMapR2S_6_0_1__EXPR__.get(role):
            if role not in self.MapS2R_6_0_1__EXPR__.get(s):
                self.MapS2R_6_0_1__EXPR__.add(s, role)
                
            
        for u in self.URMapR2U.get(role):
            if role not in self.MapU2R_5_0_1__EXPR__.get(u):
                self.MapU2R_5_0_1__EXPR__.add(u, role)
                
            
        for s in self.SRMapR2S.get(role):
            for (op,obj,) in self.PRMapR2P.get(role):
                if role not in self.MapSP2R.get((s,op,obj)):
                    self.MapSP2R.add((s,op,obj), role)
                    
                
            
        
    def DeleteRole(self, role):
        assert role in self.ROLES
        for s in self.SRMapR2S.get(role):
            for (op,obj,) in self.PRMapR2P.get(role):
                if role in self.MapSP2R.get((s,op,obj)):
                    self.MapSP2R.remove((s,op,obj), role)
                    
                
            
        for u in self.URMapR2U.get(role):
            if role in self.MapU2R_5_0_1__EXPR__.get(u):
                self.MapU2R_5_0_1__EXPR__.remove(u, role)
                
            
        for s in self.SRMapR2S_6_0_1__EXPR__.get(role):
            if role in self.MapS2R_6_0_1__EXPR__.get(s):
                self.MapS2R_6_0_1__EXPR__.remove(s, role)
                
            
        for (op,obj,) in self.PRMapR2P_13_0_1__EXPR__.get(role):
            for u in self.URMapR2U.get(role):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) in self.MapU2P_13_0_1__EXPR__.get(u):
                            self.MapU2P_13_0_1__EXPR__.remove(u, (op,obj))
                            
                        
                    
                
            
        for (op,obj,) in self.PRMapR2P_14_0_1__EXPR__.get(role):
            for s in self.SRMapR2S_14_0_1__EXPR__.get(role):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) in self.MapS2P_14_0_1__EXPR__.get(s):
                            self.MapS2P_14_0_1__EXPR__.remove(s, (op,obj))
                            
                        
                    
                
            
        self.ROLES.remove(role)
        for (op,obj,) in self.PRMapR2P.get(role).copy():
            if role in self.ROLES:
                for s in self.SRMapR2S.get(role):
                    if role in self.MapSP2R.get((s,op,obj)):
                        self.MapSP2R.add((s,op,obj), role)
                        
                    
                
            self.PRMapR2P.remove(role, (op,obj))
            if op in self.OPS:
                if obj in self.OBJS:
                    if (op,obj) in self.MapR2P_8_0_1__EXPR__.get(role):
                        self.MapR2P_8_0_1__EXPR__.remove(role, (op,obj))
                        
                    
                
            if op in self.OPS:
                if op in self.MapRO2A_9_0_1__EXPR__.get((role,obj)):
                    self.MapRO2A_9_0_1__EXPR__.remove((role,obj), op)
                    
                
            if op in self.OPS:
                if op in self.MapRO2A_9_1_1__EXPR__.get((role,obj)):
                    self.MapRO2A_9_1_1__EXPR__.remove((role,obj), op)
                    
                
            for u in self.URMapR2U.get(role):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) in self.MapU2P_13_0_1__EXPR__.get(u):
                            self.MapU2P_13_0_1__EXPR__.remove(u, (op,obj))
                            
                        
                    
                
            self.PRMapR2P_13_0_1__EXPR__.remove(role, (op,obj))
            if role in self.ROLES:
                for s in self.SRMapR2S_14_0_1__EXPR__.get(role):
                    if op in self.OPS:
                        if obj in self.OBJS:
                            if (op,obj) in self.MapS2P_14_0_1__EXPR__.get(s):
                                self.MapS2P_14_0_1__EXPR__.remove(s, (op,obj))
                                
                            
                        
                    
                self.PRMapR2P_14_0_1__EXPR__.remove(role, (op,obj))
                
            self.PR.remove(((op,obj),role))
            
        for u in self.URMapR2U.get(role).copy():
            if role in self.ROLES:
                if role in self.MapU2R_5_0_1__EXPR__.get(u):
                    self.MapU2R_5_0_1__EXPR__.remove(u, role)
                    
                
            self.URMapR2U.remove(role, u)
            if u in self.USERS:
                if u in self.MapR2U_7_0_1__EXPR__.get(role):
                    self.MapR2U_7_0_1__EXPR__.remove(role, u)
                    
                
            self.URMapU2R_7_0_1__EXPR__.remove(u, role)
            for (op,obj,) in self.PRMapR2P_13_0_1__EXPR__.get(role):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) in self.MapU2P_13_0_1__EXPR__.get(u):
                            self.MapU2P_13_0_1__EXPR__.remove(u, (op,obj))
                            
                        
                    
                
            self.URMapR2U.remove(role, u)
            self.UR.remove((u,role))
            
        for (s,u,) in self.MapR2SU_12_0_1__EXPR__.get(role):
            self.DeleteSession(u, s)
            
        
    def AssignUser(self, user, role):
        assert user in self.USERS
        assert role in self.ROLES
        assert (user,role) not in self.UR
        self.UR.add((user,role))
        for (op,obj,) in self.PRMapR2P_13_0_1__EXPR__.get(role):
            if op in self.OPS:
                if obj in self.OBJS:
                    if (op,obj) not in self.MapU2P_13_0_1__EXPR__.get(user):
                        self.MapU2P_13_0_1__EXPR__.add(user, (op,obj))
                        
                    
                
            
        self.URMapR2U.add(role, user)
        if user in self.USERS:
            if user not in self.MapR2U_7_0_1__EXPR__.get(role):
                self.MapR2U_7_0_1__EXPR__.add(role, user)
                
            
        self.URMapU2R_7_0_1__EXPR__.add(user, role)
        if role in self.ROLES:
            if role not in self.MapU2R_5_0_1__EXPR__.get(user):
                self.MapU2R_5_0_1__EXPR__.add(user, role)
                
            
        self.URMapR2U.add(role, user)
        
    def DeassignUser(self, user, role):
        assert user in self.USERS
        assert role in self.ROLES
        assert (user,role) in self.UR
        if role in self.ROLES:
            if role in self.MapU2R_5_0_1__EXPR__.get(user):
                self.MapU2R_5_0_1__EXPR__.remove(user, role)
                
            
        self.URMapR2U.remove(role, user)
        if user in self.USERS:
            if user in self.MapR2U_7_0_1__EXPR__.get(role):
                self.MapR2U_7_0_1__EXPR__.remove(role, user)
                
            
        self.URMapU2R_7_0_1__EXPR__.remove(user, role)
        for (op,obj,) in self.PRMapR2P_13_0_1__EXPR__.get(role):
            if op in self.OPS:
                if obj in self.OBJS:
                    if (op,obj) in self.MapU2P_13_0_1__EXPR__.get(user):
                        self.MapU2P_13_0_1__EXPR__.remove(user, (op,obj))
                        
                    
                
            
        self.URMapR2U.remove(role, user)
        self.UR.remove((user,role))
        for s in self.MapUR2S_11_0_1__EXPR__.get((user,role)):
            self.DeleteSession(user, s)
            
        
    def GrantPermission(self, operation, object, role):
        assert operation in self.OPS and object in self.OBJS
        assert role in self.ROLES
        assert ((operation,object),role) not in self.PR
        self.PR.add(((operation,object),role))
        if role in self.ROLES:
            for s in self.SRMapR2S_14_0_1__EXPR__.get(role):
                if operation in self.OPS:
                    if object in self.OBJS:
                        if (operation,object) not in self.MapS2P_14_0_1__EXPR__.get(s):
                            self.MapS2P_14_0_1__EXPR__.add(s, (operation,object))
                            
                        
                    
                
            self.PRMapR2P_14_0_1__EXPR__.add(role, (operation,object))
            
        for u in self.URMapR2U.get(role):
            if operation in self.OPS:
                if object in self.OBJS:
                    if (operation,object) not in self.MapU2P_13_0_1__EXPR__.get(u):
                        self.MapU2P_13_0_1__EXPR__.add(u, (operation,object))
                        
                    
                
            
        self.PRMapR2P_13_0_1__EXPR__.add(role, (operation,object))
        if operation in self.OPS:
            if operation not in self.MapRO2A_9_1_1__EXPR__.get((role,object)):
                self.MapRO2A_9_1_1__EXPR__.add((role,object), operation)
                
            
        if operation in self.OPS:
            if operation not in self.MapRO2A_9_0_1__EXPR__.get((role,object)):
                self.MapRO2A_9_0_1__EXPR__.add((role,object), operation)
                
            
        if operation in self.OPS:
            if object in self.OBJS:
                if (operation,object) not in self.MapR2P_8_0_1__EXPR__.get(role):
                    self.MapR2P_8_0_1__EXPR__.add(role, (operation,object))
                    
                
            
        if role in self.ROLES:
            for s in self.SRMapR2S.get(role):
                if role not in self.MapSP2R.get((s,operation,object)):
                    self.MapSP2R.add((s,operation,object), role)
                    
                
            
        self.PRMapR2P.add(role, (operation,object))
        
    def RevokePermission(self, operation, object, role):
        assert operation in self.OPS and object in self.OBJS
        assert role in self.ROLES
        assert ((operation,object),role) in self.PR
        if role in self.ROLES:
            for s in self.SRMapR2S.get(role):
                if role in self.MapSP2R.get((s,operation,object)):
                    self.MapSP2R.add((s,operation,object), role)
                    
                
            
        self.PRMapR2P.remove(role, (operation,object))
        if operation in self.OPS:
            if object in self.OBJS:
                if (operation,object) in self.MapR2P_8_0_1__EXPR__.get(role):
                    self.MapR2P_8_0_1__EXPR__.remove(role, (operation,object))
                    
                
            
        if operation in self.OPS:
            if operation in self.MapRO2A_9_0_1__EXPR__.get((role,object)):
                self.MapRO2A_9_0_1__EXPR__.remove((role,object), operation)
                
            
        if operation in self.OPS:
            if operation in self.MapRO2A_9_1_1__EXPR__.get((role,object)):
                self.MapRO2A_9_1_1__EXPR__.remove((role,object), operation)
                
            
        for u in self.URMapR2U.get(role):
            if operation in self.OPS:
                if object in self.OBJS:
                    if (operation,object) in self.MapU2P_13_0_1__EXPR__.get(u):
                        self.MapU2P_13_0_1__EXPR__.remove(u, (operation,object))
                        
                    
                
            
        self.PRMapR2P_13_0_1__EXPR__.remove(role, (operation,object))
        if role in self.ROLES:
            for s in self.SRMapR2S_14_0_1__EXPR__.get(role):
                if operation in self.OPS:
                    if object in self.OBJS:
                        if (operation,object) in self.MapS2P_14_0_1__EXPR__.get(s):
                            self.MapS2P_14_0_1__EXPR__.remove(s, (operation,object))
                            
                        
                    
                
            self.PRMapR2P_14_0_1__EXPR__.remove(role, (operation,object))
            
        self.PR.remove(((operation,object),role))
        
    def CreateSession(self, user, session, ars):
        assert user in self.USERS
        assert session not in self.SESSIONS
        assert ars.issubset(self.AssignedRoles(user))
        self.SU.add((session,user))
        if session in self.SESSIONS:
            if user in self.USERS:
                for r in self.SRMapS2R.get(session):
                    if (session,user) not in self.MapR2SU_12_0_1__EXPR__.get(r):
                        self.MapR2SU_12_0_1__EXPR__.add(r, (session,user))
                        
                    
                
            
        self.SUMapS2U_12_0_1__EXPR__.add(session, user)
        self.SUMapU2S_12_0_1__EXPR__.add(user, session)
        for r in self.SRMapS2R.get(session):
            if session not in self.MapUR2S_11_0_1__EXPR__.get((user,r)):
                self.MapUR2S_11_0_1__EXPR__.add((user,r), session)
                
            
        self.SUMapS2U_11_0_1__EXPR__.add(session, user)
        if session in self.SESSIONS:
            if session not in self.MapU2S_10_0_1__EXPR__.get(user):
                self.MapU2S_10_0_1__EXPR__.add(user, session)
                
            
        self.SUMapS2U_10_0_1__EXPR__.add(session, user)
        for r in ars:
            self.SR.add((session,r))
            for (op,obj,) in self.PRMapR2P_14_0_1__EXPR__.get(r):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) not in self.MapS2P_14_0_1__EXPR__.get(session):
                            self.MapS2P_14_0_1__EXPR__.add(session, (op,obj))
                            
                        
                    
                
            self.SRMapR2S_14_0_1__EXPR__.add(r, session)
            for u in self.SUMapS2U_12_0_1__EXPR__.get(session):
                if session in self.SESSIONS:
                    if u in self.USERS:
                        if (session,u) not in self.MapR2SU_12_0_1__EXPR__.get(r):
                            self.MapR2SU_12_0_1__EXPR__.add(r, (session,u))
                            
                        
                    
                
            for u in self.SUMapS2U_11_0_1__EXPR__.get(session):
                if session not in self.MapUR2S_11_0_1__EXPR__.get((u,r)):
                    self.MapUR2S_11_0_1__EXPR__.add((u,r), session)
                    
                
            self.SRMapS2R.add(session, r)
            if r not in self.MapS2R_6_0_1__EXPR__.get(session):
                self.MapS2R_6_0_1__EXPR__.add(session, r)
                
            self.SRMapR2S_6_0_1__EXPR__.add(r, session)
            if r in self.ROLES:
                for (op,obj,) in self.PRMapR2P.get(r):
                    if r not in self.MapSP2R.get((session,op,obj)):
                        self.MapSP2R.add((session,op,obj), r)
                        
                    
                
            self.SRMapR2S.add(r, session)
            
        self.SESSIONS.add(session)
        for u in self.SUMapS2U_12_0_1__EXPR__.get(session):
            if u in self.USERS:
                for r in self.SRMapS2R.get(session):
                    if (session,u) not in self.MapR2SU_12_0_1__EXPR__.get(r):
                        self.MapR2SU_12_0_1__EXPR__.add(r, (session,u))
                        
                    
                
            
        for u in self.SUMapS2U_11_0_1__EXPR__.get(session):
            for r in self.SRMapS2R.get(session):
                if session not in self.MapUR2S_11_0_1__EXPR__.get((u,r)):
                    self.MapUR2S_11_0_1__EXPR__.add((u,r), session)
                    
                
            
        for u in self.SUMapS2U_10_0_1__EXPR__.get(session):
            if session not in self.MapU2S_10_0_1__EXPR__.get(u):
                self.MapU2S_10_0_1__EXPR__.add(u, session)
                
            
        
    def DeleteSession(self, user, session):
        assert user in self.USERS
        assert session in self.SESSIONS
        assert (session,user) in self.SU
        if session in self.SESSIONS:
            if session in self.MapU2S_10_0_1__EXPR__.get(user):
                self.MapU2S_10_0_1__EXPR__.remove(user, session)
                
            
        self.SUMapS2U_10_0_1__EXPR__.remove(session, user)
        for r in self.SRMapS2R.get(session):
            if session in self.MapUR2S_11_0_1__EXPR__.get((user,r)):
                self.MapUR2S_11_0_1__EXPR__.remove((user,r), session)
                
            
        self.SUMapS2U_11_0_1__EXPR__.remove(session, user)
        if session in self.SESSIONS:
            if user in self.USERS:
                for r in self.SRMapS2R.get(session):
                    if (session,user) in self.MapR2SU_12_0_1__EXPR__.get(r):
                        self.MapR2SU_12_0_1__EXPR__.remove(r, (session,user))
                        
                    
                
            
        self.SUMapS2U_12_0_1__EXPR__.remove(session, user)
        self.SUMapU2S_12_0_1__EXPR__.remove(user, session)
        self.SU.remove((session,user))
        for r in self.SRMapS2R.get(session).copy():
            if r in self.ROLES:
                for (op,obj,) in self.PRMapR2P.get(r):
                    if r in self.MapSP2R.get((session,op,obj)):
                        self.MapSP2R.remove((session,op,obj), r)
                        
                    
                
            self.SRMapR2S.remove(r, session)
            if r in self.MapS2R_6_0_1__EXPR__.get(session):
                self.MapS2R_6_0_1__EXPR__.remove(session, r)
                
            self.SRMapR2S_6_0_1__EXPR__.remove(r, session)
            for u in self.SUMapS2U_11_0_1__EXPR__.get(session):
                if session in self.MapUR2S_11_0_1__EXPR__.get((u,r)):
                    self.MapUR2S_11_0_1__EXPR__.remove((u,r), session)
                    
                
            self.SRMapS2R.remove(session, r)
            for u in self.SUMapS2U_12_0_1__EXPR__.get(session):
                if session in self.SESSIONS:
                    if u in self.USERS:
                        if (session,u) in self.MapR2SU_12_0_1__EXPR__.get(r):
                            self.MapR2SU_12_0_1__EXPR__.remove(r, (session,u))
                            
                        
                    
                
            for (op,obj,) in self.PRMapR2P_14_0_1__EXPR__.get(r):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) in self.MapS2P_14_0_1__EXPR__.get(session):
                            self.MapS2P_14_0_1__EXPR__.remove(session, (op,obj))
                            
                        
                    
                
            self.SRMapR2S_14_0_1__EXPR__.remove(r, session)
            self.SR.remove((session,r))
            
        for u in self.SUMapS2U_10_0_1__EXPR__.get(session):
            if session in self.MapU2S_10_0_1__EXPR__.get(u):
                self.MapU2S_10_0_1__EXPR__.remove(u, session)
                
            
        for u in self.SUMapS2U_11_0_1__EXPR__.get(session):
            for r in self.SRMapS2R.get(session):
                if session in self.MapUR2S_11_0_1__EXPR__.get((u,r)):
                    self.MapUR2S_11_0_1__EXPR__.remove((u,r), session)
                    
                
            
        for u in self.SUMapS2U_12_0_1__EXPR__.get(session):
            if u in self.USERS:
                for r in self.SRMapS2R.get(session):
                    if (session,u) in self.MapR2SU_12_0_1__EXPR__.get(r):
                        self.MapR2SU_12_0_1__EXPR__.remove(r, (session,u))
                        
                    
                
            
        self.SESSIONS.remove(session)
        
    def AddActiveRole(self, user, session, role):
        assert user in self.USERS
        assert session in self.SESSIONS
        assert role in self.ROLES
        assert (session,user) in self.SU
        assert (session,role) not in self.SR
        assert role in self.AssignedRoles(user)
        self.SR.add((session,role))
        for (op,obj,) in self.PRMapR2P_14_0_1__EXPR__.get(role):
            if op in self.OPS:
                if obj in self.OBJS:
                    if (op,obj) not in self.MapS2P_14_0_1__EXPR__.get(session):
                        self.MapS2P_14_0_1__EXPR__.add(session, (op,obj))
                        
                    
                
            
        self.SRMapR2S_14_0_1__EXPR__.add(role, session)
        for u in self.SUMapS2U_12_0_1__EXPR__.get(session):
            if session in self.SESSIONS:
                if u in self.USERS:
                    if (session,u) not in self.MapR2SU_12_0_1__EXPR__.get(role):
                        self.MapR2SU_12_0_1__EXPR__.add(role, (session,u))
                        
                    
                
            
        for u in self.SUMapS2U_11_0_1__EXPR__.get(session):
            if session not in self.MapUR2S_11_0_1__EXPR__.get((u,role)):
                self.MapUR2S_11_0_1__EXPR__.add((u,role), session)
                
            
        self.SRMapS2R.add(session, role)
        if role not in self.MapS2R_6_0_1__EXPR__.get(session):
            self.MapS2R_6_0_1__EXPR__.add(session, role)
            
        self.SRMapR2S_6_0_1__EXPR__.add(role, session)
        if role in self.ROLES:
            for (op,obj,) in self.PRMapR2P.get(role):
                if role not in self.MapSP2R.get((session,op,obj)):
                    self.MapSP2R.add((session,op,obj), role)
                    
                
            
        self.SRMapR2S.add(role, session)
        
    def DropActiveRole(self, user, session, role):
        assert user in self.USERS
        assert session in self.SESSIONS
        assert role in self.ROLES
        assert (session,user) in self.SU
        assert (session,role) in self.SR
        if role in self.ROLES:
            for (op,obj,) in self.PRMapR2P.get(role):
                if role in self.MapSP2R.get((session,op,obj)):
                    self.MapSP2R.remove((session,op,obj), role)
                    
                
            
        self.SRMapR2S.remove(role, session)
        if role in self.MapS2R_6_0_1__EXPR__.get(session):
            self.MapS2R_6_0_1__EXPR__.remove(session, role)
            
        self.SRMapR2S_6_0_1__EXPR__.remove(role, session)
        for u in self.SUMapS2U_11_0_1__EXPR__.get(session):
            if session in self.MapUR2S_11_0_1__EXPR__.get((u,role)):
                self.MapUR2S_11_0_1__EXPR__.remove((u,role), session)
                
            
        self.SRMapS2R.remove(session, role)
        for u in self.SUMapS2U_12_0_1__EXPR__.get(session):
            if session in self.SESSIONS:
                if u in self.USERS:
                    if (session,u) in self.MapR2SU_12_0_1__EXPR__.get(role):
                        self.MapR2SU_12_0_1__EXPR__.remove(role, (session,u))
                        
                    
                
            
        for (op,obj,) in self.PRMapR2P_14_0_1__EXPR__.get(role):
            if op in self.OPS:
                if obj in self.OBJS:
                    if (op,obj) in self.MapS2P_14_0_1__EXPR__.get(session):
                        self.MapS2P_14_0_1__EXPR__.remove(session, (op,obj))
                        
                    
                
            
        self.SRMapR2S_14_0_1__EXPR__.remove(role, session)
        self.SR.remove((session,role))
        
    def CheckAccess(self, session, operation, object):
        assert session in self.SESSIONS
        assert operation in self.OPS
        assert object in self.OBJS
        return bool(self.MapSP2R.get((session,operation,object)))
    def AssignedUsers(self, role):
        assert role in self.ROLES
        return self.MapR2U_7_0_1__EXPR__.get(role)
    def AssignedRoles(self, user):
        assert user in self.USERS
        return self.MapU2R_5_0_1__EXPR__.get(user)
    def RolePermissions(self, role):
        assert role in self.ROLES
        return self.MapR2P_8_0_1__EXPR__.get(role)
    def UserPermissions(self, user):
        assert user in self.USERS
        return self.MapU2P_13_0_1__EXPR__.get(user)
    def SessionRoles(self, session):
        assert session in self.SESSIONS
        return self.MapS2R_6_0_1__EXPR__.get(session)
    def SessionPermissions(self, session):
        assert session in self.SESSIONS
        return self.MapS2P_14_0_1__EXPR__.get(session)
    def RoleOperationsOnObject(self, role, obj):
        assert role in self.ROLES
        assert obj in self.OBJS
        return self.MapRO2A_9_0_1__EXPR__.get((role,object))
    def UserOperationsOnObject(self, user, obj):
        assert user in self.USERS
        assert obj in self.OBJS
        return self.MapRO2A_9_1_1__EXPR__.get((role,object))
    def AddOperation(self, operation):
        self.OPS.add(operation)
        
    def AddObject(self, OBJ):
        self.OBJS.add(OBJ)
        
    def AddPermission(self, operation, obj):
        pass 
    
