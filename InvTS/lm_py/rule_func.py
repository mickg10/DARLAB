import re
import pdb
import gc
from ast import *
import pprint
import compiler
import string
import inspect
import os
from sets  import Set
from util import *
from rule import *
from compiler.ast import *
import pdb
def subset (a,b): 
    #dprint a,b
    return True
def is_immutable(a): 
    #dprint gc.get_referrers(a)  #Sanity check to make sure backreferences are availible

    return True
def Print(a):
    print a
    return a
def Class (a): 
    res=ast_of_type(a,compiler.ast.Class)
    dprint(res)
    if res!=None:
        return res.name
    else:
        return res
def Function (a): 
    res=ast_of_type(a,compiler.ast.Function)
    dprint(res)
    if res!=None:
        return res.name
    else:
        return res
def isConst (a):
    dprint (a,isinstance(a,Const))
    return isinstance(a,Const)
def isDefined (a):
    return True
def isType(a,t):
    dprint (a,t,isinstance(a,t))
    return isinstance(a,t)
def Type (a):
    dprint (a)
    return True
def FALSE (a):
    dprint (a)
    return False
def isVar(a):
    dprint (a,isinstance(a,Name))
    return isinstance(a,Name) 
def isVar2(x,a):
    #print (a,isinstance(a,Name))
    #print hasattr(a, "_contexts")
    pdb.set_trace()
    return True

def find_class(program,name):
    res= ast_find_class(program,name)
    if res:
        res=res[0]
    return res

def find_member_function(class_ast,name):
    fun=None
    funs=ast_find_function(class_ast,name)
    if funs:
        fun=funs[0]
    return fun

def find_function(program,name):
    funs=ast_find_function(program,name)
    fun=None
    if funs:
        fun=funs[0]
    return fun

def may_alias(a,b):
    nothinghascontext=True
    #pdb.set_trace()
    if not isinstance(a,set):
        A=set([a])
    else:
        A=a
    if not isinstance(b,set):
        B=set([b])
    else:
        B=b
    for a in A:
        for b in B:
            #pdb.set_trace()
            #if not isVar(a): return False
            #if not isVar(b): return False
            #pdb.set_trace()
            if hasattr(a, "_contexts") and hasattr(b,"_contexts"):
                nothinghascontext=False
                for v_a in a._contexts.values():
                    for s_v_a in v_a:
                        for v_b in b._contexts.values():
                            for s_v_b in v_b:
                                #print s_v_a.name
                                #print s_v_b.name
                                if s_v_b.name==s_v_a.name:
                                    return True
    #if nothinghascontext: assert False, "Bad alias info!"
    return False

def fa(obj,field):
    #pdb.set_trace()
    assert hasattr(obj,"_contexts"), "Must have context for obj!"
    res=set()
    for c1 in obj._contexts.values():
        for comp in c1:
            for l in comp._namespace[field]:
                res.add(l)
    return res

def set_values(sets):
    res=set()
    if isinstance(sets,set):
        for s in sets:
            if s.__class__.__name__=="Reference":
                if hasattr(s,"values"):
                    for v in s.values:
                        res.add(v)
            else:
                r=set_values(s)
                res|=r
    else:
        container=sets
        if hasattr(container,"_contexts"):
            for v_b in container._contexts.values():
                for s_v_b in v_b:
                    if hasattr(s_v_b,"values"):
                        for v in s_v_b.values:
                            res.add(v)
    return res
        
def field_values(sets,field):
    #pdb.set_trace()
    res=set()
    if isinstance(sets,set):
        for s in sets:
            if s.__class__.__name__=="Reference":
                if hasattr(s,"_namespace"):
                    if field in s._namespace:
                        for f_ref in s._namespace[field]:
                            if hasattr(f_ref,"_contexts"):
                                for v1 in f_ref._contexts.values():
                                    for v in v1:
                                        res.add(v)
            else:
                r=field_values(s)
                res|=r
    else:
        container=sets
        if hasattr(container,"_contexts"):
            for v_b in container._contexts.values():
                for s_v_b in v_b:
                    if hasattr(s_v_b,"_namespace"):
                        if field in s_v_b._namespace:
                            for f_ref in s_v_b._namespace[field]:
                                if hasattr(f_ref,"_contexts"):
                                    for v1 in f_ref._contexts.values():
                                        for v in v1:
                                            res.add(v)
    return res

def may_alias_values(needle,sets):
    assert isinstance(sets,set), "Expecting the output of field_values or set_values for the 2nd arguement."
    n_v=set()
    #assert hasattr(needle,"_contexts"), "Needle must have context (was not analyzed properly)"
    if not hasattr(needle,"_contexts"):
        return False
    for v1 in needle._contexts.values():
        for v2 in v1:
            for S in sets:
                if S.name==v2.name:
                    return True
    return False
def types(a):
    res=[]
    if not isinstance(a,set):
        A=set([a])
    else:
        A=a
    for a in A:
        for v_a in a._contexts.values():
            res+=v_a
    return res

def classes(where,objs):
    res=[]
    for i in objs:
        r=find_class(where,i.name.split(".")[-1]) 
        if r:
            res.append(r)
    return res
