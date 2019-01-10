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
            set.add(s, v)
            
        else:
            s = self.dct[k] 
            set.add(s, v)
            
        
    def remove(self, k, v):
        if k in self.dct:
            s = self.dct[k] 
            set.remove(s, v)
            if ( not bool(s)):
                del self.dct[k]
                
            
        
    
class coreRBAC:
    def __init__(self):
        self.OBJS = set() 
        self.MapR2P_0_15_0_1__REPR__ = MultiMap() 
        self.OPS = set() 
        self.MapRO2A_0_16_0_1__REPR__ = MultiMap() 
        self.MapR2P_0_15_0_1__REPR__ = MultiMap() 
        self.USERS = set() 
        self.MapR2U_0_14_0_1__REPR__ = MultiMap() 
        self.MapR2SU_0_19_0_1__REPR__ = MultiMap() 
        self.V_0_3_0_1__REPR__ = set() 
        self.Y_0_3_0_1__REPR__ = MultiMap() 
        self.X_0_3_0_1__REPR__ = MultiMap() 
        self.ROLES = set() 
        self.MapUO2A_0_22_0_1__REPR__ = MultiMap() 
        self.URMapR2U = MultiMap() 
        self.PRMapR2P_0_22_0_1__REPR__ = MultiMap() 
        self.MapS2P_0_21_0_1__REPR__ = MultiMap() 
        self.SRMapR2S_0_21_0_1__REPR__ = MultiMap() 
        self.PRMapR2P_0_21_0_1__REPR__ = MultiMap() 
        self.MapU2P_0_20_0_1__REPR__ = MultiMap() 
        self.URMapR2U = MultiMap() 
        self.PRMapR2P_0_20_0_1__REPR__ = MultiMap() 
        self.MapS2R_0_13_0_1__REPR__ = MultiMap() 
        self.MapU2R_0_12_0_1__REPR__ = MultiMap() 
        self.MapSP2R = MultiMap() 
        self.PR = set() 
        self.MapUO2A_0_22_0_1__REPR__ = MultiMap() 
        self.PRMapR2P_0_22_0_1__REPR__ = MultiMap() 
        self.MapS2P_0_21_0_1__REPR__ = MultiMap() 
        self.PRMapR2P_0_21_0_1__REPR__ = MultiMap() 
        self.MapU2P_0_20_0_1__REPR__ = MultiMap() 
        self.PRMapR2P_0_20_0_1__REPR__ = MultiMap() 
        self.MapRO2A_0_16_0_1__REPR__ = MultiMap() 
        self.MapR2P_0_15_0_1__REPR__ = MultiMap() 
        self.MapSP2R = MultiMap() 
        self.PRMapR2P = MultiMap() 
        self.UR = set() 
        self.MapR2U_0_14_0_1__REPR__ = MultiMap() 
        self.URMapU2R_0_14_0_1__REPR__ = MultiMap() 
        self.MapUO2A_0_22_0_1__REPR__ = MultiMap() 
        self.URMapR2U = MultiMap() 
        self.MapU2P_0_20_0_1__REPR__ = MultiMap() 
        self.URMapR2U = MultiMap() 
        self.MapU2R_0_12_0_1__REPR__ = MultiMap() 
        self.URMapR2U = MultiMap() 
        self.MapR2U_0_0_0_1__REPR__ = MultiMap() 
        self.MapR2U_0_3_0_1__REPR__ = MultiMap() 
        self.SESSIONS = set() 
        self.MapR2SU_0_19_0_1__REPR__ = MultiMap() 
        self.MapUR2S_0_18_0_1__REPR__ = MultiMap() 
        self.MapU2S_0_17_0_1__REPR__ = MultiMap() 
        self.V_0_0_0_1__REPR__ = set() 
        self.Y_0_0_0_1__REPR__ = MultiMap() 
        self.X_0_0_0_1__REPR__ = MultiMap() 
        self.SU = set() 
        self.SUMapS2U_0_19_0_1__REPR__ = MultiMap() 
        self.SUMapU2S_0_19_0_1__REPR__ = MultiMap() 
        self.MapR2SU_0_19_0_1__REPR__ = MultiMap() 
        self.MapUR2S_0_18_0_1__REPR__ = MultiMap() 
        self.SUMapS2U_0_18_0_1__REPR__ = MultiMap() 
        self.MapU2S_0_17_0_1__REPR__ = MultiMap() 
        self.SUMapS2U_0_17_0_1__REPR__ = MultiMap() 
        self.SR = set() 
        self.MapU2P_0_21_0_1__REPR__ = MultiMap() 
        self.SRMapR2S_0_21_0_1__REPR__ = MultiMap() 
        self.SRMapS2R = MultiMap() 
        self.MapR2SU_0_19_0_1__REPR__ = MultiMap() 
        self.MapUR2S_0_18_0_1__REPR__ = MultiMap() 
        self.SRMapS2R = MultiMap() 
        self.MapS2R_0_13_0_1__REPR__ = MultiMap() 
        self.SRMapR2S_0_13_0_1__REPR__ = MultiMap() 
        self.MapSP2R = MultiMap() 
        self.SRMapR2S = MultiMap() 
        self.MapR2S_0_0_0_1__REPR__ = MultiMap() 
        self.SsdNAMES = set() 
        self.SsdNR = set() 
        self.MapN2R_0_9_0_1__REPR__ = MultiMap() 
        self.MapR2N_0_3_0_1__REPR__ = MultiMap() 
        self.SsdNC = set() 
        self.MapN2C_0_10_0_1__REPR__ = MultiMap() 
        self.MapN2C_0_3_0_1__REPR__ = MultiMap() 
        self.DsdNAMES = set() 
        self.DsdNR = set() 
        self.MapN2R_0_1_0_1__REPR__ = MultiMap() 
        self.MapR2N_0_0_0_1__REPR__ = MultiMap() 
        self.DsdNC = set() 
        self.MapN2C_0_2_0_1__REPR__ = MultiMap() 
        self.MapN2C_0_0_0_1__REPR__ = MultiMap() 
        
    def AddUser(self, user):
        assert user not in self.USERS
        self.USERS.add(user)
        for r in self.URMapU2R_0_14_0_1__REPR__.get(user):
            if user not in self.MapR2U_0_14_0_1__REPR__.get(r):
                self.MapR2U_0_14_0_1__REPR__.add(r, user)
                
            
        for s in self.SUMapU2S_0_19_0_1__REPR__.get(user):
            if s in self.SESSIONS:
                for r in self.SRMapS2R.get(s):
                    if (s,user) not in self.MapR2SU_0_19_0_1__REPR__.get(r):
                        self.MapR2SU_0_19_0_1__REPR__.add(r, (s,user))
                        
                    
                
            
        for (name_0_3_0_1__REPR__,c_0_3_0_1__REPR__,) in self.SsdNC:
            if len(self.X_0_3_0_1__REPR__[(user,name_0_3_0_1__REPR__)]) > c_0_3_0_1__REPR__:
                self.V_0_3_0_1__REPR__.add(user)
                
            
        
    def DeleteUser(self, user):
        assert user in self.USERS
        self.UR -= set(((user,r) for r in self.ROLES))
        for s in self.MapU2S_0_17_0_1__REPR__.get(user):
            self.DeleteSession(user, s)
            
        for (name_0_3_0_1__REPR__,c_0_3_0_1__REPR__,) in self.SsdNC:
            if len(self.X_0_3_0_1__REPR__[(user,name_0_3_0_1__REPR__)]) > c_0_3_0_1__REPR__:
                self.V_0_3_0_1__REPR__.remove(user)
                
            
        for (k,v,) in self.MapR2U_0_3_0_1__REPR__.dct.iteritems:
            v.remove(user)
            
        for s in self.SUMapU2S_0_19_0_1__REPR__.get(user):
            if s in self.SESSIONS:
                for r in self.SRMapS2R.get(s):
                    if (s,user) in self.MapR2SU_0_19_0_1__REPR__.get(r):
                        self.MapR2SU_0_19_0_1__REPR__.remove(r, (s,user))
                        
                    
                
            
        for r in self.URMapU2R_0_14_0_1__REPR__.get(user):
            if user in self.MapR2U_0_14_0_1__REPR__.get(r):
                self.MapR2U_0_14_0_1__REPR__.remove(r, user)
                
            
        self.USERS.remove(user)
        
    def AddRole(self, role):
        assert role not in self.ROLES
        self.ROLES.add(role)
        for u in self.URMapR2U.get(role):
            for (op,object,) in self.PRMapR2P_0_22_0_1__REPR__.get(role):
                if role in self.ROLES:
                    if op in self.OPS:
                        if op not in self.MapUO2A_0_22_0_1__REPR__.get((u,object)):
                            self.MapUO2A_0_22_0_1__REPR__.add((u,object), op)
                            
                        
                    
                
            
        for (op,obj,) in self.PRMapR2P_0_21_0_1__REPR__.get(role):
            for s in self.SRMapR2S_0_21_0_1__REPR__.get(role):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) not in self.MapS2P_0_21_0_1__REPR__.get(s):
                            self.MapS2P_0_21_0_1__REPR__.add(s, (op,obj))
                            
                        
                    
                
            
        for (op,obj,) in self.PRMapR2P_0_20_0_1__REPR__.get(role):
            for u in self.URMapR2U.get(role):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) not in self.MapU2P_0_20_0_1__REPR__.get(u):
                            self.MapU2P_0_20_0_1__REPR__.add(u, (op,obj))
                            
                        
                    
                
            
        for s in self.SRMapR2S_0_13_0_1__REPR__.get(role):
            if role not in self.MapS2R_0_13_0_1__REPR__.get(s):
                self.MapS2R_0_13_0_1__REPR__.add(s, role)
                
            
        for u in self.URMapR2U.get(role):
            if role not in self.MapU2R_0_12_0_1__REPR__.get(u):
                self.MapU2R_0_12_0_1__REPR__.add(u, role)
                
            
        for s in self.SRMapR2S.get(role):
            for (op,obj,) in self.PRMapR2P.get(role):
                if role not in self.MapSP2R.get((s,op,obj)):
                    self.MapSP2R.add((s,op,obj), role)
                    
                
            
        for s_0_0_0_1__REPR__ in self.MapR2S_0_0_0_1__REPR__[role]:
            self.Y_0_0_0_1__REPR__.add(s_0_0_0_1__REPR__, role)
            if role in self.Y_0_0_0_1__REPR__[s_0_0_0_1__REPR__]:
                for name_0_0_0_1__REPR__ in self.MapR2N_0_0_0_1__REPR__[role]:
                    self.X_0_0_0_1__REPR__.add((s_0_0_0_1__REPR__,name_0_0_0_1__REPR__), role)
                    if s_0_0_0_1__REPR__ in self.SESSIONS:
                        for c_0_0_0_1__REPR__ in self.MapN2C_0_0_0_1__REPR__[name_0_0_0_1__REPR__]:
                            if len(self.X_0_0_0_1__REPR__.get(s_0_0_0_1__REPR__, name_0_0_0_1__REPR__)) > c_0_0_0_1__REPR__:
                                self.V_0_0_0_1__REPR__.add(s_0_0_0_1__REPR__)
                                
                            
                        
                    
                
            
        for u_0_3_0_1__REPR__ in self.MapR2U_0_3_0_1__REPR__[role]:
            self.Y_0_3_0_1__REPR__.add(u_0_3_0_1__REPR__, role)
            if role in self.Y_0_3_0_1__REPR__[u_0_3_0_1__REPR__]:
                for name_0_3_0_1__REPR__ in self.MapR2N_0_3_0_1__REPR__[role]:
                    self.X_0_3_0_1__REPR__.add((u_0_3_0_1__REPR__,name_0_3_0_1__REPR__), role)
                    if u_0_3_0_1__REPR__ in self.USERS:
                        for c_0_3_0_1__REPR__ in self.MapN2C_0_3_0_1__REPR__[name_0_3_0_1__REPR__]:
                            if len(self.X_0_3_0_1__REPR__.get(u_0_3_0_1__REPR__, name_0_3_0_1__REPR__)) > c_0_3_0_1__REPR__:
                                self.V_0_3_0_1__REPR__.add(u_0_3_0_1__REPR__)
                                
                            
                        
                    
                
            
        
    def DeleteRole(self, role):
        assert role in self.ROLES
        for u_0_3_0_1__REPR__ in self.MapR2U_0_3_0_1__REPR__[role]:
            if role in self.Y_0_3_0_1__REPR__[u_0_3_0_1__REPR__]:
                for name_0_3_0_1__REPR__ in self.MapR2N_0_3_0_1__REPR__[role]:
                    if u_0_3_0_1__REPR__ in self.USERS:
                        for c_0_3_0_1__REPR__ in self.MapN2C_0_3_0_1__REPR__[name_0_3_0_1__REPR__]:
                            if len(self.X_0_3_0_1__REPR__.get(u_0_3_0_1__REPR__, name_0_3_0_1__REPR__)) > c:
                                self.V_0_3_0_1__REPR__.remove(u_0_3_0_1__REPR__)
                                
                            
                        
                    self.X_0_3_0_1__REPR__.remove((u_0_3_0_1__REPR__,name_0_3_0_1__REPR__), role)
                    
                
            self.Y_0_3_0_1__REPR__.remove(u_0_3_0_1__REPR__, role)
            
        del self.MapR2U_0_3_0_1__REPR__.dct[role]
        for s_0_0_0_1__REPR__ in self.MapR2S_0_0_0_1__REPR__[role]:
            if role in self.Y_0_0_0_1__REPR__[s_0_0_0_1__REPR__]:
                for name_0_0_0_1__REPR__ in self.MapR2N_0_0_0_1__REPR__[role]:
                    if s_0_0_0_1__REPR__ in self.SESSIONS:
                        for c_0_0_0_1__REPR__ in self.MapN2C_0_0_0_1__REPR__[name_0_0_0_1__REPR__]:
                            if len(self.X_0_0_0_1__REPR__.get(s_0_0_0_1__REPR__, name_0_0_0_1__REPR__)) > c:
                                self.V_0_0_0_1__REPR__.remove(s_0_0_0_1__REPR__)
                                
                            
                        
                    self.X_0_0_0_1__REPR__.remove((s_0_0_0_1__REPR__,name_0_0_0_1__REPR__), role)
                    
                
            self.Y_0_0_0_1__REPR__.remove(s_0_0_0_1__REPR__, role)
            
        del self.MapR2S_0_0_0_1__REPR__.dct[role]
        for s in self.SRMapR2S.get(role):
            for (op,obj,) in self.PRMapR2P.get(role):
                if role in self.MapSP2R.get((s,op,obj)):
                    self.MapSP2R.remove((s,op,obj), role)
                    
                
            
        for u in self.URMapR2U.get(role):
            if role in self.MapU2R_0_12_0_1__REPR__.get(u):
                self.MapU2R_0_12_0_1__REPR__.remove(u, role)
                
            
        for s in self.SRMapR2S_0_13_0_1__REPR__.get(role):
            if role in self.MapS2R_0_13_0_1__REPR__.get(s):
                self.MapS2R_0_13_0_1__REPR__.remove(s, role)
                
            
        for (op,obj,) in self.PRMapR2P_0_20_0_1__REPR__.get(role):
            for u in self.URMapR2U.get(role):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) in self.MapU2P_0_20_0_1__REPR__.get(u):
                            self.MapU2P_0_20_0_1__REPR__.remove(u, (op,obj))
                            
                        
                    
                
            
        for (op,obj,) in self.PRMapR2P_0_21_0_1__REPR__.get(role):
            for s in self.SRMapR2S_0_21_0_1__REPR__.get(role):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) in self.MapS2P_0_21_0_1__REPR__.get(s):
                            self.MapS2P_0_21_0_1__REPR__.remove(s, (op,obj))
                            
                        
                    
                
            
        self.ROLES.remove(role)
        for u in self.URMapR2U.get(role):
            for (op,object,) in self.PRMapR2P_0_22_0_1__REPR__.get(role):
                if role in self.ROLES:
                    if op in self.OPS:
                        if op in self.MapUO2A_0_22_0_1__REPR__.get((u,object)):
                            self.MapUO2A_0_22_0_1__REPR__.remove((u,object), op)
                            
                        
                    
                
            
        self.PR -= set((((op,obj),role) for op in self.OPS for obj in self.OBJS))
        self.UR -= set(((u,role) for u in self.USERS))
        for (s,u,) in self.MapR2SU_0_19_0_1__REPR__.get(role):
            self.DeleteSession(u, s)
            
        
    def DeassignUser(self, user, role):
        assert user in self.USERS
        assert role in self.ROLES
        assert (user,role) in self.UR
        if role in self.ROLES:
            if role in self.Y_0_3_0_1__REPR__[user]:
                for name_0_3_0_1__REPR__ in self.MapR2N_0_3_0_1__REPR__[role]:
                    if user in self.USERS:
                        for c_0_3_0_1__REPR__ in self.MapN2C_0_3_0_1__REPR__[name_0_3_0_1__REPR__]:
                            if len(self.X_0_3_0_1__REPR__[(user,name_0_3_0_1__REPR__)]) > c_0_3_0_1__REPR__:
                                self.V_0_3_0_1__REPR__.remove(user)
                                
                            
                        
                    self.X_0_3_0_1__REPR__.remove((user,name_0_3_0_1__REPR__), role)
                    
                
            self.Y_0_3_0_1__REPR__.remove(user, role)
            
        self.MapR2U_0_3_0_1__REPR__.remove(role, user)
        if role in self.ROLES:
            if role in self.MapU2R_0_12_0_1__REPR__.get(user):
                self.MapU2R_0_12_0_1__REPR__.remove(user, role)
                
            
        self.URMapR2U.remove(role, user)
        for (op,obj,) in self.PRMapR2P_0_20_0_1__REPR__.get(role):
            if op in self.OPS:
                if obj in self.OBJS:
                    if (op,obj) in self.MapU2P_0_20_0_1__REPR__.get(user):
                        self.MapU2P_0_20_0_1__REPR__.remove(user, (op,obj))
                        
                    
                
            
        self.URMapR2U.remove(role, user)
        for (op,object,) in self.PRMapR2P_0_22_0_1__REPR__.get(role):
            if role in self.ROLES:
                if op in self.OPS:
                    if op in self.MapUO2A_0_22_0_1__REPR__.get((user,object)):
                        self.MapUO2A_0_22_0_1__REPR__.remove((user,object), op)
                        
                    
                
            
        self.URMapR2U.remove(role, user)
        if user in self.USERS:
            if user in self.MapR2U_0_14_0_1__REPR__.get(role):
                self.MapR2U_0_14_0_1__REPR__.remove(role, user)
                
            
        self.URMapU2R_0_14_0_1__REPR__.remove(user, role)
        self.UR.remove((user,role))
        for s in self.MapUR2S_0_18_0_1__REPR__.get((user,role)):
            self.DeleteSession(user, s)
            
        
    def GrantPermission(self, operation, object, role):
        assert (operation in self.OPS and object in self.OBJS)
        assert role in self.ROLES
        assert ((operation,object),role) not in self.PR
        self.PR.add(((operation,object),role))
        for u in self.URMapR2U.get(role):
            if (operation,object) in self.PRMapR2P_0_22_0_1__REPR__.get(role):
                if role in self.ROLES:
                    if operation in self.OPS:
                        if operation not in self.MapUO2A_0_22_0_1__REPR__.get((u,object)):
                            self.MapUO2A_0_22_0_1__REPR__.add((u,object), operation)
                            
                        
                    
                
            
        self.PRMapR2P_0_22_0_1__REPR__.add(role, (operation,object))
        if role in self.ROLES:
            for s in self.SRMapR2S_0_21_0_1__REPR__.get(role):
                if operation in self.OPS:
                    if object in self.OBJS:
                        if (operation,object) not in self.MapS2P_0_21_0_1__REPR__.get(s):
                            self.MapS2P_0_21_0_1__REPR__.add(s, (operation,object))
                            
                        
                    
                
            self.PRMapR2P_0_21_0_1__REPR__.add(role, (operation,object))
            
        for u in self.URMapR2U.get(role):
            if operation in self.OPS:
                if object in self.OBJS:
                    if (operation,object) not in self.MapU2P_0_20_0_1__REPR__.get(u):
                        self.MapU2P_0_20_0_1__REPR__.add(u, (operation,object))
                        
                    
                
            
        self.PRMapR2P_0_20_0_1__REPR__.add(role, (operation,object))
        if operation in self.OPS:
            if operation not in self.MapRO2A_0_16_0_1__REPR__.get((role,object)):
                self.MapRO2A_0_16_0_1__REPR__.add((role,object), operation)
                
            
        if operation in self.OPS:
            if object in self.OBJS:
                if (operation,object) not in self.MapR2P_0_15_0_1__REPR__.get(role):
                    self.MapR2P_0_15_0_1__REPR__.add(role, (operation,object))
                    
                
            
        if role in self.ROLES:
            for s in self.SRMapR2S.get(role):
                if role not in self.MapSP2R.get((s,operation,object)):
                    self.MapSP2R.add((s,operation,object), role)
                    
                
            
        self.PRMapR2P.add(role, (operation,object))
        
    def RevokePermission(self, operation, object, role):
        assert (operation in self.OPS and object in self.OBJS)
        assert role in self.ROLES
        assert ((operation,object),role) in self.PR
        if role in self.ROLES:
            for s in self.SRMapR2S.get(role):
                if role in self.MapSP2R.get((s,operation,object)):
                    self.MapSP2R.add((s,operation,object), role)
                    
                
            
        self.PRMapR2P.remove(role, (operation,object))
        if operation in self.OPS:
            if object in self.OBJS:
                if (operation,object) in self.MapR2P_0_15_0_1__REPR__.get(role):
                    self.MapR2P_0_15_0_1__REPR__.remove(role, (operation,object))
                    
                
            
        if operation in self.OPS:
            if operation in self.MapRO2A_0_16_0_1__REPR__.get((role,object)):
                self.MapRO2A_0_16_0_1__REPR__.remove((role,object), operation)
                
            
        for u in self.URMapR2U.get(role):
            if operation in self.OPS:
                if object in self.OBJS:
                    if (operation,object) in self.MapU2P_0_20_0_1__REPR__.get(u):
                        self.MapU2P_0_20_0_1__REPR__.remove(u, (operation,object))
                        
                    
                
            
        self.PRMapR2P_0_20_0_1__REPR__.remove(role, (operation,object))
        if role in self.ROLES:
            for s in self.SRMapR2S_0_21_0_1__REPR__.get(role):
                if operation in self.OPS:
                    if object in self.OBJS:
                        if (operation,object) in self.MapS2P_0_21_0_1__REPR__.get(s):
                            self.MapS2P_0_21_0_1__REPR__.remove(s, (operation,object))
                            
                        
                    
                
            self.PRMapR2P_0_21_0_1__REPR__.remove(role, (operation,object))
            
        for u in self.URMapR2U.get(role):
            if (operation,object) in self.PRMapR2P_0_22_0_1__REPR__.get(role):
                if role in self.ROLES:
                    if operation in self.OPS:
                        if operation in self.MapUO2A_0_22_0_1__REPR__.get((u,object)):
                            self.MapUO2A_0_22_0_1__REPR__.remove((u,object), operation)
                            
                        
                    
                
            
        self.PRMapR2P_0_22_0_1__REPR__.remove(role, (operation,object))
        self.PR.remove(((operation,object),role))
        
    def CreateSession(self, user, session, ars):
        added = set() 
        for role in ars:
            if (session,role) not in self.SR:
                self.SR.add((session,role))
                for (op,obj,) in self.PRMapR2P_0_21_0_1__REPR__.get(role):
                    if op in self.OPS:
                        if obj in self.OBJS:
                            if (op,obj) not in self.MapS2P_0_21_0_1__REPR__.get(session):
                                self.MapS2P_0_21_0_1__REPR__.add(session, (op,obj))
                                
                            
                        
                    
                self.SRMapR2S_0_21_0_1__REPR__.add(role, session)
                for u in self.SUMapS2U_0_19_0_1__REPR__.get(session):
                    if session in self.SESSIONS:
                        if u in self.USERS:
                            if (session,u) not in self.MapR2SU_0_19_0_1__REPR__.get(role):
                                self.MapR2SU_0_19_0_1__REPR__.add(role, (session,u))
                                
                            
                        
                    
                for u in self.SUMapS2U_0_18_0_1__REPR__.get(session):
                    if session not in self.MapUR2S_0_18_0_1__REPR__.get((u,role)):
                        self.MapUR2S_0_18_0_1__REPR__.add((u,role), session)
                        
                    
                self.SRMapS2R.add(session, role)
                if role not in self.MapS2R_0_13_0_1__REPR__.get(session):
                    self.MapS2R_0_13_0_1__REPR__.add(session, role)
                    
                self.SRMapR2S_0_13_0_1__REPR__.add(role, session)
                if role in self.ROLES:
                    for (op,obj,) in self.PRMapR2P.get(role):
                        if role not in self.MapSP2R.get((session,op,obj)):
                            self.MapSP2R.add((session,op,obj), role)
                            
                        
                    
                self.SRMapR2S.add(role, session)
                if role in self.ROLES:
                    self.Y_0_0_0_1__REPR__.add(session, role)
                    if role in self.Y_0_0_0_1__REPR__[session]:
                        for name_0_0_0_1__REPR__ in self.MapR2N_0_0_0_1__REPR__[role]:
                            self.X_0_0_0_1__REPR__.add((session,name_0_0_0_1__REPR__), role)
                            if session in self.SESSIONS:
                                for c_0_0_0_1__REPR__ in self.MapN2C_0_0_0_1__REPR__[name_0_0_0_1__REPR__]:
                                    if len(self.X_0_0_0_1__REPR__[(session,name_0_0_0_1__REPR__)]) > c_0_0_0_1__REPR__:
                                        self.V_0_0_0_1__REPR__.add(session)
                                        
                                    
                                
                            
                        
                    
                self.MapR2S_0_0_0_1__REPR__.add(role, session)
                added.add((session,role))
                
            
        good = self.checkDSD() 
        for k in added:
            if k[1] in self.ROLES:
                if k[1] in self.Y_0_0_0_1__REPR__[k[0]]:
                    for name_0_0_0_1__REPR__ in self.MapR2N_0_0_0_1__REPR__[k[1]]:
                        if k[0] in self.SESSIONS:
                            for c_0_0_0_1__REPR__ in self.MapN2C_0_0_0_1__REPR__[name_0_0_0_1__REPR__]:
                                if len(self.X_0_0_0_1__REPR__[(k[0],name_0_0_0_1__REPR__)]) > c_0_0_0_1__REPR__:
                                    self.V_0_0_0_1__REPR__.remove(k[0])
                                    
                                
                            
                        self.X_0_0_0_1__REPR__.remove((k[0],name_0_0_0_1__REPR__), k[1])
                        
                    
                self.Y_0_0_0_1__REPR__.remove(k[0], k[1])
                
            self.MapR2S_0_0_0_1__REPR__.remove(k[1], k[0])
            if k[1] in self.ROLES:
                for (op,obj,) in self.PRMapR2P.get(k[1]):
                    if k[1] in self.MapSP2R.get((k[0],op,obj)):
                        self.MapSP2R.remove((k[0],op,obj), k[1])
                        
                    
                
            self.SRMapR2S.remove(k[1], k[0])
            if k[1] in self.MapS2R_0_13_0_1__REPR__.get(k[0]):
                self.MapS2R_0_13_0_1__REPR__.remove(k[0], k[1])
                
            self.SRMapR2S_0_13_0_1__REPR__.remove(k[1], k[0])
            for u in self.SUMapS2U_0_18_0_1__REPR__.get(k[0]):
                if k[0] in self.MapUR2S_0_18_0_1__REPR__.get((u,k[1])):
                    self.MapUR2S_0_18_0_1__REPR__.remove((u,k[1]), k[0])
                    
                
            self.SRMapS2R.remove(k[0], k[1])
            for u in self.SUMapS2U_0_19_0_1__REPR__.get(k[0]):
                if k[0] in self.SESSIONS:
                    if u in self.USERS:
                        if (k[0],u) in self.MapR2SU_0_19_0_1__REPR__.get(k[1]):
                            self.MapR2SU_0_19_0_1__REPR__.remove(k[1], (k[0],u))
                            
                        
                    
                
            for (op,obj,) in self.PRMapR2P_0_21_0_1__REPR__.get(k[1]):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) in self.MapS2P_0_21_0_1__REPR__.get(k[0]):
                            self.MapS2P_0_21_0_1__REPR__.remove(k[0], (op,obj))
                            
                        
                    
                
            self.SRMapR2S_0_21_0_1__REPR__.remove(k[1], k[0])
            self.SR.remove((k[0],k[1]))
            
        assert good
        assert user in self.USERS
        assert session not in self.SESSIONS
        assert ars.issubset(self.AssignedRoles(user))
        self.SU.add((session,user))
        if session in self.SESSIONS:
            if user in self.USERS:
                for r in self.SRMapS2R.get(session):
                    if (session,user) not in self.MapR2SU_0_19_0_1__REPR__.get(r):
                        self.MapR2SU_0_19_0_1__REPR__.add(r, (session,user))
                        
                    
                
            
        self.SUMapS2U_0_19_0_1__REPR__.add(session, user)
        self.SUMapU2S_0_19_0_1__REPR__.add(user, session)
        for r in self.SRMapS2R.get(session):
            if session not in self.MapUR2S_0_18_0_1__REPR__.get((user,r)):
                self.MapUR2S_0_18_0_1__REPR__.add((user,r), session)
                
            
        self.SUMapS2U_0_18_0_1__REPR__.add(session, user)
        if session in self.SESSIONS:
            if session not in self.MapU2S_0_17_0_1__REPR__.get(user):
                self.MapU2S_0_17_0_1__REPR__.add(user, session)
                
            
        self.SUMapS2U_0_17_0_1__REPR__.add(session, user)
        for r in ars:
            self.SR.add((session,r))
            for (op,obj,) in self.PRMapR2P_0_21_0_1__REPR__.get(r):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) not in self.MapS2P_0_21_0_1__REPR__.get(session):
                            self.MapS2P_0_21_0_1__REPR__.add(session, (op,obj))
                            
                        
                    
                
            self.SRMapR2S_0_21_0_1__REPR__.add(r, session)
            for u in self.SUMapS2U_0_19_0_1__REPR__.get(session):
                if session in self.SESSIONS:
                    if u in self.USERS:
                        if (session,u) not in self.MapR2SU_0_19_0_1__REPR__.get(r):
                            self.MapR2SU_0_19_0_1__REPR__.add(r, (session,u))
                            
                        
                    
                
            for u in self.SUMapS2U_0_18_0_1__REPR__.get(session):
                if session not in self.MapUR2S_0_18_0_1__REPR__.get((u,r)):
                    self.MapUR2S_0_18_0_1__REPR__.add((u,r), session)
                    
                
            self.SRMapS2R.add(session, r)
            if r not in self.MapS2R_0_13_0_1__REPR__.get(session):
                self.MapS2R_0_13_0_1__REPR__.add(session, r)
                
            self.SRMapR2S_0_13_0_1__REPR__.add(r, session)
            if r in self.ROLES:
                for (op,obj,) in self.PRMapR2P.get(r):
                    if r not in self.MapSP2R.get((session,op,obj)):
                        self.MapSP2R.add((session,op,obj), r)
                        
                    
                
            self.SRMapR2S.add(r, session)
            if r in self.ROLES:
                self.Y_0_0_0_1__REPR__.add(session, r)
                if r in self.Y_0_0_0_1__REPR__[session]:
                    for name_0_0_0_1__REPR__ in self.MapR2N_0_0_0_1__REPR__[r]:
                        self.X_0_0_0_1__REPR__.add((session,name_0_0_0_1__REPR__), r)
                        if session in self.SESSIONS:
                            for c_0_0_0_1__REPR__ in self.MapN2C_0_0_0_1__REPR__[name_0_0_0_1__REPR__]:
                                if len(self.X_0_0_0_1__REPR__[(session,name_0_0_0_1__REPR__)]) > c_0_0_0_1__REPR__:
                                    self.V_0_0_0_1__REPR__.add(session)
                                    
                                
                            
                        
                    
                
            self.MapR2S_0_0_0_1__REPR__.add(r, session)
            
        self.SESSIONS.add(session)
        for u in self.SUMapS2U_0_19_0_1__REPR__.get(session):
            if u in self.USERS:
                for r in self.SRMapS2R.get(session):
                    if (session,u) not in self.MapR2SU_0_19_0_1__REPR__.get(r):
                        self.MapR2SU_0_19_0_1__REPR__.add(r, (session,u))
                        
                    
                
            
        for u in self.SUMapS2U_0_18_0_1__REPR__.get(session):
            for r in self.SRMapS2R.get(session):
                if session not in self.MapUR2S_0_18_0_1__REPR__.get((u,r)):
                    self.MapUR2S_0_18_0_1__REPR__.add((u,r), session)
                    
                
            
        for u in self.SUMapS2U_0_17_0_1__REPR__.get(session):
            if session not in self.MapU2S_0_17_0_1__REPR__.get(u):
                self.MapU2S_0_17_0_1__REPR__.add(u, session)
                
            
        for (name_0_0_0_1__REPR__,c_0_0_0_1__REPR__,) in self.DsdNC:
            if len(self.X_0_0_0_1__REPR__[(session,name_0_0_0_1__REPR__)]) > c_0_0_0_1__REPR__:
                self.V_0_0_0_1__REPR__.add(session)
                
            
        
    def AddActiveRole(self, user, session, role):
        added = set() 
        if (session,role) not in self.SR:
            self.SR.add((session,role))
            for (op,obj,) in self.PRMapR2P_0_21_0_1__REPR__.get(role):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) not in self.MapS2P_0_21_0_1__REPR__.get(session):
                            self.MapS2P_0_21_0_1__REPR__.add(session, (op,obj))
                            
                        
                    
                
            self.SRMapR2S_0_21_0_1__REPR__.add(role, session)
            for u in self.SUMapS2U_0_19_0_1__REPR__.get(session):
                if session in self.SESSIONS:
                    if u in self.USERS:
                        if (session,u) not in self.MapR2SU_0_19_0_1__REPR__.get(role):
                            self.MapR2SU_0_19_0_1__REPR__.add(role, (session,u))
                            
                        
                    
                
            for u in self.SUMapS2U_0_18_0_1__REPR__.get(session):
                if session not in self.MapUR2S_0_18_0_1__REPR__.get((u,role)):
                    self.MapUR2S_0_18_0_1__REPR__.add((u,role), session)
                    
                
            self.SRMapS2R.add(session, role)
            if role not in self.MapS2R_0_13_0_1__REPR__.get(session):
                self.MapS2R_0_13_0_1__REPR__.add(session, role)
                
            self.SRMapR2S_0_13_0_1__REPR__.add(role, session)
            if role in self.ROLES:
                for (op,obj,) in self.PRMapR2P.get(role):
                    if role not in self.MapSP2R.get((session,op,obj)):
                        self.MapSP2R.add((session,op,obj), role)
                        
                    
                
            self.SRMapR2S.add(role, session)
            if role in self.ROLES:
                self.Y_0_0_0_1__REPR__.add(session, role)
                if role in self.Y_0_0_0_1__REPR__[session]:
                    for name_0_0_0_1__REPR__ in self.MapR2N_0_0_0_1__REPR__[role]:
                        self.X_0_0_0_1__REPR__.add((session,name_0_0_0_1__REPR__), role)
                        if session in self.SESSIONS:
                            for c_0_0_0_1__REPR__ in self.MapN2C_0_0_0_1__REPR__[name_0_0_0_1__REPR__]:
                                if len(self.X_0_0_0_1__REPR__[(session,name_0_0_0_1__REPR__)]) > c_0_0_0_1__REPR__:
                                    self.V_0_0_0_1__REPR__.add(session)
                                    
                                
                            
                        
                    
                
            self.MapR2S_0_0_0_1__REPR__.add(role, session)
            added.add((session,role))
            
        for (op,obj,) in self.PRMapR2P_0_21_0_1__REPR__.get(role):
            if op in self.OPS:
                if obj in self.OBJS:
                    if (op,obj) not in self.MapS2P_0_21_0_1__REPR__.get(session):
                        self.MapS2P_0_21_0_1__REPR__.add(session, (op,obj))
                        
                    
                
            
        self.SRMapR2S_0_21_0_1__REPR__.add(role, session)
        for u in self.SUMapS2U_0_19_0_1__REPR__.get(session):
            if session in self.SESSIONS:
                if u in self.USERS:
                    if (session,u) not in self.MapR2SU_0_19_0_1__REPR__.get(role):
                        self.MapR2SU_0_19_0_1__REPR__.add(role, (session,u))
                        
                    
                
            
        for u in self.SUMapS2U_0_18_0_1__REPR__.get(session):
            if session not in self.MapUR2S_0_18_0_1__REPR__.get((u,role)):
                self.MapUR2S_0_18_0_1__REPR__.add((u,role), session)
                
            
        self.SRMapS2R.add(session, role)
        if role not in self.MapS2R_0_13_0_1__REPR__.get(session):
            self.MapS2R_0_13_0_1__REPR__.add(session, role)
            
        self.SRMapR2S_0_13_0_1__REPR__.add(role, session)
        if role in self.ROLES:
            for (op,obj,) in self.PRMapR2P.get(role):
                if role not in self.MapSP2R.get((session,op,obj)):
                    self.MapSP2R.add((session,op,obj), role)
                    
                
            
        self.SRMapR2S.add(role, session)
        if role in self.ROLES:
            self.Y_0_0_0_1__REPR__.add(session, role)
            if role in self.Y_0_0_0_1__REPR__[session]:
                for name_0_0_0_1__REPR__ in self.MapR2N_0_0_0_1__REPR__[role]:
                    self.X_0_0_0_1__REPR__.add((session,name_0_0_0_1__REPR__), role)
                    if session in self.SESSIONS:
                        for c_0_0_0_1__REPR__ in self.MapN2C_0_0_0_1__REPR__[name_0_0_0_1__REPR__]:
                            if len(self.X_0_0_0_1__REPR__[(session,name_0_0_0_1__REPR__)]) > c_0_0_0_1__REPR__:
                                self.V_0_0_0_1__REPR__.add(session)
                                
                            
                        
                    
                
            
        self.MapR2S_0_0_0_1__REPR__.add(role, session)
        good = self.CheckDSD() 
        for k in added:
            if k[1] in self.ROLES:
                if k[1] in self.Y_0_0_0_1__REPR__[k[0]]:
                    for name_0_0_0_1__REPR__ in self.MapR2N_0_0_0_1__REPR__[k[1]]:
                        if k[0] in self.SESSIONS:
                            for c_0_0_0_1__REPR__ in self.MapN2C_0_0_0_1__REPR__[name_0_0_0_1__REPR__]:
                                if len(self.X_0_0_0_1__REPR__[(k[0],name_0_0_0_1__REPR__)]) > c_0_0_0_1__REPR__:
                                    self.V_0_0_0_1__REPR__.remove(k[0])
                                    
                                
                            
                        self.X_0_0_0_1__REPR__.remove((k[0],name_0_0_0_1__REPR__), k[1])
                        
                    
                self.Y_0_0_0_1__REPR__.remove(k[0], k[1])
                
            self.MapR2S_0_0_0_1__REPR__.remove(k[1], k[0])
            if k[1] in self.ROLES:
                for (op,obj,) in self.PRMapR2P.get(k[1]):
                    if k[1] in self.MapSP2R.get((k[0],op,obj)):
                        self.MapSP2R.remove((k[0],op,obj), k[1])
                        
                    
                
            self.SRMapR2S.remove(k[1], k[0])
            if k[1] in self.MapS2R_0_13_0_1__REPR__.get(k[0]):
                self.MapS2R_0_13_0_1__REPR__.remove(k[0], k[1])
                
            self.SRMapR2S_0_13_0_1__REPR__.remove(k[1], k[0])
            for u in self.SUMapS2U_0_18_0_1__REPR__.get(k[0]):
                if k[0] in self.MapUR2S_0_18_0_1__REPR__.get((u,k[1])):
                    self.MapUR2S_0_18_0_1__REPR__.remove((u,k[1]), k[0])
                    
                
            self.SRMapS2R.remove(k[0], k[1])
            for u in self.SUMapS2U_0_19_0_1__REPR__.get(k[0]):
                if k[0] in self.SESSIONS:
                    if u in self.USERS:
                        if (k[0],u) in self.MapR2SU_0_19_0_1__REPR__.get(k[1]):
                            self.MapR2SU_0_19_0_1__REPR__.remove(k[1], (k[0],u))
                            
                        
                    
                
            for (op,obj,) in self.PRMapR2P_0_21_0_1__REPR__.get(k[1]):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) in self.MapS2P_0_21_0_1__REPR__.get(k[0]):
                            self.MapS2P_0_21_0_1__REPR__.remove(k[0], (op,obj))
                            
                        
                    
                
            self.SRMapR2S_0_21_0_1__REPR__.remove(k[1], k[0])
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
        if session in self.SESSIONS:
            if session in self.MapU2S_0_17_0_1__REPR__.get(user):
                self.MapU2S_0_17_0_1__REPR__.remove(user, session)
                
            
        self.SUMapS2U_0_17_0_1__REPR__.remove(session, user)
        for r in self.SRMapS2R.get(session):
            if session in self.MapUR2S_0_18_0_1__REPR__.get((user,r)):
                self.MapUR2S_0_18_0_1__REPR__.remove((user,r), session)
                
            
        self.SUMapS2U_0_18_0_1__REPR__.remove(session, user)
        if session in self.SESSIONS:
            if user in self.USERS:
                for r in self.SRMapS2R.get(session):
                    if (session,user) in self.MapR2SU_0_19_0_1__REPR__.get(r):
                        self.MapR2SU_0_19_0_1__REPR__.remove(r, (session,user))
                        
                    
                
            
        self.SUMapS2U_0_19_0_1__REPR__.remove(session, user)
        self.SUMapU2S_0_19_0_1__REPR__.remove(user, session)
        self.SU.remove((session,user))
        self.SR -= set(((session,r) for r in self.ROLES))
        for (name_0_0_0_1__REPR__,c_0_0_0_1__REPR__,) in self.DsdNC:
            if len(self.X_0_0_0_1__REPR__[(session,name_0_0_0_1__REPR__)]) > c_0_0_0_1__REPR__:
                self.V_0_0_0_1__REPR__.remove(session)
                
            
        for (k,v,) in self.MapR2S_0_0_0_1__REPR__.dct.iteritems:
            v.remove(session)
            
        for u in self.SUMapS2U_0_17_0_1__REPR__.get(session):
            if session in self.MapU2S_0_17_0_1__REPR__.get(u):
                self.MapU2S_0_17_0_1__REPR__.remove(u, session)
                
            
        for u in self.SUMapS2U_0_18_0_1__REPR__.get(session):
            for r in self.SRMapS2R.get(session):
                if session in self.MapUR2S_0_18_0_1__REPR__.get((u,r)):
                    self.MapUR2S_0_18_0_1__REPR__.remove((u,r), session)
                    
                
            
        for u in self.SUMapS2U_0_19_0_1__REPR__.get(session):
            if u in self.USERS:
                for r in self.SRMapS2R.get(session):
                    if (session,u) in self.MapR2SU_0_19_0_1__REPR__.get(r):
                        self.MapR2SU_0_19_0_1__REPR__.remove(r, (session,u))
                        
                    
                
            
        self.SESSIONS.remove(session)
        
    def DropActiveRole(self, user, session, role):
        assert user in self.USERS
        assert session in self.SESSIONS
        assert role in self.ROLES
        assert (session,user) in self.SU
        assert (session,role) in self.SR
        if role in self.ROLES:
            if role in self.Y_0_0_0_1__REPR__[session]:
                for name_0_0_0_1__REPR__ in self.MapR2N_0_0_0_1__REPR__[role]:
                    if session in self.SESSIONS:
                        for c_0_0_0_1__REPR__ in self.MapN2C_0_0_0_1__REPR__[name_0_0_0_1__REPR__]:
                            if len(self.X_0_0_0_1__REPR__[(session,name_0_0_0_1__REPR__)]) > c_0_0_0_1__REPR__:
                                self.V_0_0_0_1__REPR__.remove(session)
                                
                            
                        
                    self.X_0_0_0_1__REPR__.remove((session,name_0_0_0_1__REPR__), role)
                    
                
            self.Y_0_0_0_1__REPR__.remove(session, role)
            
        self.MapR2S_0_0_0_1__REPR__.remove(role, session)
        if role in self.ROLES:
            for (op,obj,) in self.PRMapR2P.get(role):
                if role in self.MapSP2R.get((session,op,obj)):
                    self.MapSP2R.remove((session,op,obj), role)
                    
                
            
        self.SRMapR2S.remove(role, session)
        if role in self.MapS2R_0_13_0_1__REPR__.get(session):
            self.MapS2R_0_13_0_1__REPR__.remove(session, role)
            
        self.SRMapR2S_0_13_0_1__REPR__.remove(role, session)
        for u in self.SUMapS2U_0_18_0_1__REPR__.get(session):
            if session in self.MapUR2S_0_18_0_1__REPR__.get((u,role)):
                self.MapUR2S_0_18_0_1__REPR__.remove((u,role), session)
                
            
        self.SRMapS2R.remove(session, role)
        for u in self.SUMapS2U_0_19_0_1__REPR__.get(session):
            if session in self.SESSIONS:
                if u in self.USERS:
                    if (session,u) in self.MapR2SU_0_19_0_1__REPR__.get(role):
                        self.MapR2SU_0_19_0_1__REPR__.remove(role, (session,u))
                        
                    
                
            
        for (op,obj,) in self.PRMapR2P_0_21_0_1__REPR__.get(role):
            if op in self.OPS:
                if obj in self.OBJS:
                    if (op,obj) in self.MapS2P_0_21_0_1__REPR__.get(session):
                        self.MapS2P_0_21_0_1__REPR__.remove(session, (op,obj))
                        
                    
                
            
        self.SRMapR2S_0_21_0_1__REPR__.remove(role, session)
        self.SR.remove((session,role))
        
    def CheckAccess(self, session, operation, object):
        assert session in self.SESSIONS
        assert operation in self.OPS
        assert object in self.OBJS
        return bool(self.MapSP2R.get((session,operation,object)))
    def AssignedUsers(self, role):
        assert role in self.ROLES
        return self.MapR2U_0_14_0_1__REPR__.get(role)
    def AssignedRoles(self, user):
        assert user in self.USERS
        return self.MapU2R_0_12_0_1__REPR__.get(user)
    def RolePermissions(self, role):
        assert role in self.ROLES
        return self.MapR2P_0_15_0_1__REPR__.get(role)
    def UserPermissions(self, user):
        assert user in self.USERS
        return self.MapU2P_0_20_0_1__REPR__.get(user)
    def SessionRoles(self, session):
        assert session in self.SESSIONS
        return self.MapS2R_0_13_0_1__REPR__.get(session)
    def SessionPermissions(self, session):
        assert session in self.SESSIONS
        return self.MapS2P_0_21_0_1__REPR__.get(session)
    def RoleOperationsOnObject(self, role, obj):
        assert role in self.ROLES
        assert obj in self.OBJS
        return self.MapRO2A_0_16_0_1__REPR__.get((role,object))
    def UserOperationsOnObject(self, user, object):
        assert user in self.USERS
        assert object in self.OBJS
        return self.MapUO2A_0_22_0_1__REPR__.get((user,object))
    def AddOperation(self, operation):
        self.OPS.add(operation)
        
    def AddObject(self, OBJ):
        self.OBJS.add(OBJ)
        
    def AddPermission(self, operation, obj):
        pass 
    def checkSSD(self):
        return ( not bool(self.V_0_3_0_1__REPR__))
    def AssignUser(self, user, role):
        assert user in self.USERS
        assert role in self.ROLES
        assert (user,role) not in self.UR
        self.UR.add((user,role))
        if user in self.USERS:
            if user not in self.MapR2U_0_14_0_1__REPR__.get(role):
                self.MapR2U_0_14_0_1__REPR__.add(role, user)
                
            
        self.URMapU2R_0_14_0_1__REPR__.add(user, role)
        for (op,object,) in self.PRMapR2P_0_22_0_1__REPR__.get(role):
            if role in self.ROLES:
                if op in self.OPS:
                    if op not in self.MapUO2A_0_22_0_1__REPR__.get((user,object)):
                        self.MapUO2A_0_22_0_1__REPR__.add((user,object), op)
                        
                    
                
            
        self.URMapR2U.add(role, user)
        for (op,obj,) in self.PRMapR2P_0_20_0_1__REPR__.get(role):
            if op in self.OPS:
                if obj in self.OBJS:
                    if (op,obj) not in self.MapU2P_0_20_0_1__REPR__.get(user):
                        self.MapU2P_0_20_0_1__REPR__.add(user, (op,obj))
                        
                    
                
            
        self.URMapR2U.add(role, user)
        if role in self.ROLES:
            if role not in self.MapU2R_0_12_0_1__REPR__.get(user):
                self.MapU2R_0_12_0_1__REPR__.add(user, role)
                
            
        self.URMapR2U.add(role, user)
        if role in self.ROLES:
            self.Y_0_3_0_1__REPR__.add(user, role)
            if role in self.Y_0_3_0_1__REPR__[user]:
                for name_0_3_0_1__REPR__ in self.MapR2N_0_3_0_1__REPR__[role]:
                    self.X_0_3_0_1__REPR__.add((user,name_0_3_0_1__REPR__), role)
                    if user in self.USERS:
                        for c_0_3_0_1__REPR__ in self.MapN2C_0_3_0_1__REPR__[name_0_3_0_1__REPR__]:
                            if len(self.X_0_3_0_1__REPR__[(user,name_0_3_0_1__REPR__)]) > c_0_3_0_1__REPR__:
                                self.V_0_3_0_1__REPR__.add(user)
                                
                            
                        
                    
                
            
        self.MapR2U_0_3_0_1__REPR__.add(role, user)
        good = self.checkSSD() 
        if ( not good):
            if r in self.ROLES:
                if r in self.Y_0_3_0_1__REPR__[u]:
                    for name_0_3_0_1__REPR__ in self.MapR2N_0_3_0_1__REPR__[r]:
                        if u in self.USERS:
                            for c_0_3_0_1__REPR__ in self.MapN2C_0_3_0_1__REPR__[name_0_3_0_1__REPR__]:
                                if len(self.X_0_3_0_1__REPR__[(u,name_0_3_0_1__REPR__)]) > c_0_3_0_1__REPR__:
                                    self.V_0_3_0_1__REPR__.remove(u)
                                    
                                
                            
                        self.X_0_3_0_1__REPR__.remove((u,name_0_3_0_1__REPR__), r)
                        
                    
                self.Y_0_3_0_1__REPR__.remove(u, r)
                
            self.MapR2U_0_3_0_1__REPR__.remove(r, u)
            if r in self.ROLES:
                if r in self.MapU2R_0_12_0_1__REPR__.get(u):
                    self.MapU2R_0_12_0_1__REPR__.remove(u, r)
                    
                
            self.URMapR2U.remove(r, u)
            for (op,obj,) in self.PRMapR2P_0_20_0_1__REPR__.get(r):
                if op in self.OPS:
                    if obj in self.OBJS:
                        if (op,obj) in self.MapU2P_0_20_0_1__REPR__.get(u):
                            self.MapU2P_0_20_0_1__REPR__.remove(u, (op,obj))
                            
                        
                    
                
            self.URMapR2U.remove(r, u)
            for (op,object,) in self.PRMapR2P_0_22_0_1__REPR__.get(r):
                if r in self.ROLES:
                    if op in self.OPS:
                        if op in self.MapUO2A_0_22_0_1__REPR__.get((u,object)):
                            self.MapUO2A_0_22_0_1__REPR__.remove((u,object), op)
                            
                        
                    
                
            self.URMapR2U.remove(r, u)
            if u in self.USERS:
                if u in self.MapR2U_0_14_0_1__REPR__.get(r):
                    self.MapR2U_0_14_0_1__REPR__.remove(r, u)
                    
                
            self.URMapU2R_0_14_0_1__REPR__.remove(u, r)
            self.UR.remove((u,r))
            
        assert good
        
    def CreateSsdSet(self, name, roles, c):
        assert name not in self.SsdNAMES
        assert roles.issubset(self.ROLES)
        assert 1 <= c <= (len(roles) - 1)
        AddedSsdNR = set() 
        for r in roles:
            if (name,r) not in self.SsdNR:
                AddedSsdNR.add((name,r))
                self.SsdNR.add((name,r))
                self.MapN2R_0_9_0_1__REPR__.add((name,r)[0], (name,r)[1])
                if r in self.ROLES:
                    if (name,r) in self.SsdNR:
                        self.X_0_3_0_1__REPR__.add((u_0_3_0_1__REPR__,name), r)
                        for u_0_3_0_1__REPR__ in self.USERS:
                            for c_0_3_0_1__REPR__ in self.MapN2C_0_3_0_1__REPR__[name]:
                                if len(self.X_0_3_0_1__REPR__[(u_0_3_0_1__REPR__,name)]) > c_0_3_0_1__REPR__:
                                    self.V_0_3_0_1__REPR__.add(u_0_3_0_1__REPR__)
                                    
                                
                            
                        
                    
                self.MapR2N_0_3_0_1__REPR__.add((name,r))
                
            
        AddedSsdNC = set() 
        if (name,c) not in self.SsdNC:
            AddedSsdNC.add((name,c))
            self.MapN2C_0_10_0_1__REPR__.add((name,c)[0], (name,c)[1])
            self.SsdNC.add((name,c))
            name_0_3_0_1__REPR__ = (name,c)[0] 
            c_0_3_0_1__REPR__ = (name,c)[1] 
            for u_0_3_0_1__REPR__ in self.USERS:
                if len(self.X_0_3_0_1__REPR__[(u_0_3_0_1__REPR__,name_0_3_0_1__REPR__)]) > c:
                    self.V_0_3_0_1__REPR__.add(u_0_3_0_1__REPR__)
                    
                
            self.MapN2C_0_3_0_1__REPR__.add((name_0_3_0_1__REPR__,c_0_3_0_1__REPR__))
            
        name_0_3_0_1__REPR__ = (name,c)[0] 
        c_0_3_0_1__REPR__ = (name,c)[1] 
        for u_0_3_0_1__REPR__ in self.USERS:
            if len(self.X_0_3_0_1__REPR__[(u_0_3_0_1__REPR__,name_0_3_0_1__REPR__)]) > c:
                self.V_0_3_0_1__REPR__.add(u_0_3_0_1__REPR__)
                
            
        self.MapN2C_0_3_0_1__REPR__.add((name_0_3_0_1__REPR__,c_0_3_0_1__REPR__))
        good = self.checkSSD() 
        if ( not good):
            for (name,r,) in AddedSsdNR:
                if r in self.ROLES:
                    if (name,r) in self.SsdNR:
                        for u_0_3_0_1__REPR__ in self.USERS:
                            for c_0_3_0_1__REPR__ in self.MapN2C_0_3_0_1__REPR__[name]:
                                if len(self.X_0_3_0_1__REPR__[(u_0_3_0_1__REPR__,name)]) > c_0_3_0_1__REPR__:
                                    self.V_0_3_0_1__REPR__.remove(u_0_3_0_1__REPR__)
                                    
                                
                            
                        self.X_0_3_0_1__REPR__.remove((u_0_3_0_1__REPR__,name), r)
                        
                    
                self.MapR2N_0_3_0_1__REPR__.remove((name,r))
                self.SsdNR.remove((name,r))
                self.MapN2R_0_9_0_1__REPR__.remove((name,r)[0], (name,r)[1])
                
            for (name,c,) in AddedSsdNC:
                name_0_3_0_1__REPR__ = (name,c)[0] 
                c_0_3_0_1__REPR__ = (name,c)[1] 
                for u_0_3_0_1__REPR__ in self.USERS:
                    if len(self.X_0_3_0_1__REPR__[(u_0_3_0_1__REPR__,name_0_3_0_1__REPR__)]) > c:
                        self.V_0_3_0_1__REPR__.remove(u_0_3_0_1__REPR__)
                        
                    
                self.MapN2C_0_3_0_1__REPR__.remove((name_0_3_0_1__REPR__,c_0_3_0_1__REPR__))
                self.MapN2C_0_10_0_1__REPR__.remove((name,c)[0], (name,c)[1])
                self.SsdNC.remove((name,c))
                
            
        assert good
        self.MapN2C_0_10_0_1__REPR__.add((name,c)[0], (name,c)[1])
        self.SsdNC.add((name,c))
        
    def DeleteSsdSet(self, name):
        assert name in self.SsdNAMES
        self.SsdNR -= set(((name,r) for r in self.SsdRoleSetRoles(name)))
        name_0_3_0_1__REPR__ = (name,self.SsdRoleSetCardinality(name))[0] 
        c_0_3_0_1__REPR__ = (name,self.SsdRoleSetCardinality(name))[1] 
        for u_0_3_0_1__REPR__ in self.USERS:
            if len(self.X_0_3_0_1__REPR__[(u_0_3_0_1__REPR__,name_0_3_0_1__REPR__)]) > c:
                self.V_0_3_0_1__REPR__.remove(u_0_3_0_1__REPR__)
                
            
        self.MapN2C_0_3_0_1__REPR__.remove((name_0_3_0_1__REPR__,c_0_3_0_1__REPR__))
        self.MapN2C_0_10_0_1__REPR__.remove((name,self.SsdRoleSetCardinality(name))[0], (name,self.SsdRoleSetCardinality(name))[1])
        self.SsdNC.remove((name,self.SsdRoleSetCardinality(name)))
        self.SsdNAMES.remove(name)
        
    def AddSsdRoleMember(self, name, role):
        assert name in self.SsdNAMES
        assert role in self.ROLES
        assert role not in self.SsdRoleSetRoles(name)
        AddedSsdNR = set() 
        if (name,role) not in self.SsdNR:
            AddedSsdNR.add((name,role))
            self.SsdNR.add((name,role))
            self.MapN2R_0_9_0_1__REPR__.add((name,role)[0], (name,role)[1])
            if role in self.ROLES:
                if (name,role) in self.SsdNR:
                    self.X_0_3_0_1__REPR__.add((u_0_3_0_1__REPR__,name), role)
                    for u_0_3_0_1__REPR__ in self.USERS:
                        for c_0_3_0_1__REPR__ in self.MapN2C_0_3_0_1__REPR__[name]:
                            if len(self.X_0_3_0_1__REPR__[(u_0_3_0_1__REPR__,name)]) > c_0_3_0_1__REPR__:
                                self.V_0_3_0_1__REPR__.add(u_0_3_0_1__REPR__)
                                
                            
                        
                    
                
            self.MapR2N_0_3_0_1__REPR__.add((name,role))
            
        good = self.checkSSD() 
        if ( not good):
            for (name,r,) in AddedSsdNR:
                if r in self.ROLES:
                    if (name,r) in self.SsdNR:
                        for u_0_3_0_1__REPR__ in self.USERS:
                            for c_0_3_0_1__REPR__ in self.MapN2C_0_3_0_1__REPR__[name]:
                                if len(self.X_0_3_0_1__REPR__[(u_0_3_0_1__REPR__,name)]) > c_0_3_0_1__REPR__:
                                    self.V_0_3_0_1__REPR__.remove(u_0_3_0_1__REPR__)
                                    
                                
                            
                        self.X_0_3_0_1__REPR__.remove((u_0_3_0_1__REPR__,name), r)
                        
                    
                self.MapR2N_0_3_0_1__REPR__.remove((name,r))
                self.SsdNR.remove((name,r))
                self.MapN2R_0_9_0_1__REPR__.remove((name,r)[0], (name,r)[1])
                
            
        assert good
        
    def DeleteSsdRoleMember(self, name, role):
        assert name in self.SsdNAMES
        assert role in self.SsdRoleSetRoles(name)
        assert self.SsdRoleSetCardinality(name) <= (len(self.SsdRoleSetRoles(name)) - 2)
        if role in self.ROLES:
            if (name,role) in self.SsdNR:
                for u_0_3_0_1__REPR__ in self.USERS:
                    for c_0_3_0_1__REPR__ in self.MapN2C_0_3_0_1__REPR__[name]:
                        if len(self.X_0_3_0_1__REPR__[(u_0_3_0_1__REPR__,name)]) > c_0_3_0_1__REPR__:
                            self.V_0_3_0_1__REPR__.remove(u_0_3_0_1__REPR__)
                            
                        
                    
                self.X_0_3_0_1__REPR__.remove((u_0_3_0_1__REPR__,name), role)
                
            
        self.MapR2N_0_3_0_1__REPR__.remove((name,role))
        self.SsdNR.remove((name,role))
        self.MapN2R_0_9_0_1__REPR__.remove((name,role)[0], (name,role)[1])
        
    def SetSsdSetCardinality(self, name, c):
        assert name in self.SsdNAMES
        assert 1 <= c <= (len(self.SsdRoleSetRoles(name)) - 1)
        NegSsdNC = set() 
        for (name,c,) in set((name,self.SsdRoleSetCardinality(name))):
            if (name,c) in self.SsdNC:
                name_0_3_0_1__REPR__ = (name,c)[0] 
                c_0_3_0_1__REPR__ = (name,c)[1] 
                for u_0_3_0_1__REPR__ in self.USERS:
                    if len(self.X_0_3_0_1__REPR__[(u_0_3_0_1__REPR__,name_0_3_0_1__REPR__)]) > c:
                        self.V_0_3_0_1__REPR__.remove(u_0_3_0_1__REPR__)
                        
                    
                self.MapN2C_0_3_0_1__REPR__.remove((name_0_3_0_1__REPR__,c_0_3_0_1__REPR__))
                self.MapN2C_0_10_0_1__REPR__.remove((name,c)[0], (name,c)[1])
                self.SsdNC.remove((name,c))
                NegSsdNC.add((name,c))
                
            
        PosSsdNC = set() 
        if (name,c) not in self.SsdNC:
            self.MapN2C_0_10_0_1__REPR__.add((name,c)[0], (name,c)[1])
            self.SsdNC.add((name,c))
            name_0_3_0_1__REPR__ = (name,c)[0] 
            c_0_3_0_1__REPR__ = (name,c)[1] 
            for u_0_3_0_1__REPR__ in self.USERS:
                if len(self.X_0_3_0_1__REPR__[(u_0_3_0_1__REPR__,name_0_3_0_1__REPR__)]) > c:
                    self.V_0_3_0_1__REPR__.add(u_0_3_0_1__REPR__)
                    
                
            self.MapN2C_0_3_0_1__REPR__.add((name_0_3_0_1__REPR__,c_0_3_0_1__REPR__))
            PosSsdNC.add((name,c))
            
        good = self.checkSSD() 
        if ( not good):
            for (name,c,) in PosSsdNC:
                name_0_3_0_1__REPR__ = (name,c)[0] 
                c_0_3_0_1__REPR__ = (name,c)[1] 
                for u_0_3_0_1__REPR__ in self.USERS:
                    if len(self.X_0_3_0_1__REPR__[(u_0_3_0_1__REPR__,name_0_3_0_1__REPR__)]) > c:
                        self.V_0_3_0_1__REPR__.remove(u_0_3_0_1__REPR__)
                        
                    
                self.MapN2C_0_3_0_1__REPR__.remove((name_0_3_0_1__REPR__,c_0_3_0_1__REPR__))
                self.MapN2C_0_10_0_1__REPR__.remove((name,c)[0], (name,c)[1])
                self.SsdNC.remove((name,c))
                
            for (name,c,) in NegSsdNC:
                self.MapN2C_0_10_0_1__REPR__.add((name,c)[0], (name,c)[1])
                self.SsdNC.add((name,c))
                name_0_3_0_1__REPR__ = (name,c)[0] 
                c_0_3_0_1__REPR__ = (name,c)[1] 
                for u_0_3_0_1__REPR__ in self.USERS:
                    if len(self.X_0_3_0_1__REPR__[(u_0_3_0_1__REPR__,name_0_3_0_1__REPR__)]) > c:
                        self.V_0_3_0_1__REPR__.add(u_0_3_0_1__REPR__)
                        
                    
                self.MapN2C_0_3_0_1__REPR__.add((name_0_3_0_1__REPR__,c_0_3_0_1__REPR__))
                
            
        assert good
        pass 
    def SsdRoleSets(self):
        return self.SsdNAMES
    def SsdRoleSetRoles(self, name):
        assert name in self.SsdNAMES
        return self.MapN2R_0_9_0_1__REPR__.get(name)
    def SsdRoleSetCardinality(self, name):
        assert name in self.SsdNAMES
        return self.MapN2C_0_10_0_1__REPR__.get(name).pop()
    def checkDSD(self):
        return ( not bool(self.V_0_0_0_1__REPR__))
    def CreateDsdSet(self, name, roles, c):
        assert name not in self.DsdNAMES
        assert roles.issubset(self.ROLES)
        assert 1 <= c <= (len(roles) - 1)
        negDsdNR = set() 
        for r in roles:
            if (name,r) not in self.DsdNR:
                self.DsdNR.add((name,r))
                self.MapN2R_0_1_0_1__REPR__.add((name,r)[0], (name,r)[1])
                if r in self.ROLES:
                    if (name,r) in self.DsdNR:
                        self.X_0_0_0_1__REPR__.add((u_0_0_0_1__REPR__,name), r)
                        for u_0_0_0_1__REPR__ in self.SESSIONS:
                            for c_0_0_0_1__REPR__ in self.MapN2C_0_0_0_1__REPR__[name]:
                                if len(self.X_0_0_0_1__REPR__[(u_0_0_0_1__REPR__,name)]) > c_0_0_0_1__REPR__:
                                    self.V_0_0_0_1__REPR__.add(u_0_0_0_1__REPR__)
                                    
                                
                            
                        
                    
                self.MapR2N_0_0_0_1__REPR__.add((name,r))
                negDsdNR.add((name,r))
                
            
        negDsdNC = set() 
        if (name,c) not in self.DsdNC:
            self.MapN2C_0_2_0_1__REPR__.add((name,c)[0], (name,c)[1])
            self.DsdNC.add((name,c))
            name_0_0_0_1__REPR__ = (name,c)[0] 
            c_0_0_0_1__REPR__ = (name,c)[1] 
            for u_0_0_0_1__REPR__ in self.SESSIONS:
                if len(self.X_0_0_0_1__REPR__[(u_0_0_0_1__REPR__,name_0_0_0_1__REPR__)]) > c:
                    self.V_0_0_0_1__REPR__.add(u_0_0_0_1__REPR__)
                    
                
            self.MapN2C_0_0_0_1__REPR__.add((name_0_0_0_1__REPR__,c_0_0_0_1__REPR__))
            negDsdNC.add((name,c))
            
        assert self.checkDSD()
        self.DsdNAMES.add(name)
        
    def DeleteDsdSet(self, name):
        assert name in self.DsdNAMES
        self.DsdNR -= set(((name,r) for r in self.DsdRoleSetRoles(name)))
        name_0_0_0_1__REPR__ = (name,self.DsdRoleSetCardinality(name))[0] 
        c_0_0_0_1__REPR__ = (name,self.DsdRoleSetCardinality(name))[1] 
        for u_0_0_0_1__REPR__ in self.SESSIONS:
            if len(self.X_0_0_0_1__REPR__[(u_0_0_0_1__REPR__,name_0_0_0_1__REPR__)]) > c:
                self.V_0_0_0_1__REPR__.remove(u_0_0_0_1__REPR__)
                
            
        self.MapN2C_0_0_0_1__REPR__.remove((name_0_0_0_1__REPR__,c_0_0_0_1__REPR__))
        self.MapN2C_0_2_0_1__REPR__.remove((name,self.DsdRoleSetCardinality(name))[0], (name,self.DsdRoleSetCardinality(name))[1])
        self.DsdNC.remove((name,self.DsdRoleSetCardinality(name)))
        self.DsdNAMES.remove(name)
        
    def AddDsdRoleMember(self, name, role):
        assert name in self.DsdNAMES
        assert role in self.ROLES
        assert role not in self.DsdRoleSetRoles(name)
        self.DsdNR.add((name,role))
        self.MapN2R_0_1_0_1__REPR__.add((name,role)[0], (name,role)[1])
        if role in self.ROLES:
            if (name,role) in self.DsdNR:
                self.X_0_0_0_1__REPR__.add((u_0_0_0_1__REPR__,name), role)
                for u_0_0_0_1__REPR__ in self.SESSIONS:
                    for c_0_0_0_1__REPR__ in self.MapN2C_0_0_0_1__REPR__[name]:
                        if len(self.X_0_0_0_1__REPR__[(u_0_0_0_1__REPR__,name)]) > c_0_0_0_1__REPR__:
                            self.V_0_0_0_1__REPR__.add(u_0_0_0_1__REPR__)
                            
                        
                    
                
            
        self.MapR2N_0_0_0_1__REPR__.add((name,role))
        assert self.checkDSD()
        
    def DeleteDsdRoleMember(self, name, role):
        assert name in self.DsdNAMES
        assert role in self.DsdRoleSetRoles(name)
        assert self.DsdRoleSetCardinality(name) <= (len(self.DsdRoleSetRoles(name)) - 2)
        if role in self.ROLES:
            if (name,role) in self.DsdNR:
                for u_0_0_0_1__REPR__ in self.SESSIONS:
                    for c_0_0_0_1__REPR__ in self.MapN2C_0_0_0_1__REPR__[name]:
                        if len(self.X_0_0_0_1__REPR__[(u_0_0_0_1__REPR__,name)]) > c_0_0_0_1__REPR__:
                            self.V_0_0_0_1__REPR__.remove(u_0_0_0_1__REPR__)
                            
                        
                    
                self.X_0_0_0_1__REPR__.remove((u_0_0_0_1__REPR__,name), role)
                
            
        self.MapR2N_0_0_0_1__REPR__.remove((name,role))
        self.DsdNR.remove((name,role))
        self.MapN2R_0_1_0_1__REPR__.remove((name,role)[0], (name,role)[1])
        
    def SetDsdSetCardinality(self, name, c):
        assert name in self.DsdNAMES
        assert 1 <= c <= (len(self.DsdRoleSetRoles(name)) - 1)
        name_0_0_0_1__REPR__ = (name,self.DsdRoleSetCardinality(name))[0] 
        c_0_0_0_1__REPR__ = (name,self.DsdRoleSetCardinality(name))[1] 
        for u_0_0_0_1__REPR__ in self.SESSIONS:
            if len(self.X_0_0_0_1__REPR__[(u_0_0_0_1__REPR__,name_0_0_0_1__REPR__)]) > c:
                self.V_0_0_0_1__REPR__.remove(u_0_0_0_1__REPR__)
                
            
        self.MapN2C_0_0_0_1__REPR__.remove((name_0_0_0_1__REPR__,c_0_0_0_1__REPR__))
        self.MapN2C_0_2_0_1__REPR__.remove((name,self.DsdRoleSetCardinality(name))[0], (name,self.DsdRoleSetCardinality(name))[1])
        self.DsdNC.remove((name,self.DsdRoleSetCardinality(name)))
        self.MapN2C_0_2_0_1__REPR__.add((name,c)[0], (name,c)[1])
        self.DsdNC.add((name,c))
        name_0_0_0_1__REPR__ = (name,c)[0] 
        c_0_0_0_1__REPR__ = (name,c)[1] 
        for u_0_0_0_1__REPR__ in self.SESSIONS:
            if len(self.X_0_0_0_1__REPR__[(u_0_0_0_1__REPR__,name_0_0_0_1__REPR__)]) > c:
                self.V_0_0_0_1__REPR__.add(u_0_0_0_1__REPR__)
                
            
        self.MapN2C_0_0_0_1__REPR__.add((name_0_0_0_1__REPR__,c_0_0_0_1__REPR__))
        assert self.checkDSD()
        
    def DsdRoleSets(self):
        return self.DsdNAMES
    def DsdRoleSetRoles(self, name):
        assert name in self.DsdNAMES
        return self.MapN2R_0_1_0_1__REPR__.get(name)
    def DsdRoleSetCardinality(self, name):
        assert name in self.DsdNAMES
        return self.MapN2C_0_2_0_1__REPR__.get(name).pop()
    
