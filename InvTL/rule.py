#yfrom lm_py.ast import ast
import re
import sys
import sha
import gc
import pickle
import pprint
import compiler
import pdb
import string
import inspect
import os
import difflib
from util_int import *

import py
log = py.log.Producer("InvTS:rule") 
import util_int
#pdb.set_trace()
py.log.setconsumer("InvTS:rule event", util_int.eventlog) #

HL = HugeLog()
stop=False
class DE:
    def __init__(self,LM,dct):
        self.ONCE=dct['once']
        self.AT=dct['at']
        self.IN=dct['in']
        self.BEGINNING=dct['beginning']
        self.END=dct['end']
        self.loc=dct['location']
        self.code=LM.SubjectCode(dct['code'])
        
class AIDD:
    def __init__ (self,LM,at,iff,de,do):
        #print "AAAAAAAAAAAAAAAAAAAAAA"
        #print do[1]
        self.do_before=LM.SubjectCode("")
        self.do_after=LM.SubjectCode("")
        self.do_instead=LM.SubjectCode("")
        self.at_pat=LM.SubjectCode("")
        self.orig_at=""
        self.orig_if=""
        self.orig_do_before=""
        self.orig_do_after=""
        self.orig_do_instead=""
        self.orig_de_field=""
        self.orig_de=None

        if do is not None:
            self.do_before=LM.SubjectCode(do[0])
            self.orig_do_before=do[0]
            try: 
                self.do_after=LM.SubjectCode(do[1])
                self.orig_do_after=do[1]
            except:
                self.do_after=LM.SubjectCode("")
                self.orig_do_after=""
            try: 
                self.do_instead=LM.SubjectCode(do[2])
                self.orig_do_instead=do[2]
            except:
                self.do_instead=LM.SubjectCode("")
        
        
        if at is not None:
            self.at_pat=LM.SubjectCode(at)
            self.orig_at=at
        self.de={}
        if de is not None:
            self.orig_de=de
            #pdb.set_trace()
            for de_elem in de:
                loc=LM.ConditionalCode(de_elem['location'])
                if loc not in de:
                    self.de[loc]=[]
                self.de[loc].append(DE(LM,de_elem))
        self.if_pat=LM.ConditionalCode(iff)
        self.orig_if=iff
        #print >>Debug(),  at
    def __getstate__(self):
        return self.do_before, self.do_after, self.do_instead, self.de, self.at_pat, self.if_pat 

    def __setstate__(self, args):
        assert len(args) == 6
        #self.__dict__.update(args[0]) 
        self.do_before=args[0]
        self.do_after=args[1]
        self.do_instead=args[2]
        self.de=args[3]
        self.at_pat=args[4]
        self.if_pat=args[5]

class Rule:
    def __init__ (self,LM,var,pat,ai,idd):
        self.LM=LM
        self.vars={}
        self.aidd=set(ai)
        #pdb.set_trace()
        self.idd=idd
        self.pattern=LM.SubjectCode(pat)
        if var[0]=="{":
            var=LM.SubjectCode(var)
        #pdb.set_trace()
        self.var=var
        self.last_postfix=""
        self.last_rep=""
        self.orig_pat=pat
        pass

    def __getstate__(self):
        #print self.__dict__
        return self.__dict__

    def __setstate__(self, args):
        self.__dict__.update(args) 

    def prep_vars(self,def_rep='',postfix=""):
        if def_rep=="":
            def_rep=self.last_rep
        else:
            self.last_rep=def_rep
        if postfix=="":
            postfix=self.last_postfix
        else:
            self.postfix=postfix
        R=set()
        for b in self.aidd:
            R.update(b.do_before.get_vars())
            R.update(b.do_after.get_vars())
            R.update(b.do_instead.get_vars())
            print >>Debug(),  (R)
            R.update(b.at_pat.get_vars())
            R.update(b.if_pat.get_vars())
            for K in b.de.keys():
                R.update(K.get_vars())
                for body in b.de[K]:
                    R.update(body.code.get_vars())

        for b in [self.idd]:
            R.update(b.do_before.get_vars())
            R.update(b.do_after.get_vars())
            R.update(b.do_instead.get_vars())
            print >>Debug(),  (R)
            R.update(b.at_pat.get_vars())
            R.update(b.if_pat.get_vars())
            for K in b.de.keys():
                R.update(K.get_vars())
                for body in b.de[K]:
                    R.update(body.code.get_vars())

        R.update(self.pattern.get_vars())    
        #R.update(self.if_pat.get_vars())
        if isinstance(self.var,str):
            R.add(self.var)
        else:
            R.update(self.var.get_vars())    

        R.add("$query")
        R.add("$textquery")
        R.add("$update")
        R.add("$module")
        for r in R:
            self.vars[r]=r.replace('$',def_rep)
            self.vars[r]=self.vars[r]+postfix
        #print >>Debug(),  self.pattern.gen_code(self.vars)
    def get_vars(self):
        if def_rep=="":
            def_rep=self.last_rep
        else:
            self.last_rep=def_rep
        if postfix=="":
            postfix=self.last_postfix
        else:
            self.postfix=postfix
        R=set()
        for b in self.aidd:
            R.update(b.do_before.get_vars())
            R.update(b.do_after.get_vars())
            R.update(b.do_instead.get_vars())
            print >>Debug(),  (R)
            R.update(b.at_pat.get_vars())
            R.update(b.if_pat.get_vars())
            for K in b.de.keys():
                R.update(K.get_vars())
                for body in b.de[K]:
                    R.update(body.code.get_vars())
        for b in [self.idd]:
            R.update(b.do_before.get_vars())
            R.update(b.do_after.get_vars())
            R.update(b.do_instead.get_vars())
            print >>Debug(),  (R)
            R.update(b.at_pat.get_vars())
            R.update(b.if_pat.get_vars())
            for K in b.de.keys():
                R.update(K.get_vars())
                for body in b.de[K]:
                    R.update(body.code.get_vars())
        R.update(self.pattern.get_vars())    
        #R.update(self.if_pat.get_vars())    
        if isinstance(self.var,str):
            R.add(self.var)
        else:
            R.update(self.var.get_vars())    
        #R.add(self.var)
        R.add("$module")
        R.add("$query")
        R.add("$textquery")
        R.add("$update")
        return R



def BindVars(LM,AST,vars,debug=False,lexical_way=False):
    #pdb.set_trace()
    for Var in vars.keys():
        if lexical_way :
            param=vars[Var]
            if param:
                param=LM.repr.to_string(vars[Var])
            else:
                param=LM.repr.to_string(LM.repr.bare_from_code(Var))
            ast=LM.repr.get(string.replace(LM.repr.to_string(AST),LM.repr.to_string(LM.repr.bare_from_code(Var)),param))
                
            if (debug): print >>Debug(), (LM.repr.to_string(LM.repr.bare_from_code(Var)))
            if (debug): print >>Debug(), (ast)
            if (debug): print >>Debug(), (AST)
            AST=ast
        else:
            #pdb.set_trace()
            #if Var=="X_0_0_1__EXPR__":
            #    pdb.set_trace()
            locs=LM.repr.find_locs(LM.repr.bare_from_code(Var),AST,AST,False,vars,True,False)
            if (debug): print >>Debug(), (LM.repr.to_string(LM.repr.bare_from_code(Var)),LM.repr.to_string(vars[Var]))
            if len(locs)>0:
                #ast_compare_result_print(locs)
                for L in locs:
                    #print >>Debug(), (AST)
                    #print >>Debug(),  (L[0])
                    #print >>Debug(),  (L[2])
                    #print >>Debug(),  (vars[Var])
                    LM.repr.replace(LM.repr.get_parent(L),L[0],vars[Var])
    #pdb.set_trace()
    return AST
def CodeToAst(LM,code,lexical_repl,bindings,strip,Lexical):
    cd=code.gen_code(lexical_repl)
    print >>Debug(), (code.gen_code({}))
    print >>Debug(), (cd)
    ast_cd=LM.repr.get(cd)
    #print >>Debug(), (ast_cd)
    ast_bound=BindVars(LM,ast_cd,bindings,False,Lexical)
    #print >>Debug(), (ast_bound)
    if strip:
        ast_cd=LM.repr.get_bare(ast_bound)
    return ast_cd

def CodeToAstWithRepl(LM,code,lexical_repl,bindings,Lexical=False):
    code=code.gen_code({})
    #print >>Debug(), (code)
    res=re.findall(r'(\$[_a-zA-Z][_a-zA-Z0-9]*\{[^}]+\})',code)
    repl={}
    print >>Debug(),  (res)
    local_bindings={}
    local_bindings.update(bindings)
    print >>Debug(), (local_bindings)
    for (k,v) in lexical_repl.items():
        if v not in local_bindings:
            local_bindings[v]=LM.repr.bare_from_code(v)
            #ast_strip(ast_from_code(v))#CodeToAst(LM.ConditionalCode(v),lexical_repl,bindings,True,Lexical)
            #print >>Debug(), (k,v,ast_strip(ast_from_code(v)))
    print >>Debug(), (local_bindings)
    for r in res:

        res=re.match(r'((\$[_a-zA-Z][_a-zA-Z0-9]*)(\{[^}]+\}))',r)
        var=res.group(2)
        v_dict=res.group(3)
        print >>Debug(),  (var,v_dict)
        lhs=CodeToAst(LM,LM.SubjectCode(var),lexical_repl,local_bindings,True,False)
        print >>Debug(),  (lhs)
        print >>Debug(),  (LM.SubjectCode(v_dict,False).gen_code(lexical_repl))
        print LM.SubjectCode(v_dict,False).gen_code(lexical_repl)
        rhs_dict=LM.EvalMetaExpression(LM.ConditionalCode(v_dict,False).gen_code(lexical_repl),local_bindings)
        ast_res=LM.repr.get_bare(LM.repr.replace_all(lhs,rhs_dict))
        repl[r]=(ast_res,var)
    for k in repl.keys():
        var_add=""#str(abs(hash(repl[k])))
        code=code.replace(k,lexical_repl[repl[k][1]]+var_add)
        local_bindings[lexical_repl[repl[k][1]]+var_add]=repl[k][0]
    #print >>Debug(), (code)
    #global stop
    #if (stop):
    #    pdb.set_trace()
    return CodeToAst(LM,LM.SubjectCode(code),lexical_repl,local_bindings,True,Lexical)

def ApplyAIDD(LM,A,vars,AST,rule,anngraph,dorepl=True,pattern=True,listindex=[0]):
    #locate, confirm, apply de transforms, replace by do
    #ast_strip(ast_from_code(A.at_pat.gen_code(rule.vars)))
    #at_ast=BindVars(at_ast,vars)
    #at_ast=CodeToAstWithRepl(LM,A.at_pat,{}rule.vars,vars,True)
    #x=False
    #pdb.set_trace()
    #if x:
    #    global stop
    #    stop=True
    #pdb.set_trace()
    at_ast=CodeToAstWithRepl(LM,A.at_pat,rule.vars,vars,True)
    #print "ZZZZZZZZZZZZZZZZZZZZZ"
    #print at_ast
    #print(A.at_pat.gen_code(),'=>',`LM.repr.to_string(at_ast)`)
    #pdb.set_trace()
    locs=LM.repr.find_locs(at_ast,AST,AST,pattern,vars,False,False)
    #pdb.set_trace()
    #print(vars)
    #ast_compare_result_print(locs)
    listindex[0]+=1
    #print len(locs)
    pos=0

    if not dorepl: return len(locs)!=0

    for L in locs:
        pos+=1
        L[0].repl_tag="%d_%d"%(listindex[0],pos)
        bvars={}
        bvars.update(vars)
        bvars.update(L[1])
        hold=True
        if len(A.if_pat.gen_code(rule.vars))>0:
            #pdb.set_trace()
            bvars[rule.vars["$update"]]=L[0]  #update the $update metavar
            code_if=A.if_pat.gen_code(rule.vars)
            hold=LM.EvalMetaExpression(code_if,bvars) #does the rule if condition hold?
            #print >>Debug(),  ifcode

            #print >>Debug(),  hold
#            if_ast=ast_strip(ast_from_code(if_code))
        if hold:
            #do_ast=CodeToAstWithRepl(A.do_after,rule.vars,bvars)
            #ast_replace(L[2],L[0],do_ast)
            log.event("De,Do Before, Do After")
            #print "ZZZZZZZZZZZZSDDDDDDDDDDDDD"
            #print A.at_pat.gen_code(rule.vars)
            #print >>Debug(),  (do_ast)
            #@Todo need to do DE
           #print A.do_instead.gen_code()
            for (k,v) in A.de.items():
                # k : the location for de
                # v : the list of DEs with that location
                cd=("%s"%k.gen_code(rule.vars))
                C= LM.EvalMetaExpression(cd,bvars)
                if not isinstance(C,list):
                    C=[C]
                #pdb.set_trace()
                for class_ast in C:
                    #pdb.set_trace()
                    if class_ast is None: continue
                    assert class_ast is not None, "Invalid 'Location' specification: %s"%cd
                    for i in v:
                        #i is an instance of DE
                        code_v=(CodeToAst(LM,i.code,rule.vars,bvars,True,False))
                        if hasattr(class_ast,"node"): insert_loc=class_ast.node
                        elif hasattr(class_ast,"code"): insert_loc=class_ast.code
                        else: assert False, "Do not know how to insert code into %s"%class_ast.__class__
                        if i.ONCE:
                            inserted_code=LM.repr.to_string(code_v)
                            if not hasattr(LM,"applied"):
                                LM.applied=set()
                            if inserted_code in LM.applied:
                                continue             
                            LM.applied.add(inserted_code)
                        if i.IN:
                            if i.BEGINNING:
                                if (isinstance(insert_loc,compiler.ast.Stmt)):
                                    LM.repr.prepend(insert_loc.nodes[0],code_v)
                            if i.END:
                                if (isinstance(insert_loc,compiler.ast.Stmt)):
                                    LM.repr.postpend(insert_loc.nodes[-1],code_v)
                        if i.AT:
                            if i.BEGINNING:
                                container=insert_loc.parent
                                index=container.parent.nodes.index(container)
                                container.parent.nodes.insert(index,LM.repr.make_statement(code_v))
                            if i.END:
                                container=insert_loc.parent
                                index=container.parent.nodes.index(container)
                                container.parent.nodes.insert(index+1,LM.repr.make_statement(code_v))
                    #pdb.set_trace()
            if A.do_before.code!="":
                do_before=LM.repr.make_statement(CodeToAstWithRepl(LM,A.do_before,rule.vars,bvars,False))
                print >>Debug(), ("1")
                LM.repr.prepend(L[0],do_before)
            if A.do_after.code!="":
                do_after=LM.repr.make_statement(CodeToAstWithRepl(LM,A.do_after,rule.vars,bvars,False))
                print >>Debug(), ("2")
                print >>Debug(), (L[0])
                print >>Debug(), (do_after)
                LM.repr.postpend(L[0],do_after)
            #print A.__dict__
            if A.do_instead.code!="":
                do_instead=CodeToAstWithRepl(LM,A.do_instead,rule.vars,bvars,False)
                #pdb.set_trace()
                #print do_instead
                #print("3")
                LM.repr.replace(LM.repr.get_parent(L),L[0],do_instead)

            #bvars[rule.vars["$update"]]=do_ast   #update the $update metavar
            
        pass
    pass
    return True

def ApplyIDD(LM,loc,A,vars,AST,rule,alt):
    #locate, confirm, apply de transforms, replace by do
    #ast_strip(ast_from_code(A.at_pat.gen_code(rule.vars)))
    #at_ast=BindVars(at_ast,vars)
    #at_ast=CodeToAstWithRepl(LM,A.at_pat,rule.vars,vars,True)
    #print "ZZZZZZZZZZZZZZZZZZZZZ"
    #print at_ast
    #print(A.at_pat.gen_code(),'=>',`LM.repr.to_string(at_ast)`)
    #locs=LM.repr.find_locs(at_ast,AST,True,vars,False,False)
    #print(vars)
    #ast_compare_result_print(locs)
    #print len(locs)
    for L in [loc]+alt:
        #print "C : " , L[2]
        bvars={}
        bvars.update(vars)
        bvars.update(L[1])
        hold=True
        if hold:
            #do_ast=CodeToAstWithRepl(A.do_after,rule.vars,bvars)
            #ast_replace(L[2],L[0],do_ast)
            log.event("De,Do Before, Do After")
            #print "ZZZZZZZZZZZZSDDDDDDDDDDDDD"
            #print >>Debug(),  (do_ast)
            #@Todo need to do DE

            for (k,v) in A.de.items():
                cd=("%s"%k.gen_code(rule.vars))
                C= LM.EvalMetaExpression(cd,bvars)               
                #pdb.set_trace()
                if not isinstance(C,list):
                    C=[C]               
                for class_ast in C:
                    if class_ast is None: continue
                    assert class_ast is not None, "Invalid 'Location' specification: %s"%cd
                    for i in v:
                        #i is an instance of DE
                        code_v=(CodeToAst(LM,i.code,rule.vars,bvars,True,False))
                        if i.ONCE:
                            inserted_code=LM.repr.to_string(code_v)
                            if not hasattr(LM,"applied"):
                                LM.applied=set()                       
                            if inserted_code in LM.applied:
                                continue        
                            LM.applied.add(inserted_code)
                        if hasattr(class_ast,"node"): insert_loc=class_ast.node
                        elif hasattr(class_ast,"code"): insert_loc=class_ast.code
                        else: assert False, "Do not know how to insert code into %s"%class_ast.__class__
                        if i.IN:
                            if i.BEGINNING:
                                if (isinstance(insert_loc,compiler.ast.Stmt)):
                                    LM.repr.prepend(insert_loc.nodes[0],code_v)
                            if i.END:
                                if (isinstance(insert_loc,compiler.ast.Stmt)):
                                    LM.repr.postpend(insert_loc.nodes[-1],code_v)
                        if i.AT:
                            if i.BEGINNING:
                                container=insert_loc.parent
                                index=container.parent.nodes.index(container)
                                container.parent.nodes.insert(index,LM.repr.make_statement(code_v))
                            if i.END:
                                container=insert_loc.parent
                                index=container.parent.nodes.index(container)
                                container.parent.nodes.insert(index+1,LM.repr.make_statement(code_v))

            #print A.do_instead.gen_code()            
            if A.do_before.code!="":
                do_before=LM.repr.make_statement(CodeToAstWithRepl(LM,A.do_before,rule.vars,bvars,False))
                print >>Debug(), ("1")
                LM.repr.prepend(L[0],do_before)
            if A.do_after.code!="":
                do_after=LM.repr.make_statement(CodeToAstWithRepl(LM,A.do_after,rule.vars,bvars,False))
                print >>Debug(), ("2")
                print >>Debug(), (L[0])
                print >>Debug(), (do_after)
                LM.repr.postpend(L[0],do_after)
            #print A.__dict__
            if A.do_instead.code!="":
                do_instead=CodeToAstWithRepl(LM,A.do_instead,rule.vars,bvars,False)
                #print do_instead
                print >>Debug(), ("3")
                LM.repr.replace(LM.repr.get_parent(L),L[0],do_instead)

            #bvars[rule.vars["$update"]]=do_ast   #update the $update metavar
            
        pass
    pass

def ApplyOneRule(LM,rule,AST,L,i,anngraph,alternatives):
    #L is the locus to update the rule
    pass

    #create the cached variable AST
    if isinstance(rule.var,str):
        var=LM.repr.get_bare(LM.repr.get(LM.SubjectCode(rule.var).gen_code(rule.vars)))
    else:
        var=LM.repr.get_bare(LM.repr.get(rule.var.gen_code(rule.vars)))

    #replace the invariant by the cached copy

    L[1][rule.vars["$query"]]=var #Rebind the $query variable
    if isinstance(rule.var,str):
        L[1][rule.vars[rule.var]]=var
    for l in alternatives:
        l[1][rule.vars["$query"]]=var #Rebind the $query variable
        if isinstance(rule.var,str):
            l[1][rule.vars[rule.var]]=var
         
    #print >>Debug(),  ast2string(AST)

  
    pre=LM.repr.to_string(AST)
    any_at_match = False
    for A in rule.aidd: #Apply all aidd tuples to locus
        any_at_match |= ApplyAIDD(LM,A,L[1],AST,rule,anngraph,dorepl=False)
    if not any_at_match:
        return
    ApplyIDD(LM,L,rule.idd,L[1],AST,rule,alternatives)
    try:
        LM.repr.reanalyze(AST)
        pass
    except Exception,inst:
        pass#print "Analysis failed post AIDD: %s"%`inst`

    for l in [L]+alternatives:
        if (rule.idd.do_instead.code==""):
            if isinstance(rule.var,str):
                LM.repr.replace(LM.repr.get_parent(l),l[0],var)
            else:
                #pdb.set_trace()
                do_instead=CodeToAstWithRepl(LM,rule.var,rule.vars,l[1],False)
                #print do_instead
                print >>Debug(), ("3")
                LM.repr.replace(LM.repr.get_parent(l),l[0],do_instead)
         
    HL.last().apps.append( (rule.idd, pre,LM.repr.to_string(AST)) )

    pre=LM.repr.to_string(AST)
    for A in rule.aidd: #Apply all aidd tuples to locus
        preAIDD=LM.repr.to_string(AST)
        ApplyAIDD(LM,A,L[1],AST,rule,anngraph)
        try:
            LM.repr.reanalyze(AST)
            pass
        except Exception,inst:
            pass#print "Analysis failed post AIDD: %s"%`inst`
        HL.last().apps.append( (A, preAIDD,LM.repr.to_string(AST)) )
    print
    HL.last().apps.append( (rule.idd, pre,LM.repr.to_string(AST)) )
    #
    #
    #r1,r2=get_blocks_diff(str_begin,str_end)
    #for i in r2:
    #    if hasattr(i,'added'):
    #        print "@@@@@@"
    #        print '\n'.join(i)
    #assert False
    
    #print >>Debug(),  var
    #print >>Debug(),  rule.vars

def ApplyRule(LM,rule,AST,rid="",DB=None,(infile,driverfile)=(None,None),search_LOC=None,refactor=False,overrideBind={}):
    global HL
    if DB is None: log.Warning("Cache is disabled!")
    if len(search_LOC)>3:
       print "Duplicate query  ", LM.repr.to_string(search_LOC[0]) 
       print " in ", LM.repr.to_string(search_LOC[2]) 
       for l in search_LOC[3:]:
           print " in ",LM.repr.to_string(l[2])
       print "End"
    if search_LOC is None:
        search_ast=AST
        search_parent=AST
    else:
        search_ast=search_LOC[0]
        search_parent=search_LOC[2]
    #Locate the rule pattern
    origASTHash=getHash(LM.repr.to_string(AST))
    origRuleHash=getHash(pickle.dumps(rule))
    anngraph=None
    log.event ("Processing rule:")
    log.event ("%s"%    rule.pattern.gen_code())
    log.event( "  inv_hash = %s"%origRuleHash)
    log.event( "  arg_hash = %s"%origASTHash)
    log.event( "  id = %s"%rid)
    #log.status ("Trying rule: %s"%rule.pattern.gen_code())
    LM.repr.prepare(AST)
    try:
        res= DB.load(origRuleHash,origASTHash,rid),True
        #print "!!!!!!!!!1"
        #print HL    
        #print "@@@@@@@@@2"
        #HL=DB.load("HL",origRuleHash,origASTHash,rid)
        #print "@@@@@@@@@3"
        #print HL
        #print "@@@@@@@@@4"
        return res
    except:
        pass
    goon=True
    i=0
    ol=0
    log.event("    failed loading from cache.")
    log.event("  applying rule...")
    applied=False
    while goon:
        i+=1
        rule.prep_vars('','_%s_%d__EXPR__'%(rid,i))
        if overrideBind:
            rule.vars.update(overrideBind)
        if rule.var=="$refactor" or refactor:
            lst=[AST,{rule.vars["$query"]:AST},None]
            #pdb.set_trace()
            #    lst[1].update(overrideBind)
            for A in rule.aidd: #Apply all aidd tuples to locus
                ApplyAIDD(LM,A,lst[1],AST,rule,None,pattern=overrideBind)
            goon=False
        else:
            old_graph=anngraph
            try:
                anngraph=LM.annotate(infile,LM.repr.to_string(AST),driverfile,DB)
            except:
                #If we cannot apply analysis right now, lets reuse old one
                log.event("  Could not annotate at rule %d"%(i-1))
                anngraph=old_graph

            pat_code=rule.pattern.gen_code(rule.vars)
            pat_ast=LM.repr.get_bare(LM.repr.get(pat_code))
            if_code=rule.idd.if_pat.gen_code(rule.vars)

            #pdb.set_trace()
            locs=LM.repr.find_locs(pat_ast,search_ast,search_parent,True,{},False,False,anngraph)
            for l in search_LOC[3:]:
                locs+=LM.repr.find_locs(pat_ast,l[0],l[2],True,{},False,False,anngraph)
                
                
            ln=len(locs)
            #print "ZZZZZZZZZZZZZZZZZZZZ"
            #print len(locs)
            #print if_code
    
            if ol==ln:
                goon=False
                break
            ol=ln
            #pdb.set_trace()

            canapply=False
            visited = set()
            for i in range(len(locs)):
                L = locs[i]
                if i in visited: continue
                alternates=[]  
                for j in range(len(locs)):
                  if i!=j and j not in visited:
                     if LM.repr.to_string(L[0])==LM.repr.to_string(locs[j][0]):
                         alternates.append((j,locs[j]))
                #try to apply the update to the found location
                L[1][rule.vars["$query"]]=L[0] #Bind the $query variable
                L[1][rule.vars["$textquery"]]=L[0] #Bind the $query variable
                L[1][rule.vars["$module"]]=AST
                #print (pat_code)
                #print (if_code)
                print(LM.repr.to_string(L[0]))
                if_condition_holds = LM.EvalMetaExpression(if_code,L[1])
                #print "AAAAAAAAAAAAA"
                #print hola
                real_alternates=[]
                for l in alternates:
                    if LM.EvalMetaExpression(if_code,l[1][1]):
                        visited.add(l[0])
                        real_alternates.append(l[1])
                if if_condition_holds:
		    visited.add(i)
                    print >>Debug(), (LM.repr.to_string(L[0]))
                    dumpVars (LM,L[1])
                    #print >>Debug(), (L[1])
                    #print >>Debug(), (ast2string(pat_ast))

                    #Condition was valid, applying rule
                    #Do rule application
                    #ast_compare_result_print(locs)
                    HL.new()
                    HL.last().rule=rule
                    HL.last().pre=LM.repr.to_string(AST)
                    #if (real_alternates) : print "AAAAAAAAAAAAAAAA" 
                    #else: print "BBBBBBBBBBBBBBBBBBB"
                    ApplyOneRule(LM,rule,AST,L,i,anngraph,real_alternates)
                    HL.last().post=LM.repr.to_string(AST)
                    applied=True
                    #goon=False #Should be gone for multiple rules to apply
                    canapply=canapply or True
                    goon=False
                    break
            goon=canapply
    log.event("    applied.")
    try :
        log.event("  storing in DB...")
        DB.save(AST,origRuleHash,origASTHash,rid)
        #if applied: DB.save(HL,"HL",origRuleHash,origASTHash,rid)
    except:
        pass
    return AST,applied


def GetLocs(LM,rule,AST,rid="",DB=None,(infile,driverfile)=(None,None)):
    if DB is None: log.Warning("Cache is disabled!")

    #Locate the rule pattern
    origASTHash=getHash(LM.repr.to_string(AST))
    #pdb.set_trace()
    origRuleHash=getHash(pickle.dumps(rule))
    log.event ("Processing rule:")
    log.event ("%s"%    rule.pattern.gen_code())
    log.event( "  inv_hash = %s"%origRuleHash)
    log.event( "  arg_hash = %s"%origASTHash)
    log.event( "  id = %s"%rid)
    log.status ("Finding matches for : %s"%rule.pattern.gen_code())
    #pdb.set_trace()
    LM.repr.prepare(AST)
    try:
        return DB.load(origRuleHash,origASTHash,rid)
    except:
        pass

    listlocs=[]

    log.event("    failed loading from cache.")
    log.event("  applying rule...")
    rule.prep_vars('','_%s_%d__EXPR__'%(rid,0))
    if rule.var=="$refactor":
        pass
    else:
        pat_code=rule.pattern.gen_code(rule.vars)
        pat_ast=LM.repr.get_bare(LM.repr.get(pat_code))
        if_code=rule.idd.if_pat.gen_code(rule.vars)
        #pdb.set_trace()
        locs=LM.repr.find_locs(pat_ast,AST,AST,True,{},False,False)

        canapply=False
        #print "ZZZZZZZZZZZZZZZZZZZZ"
        #print len(locs)
        for L in locs:
            #try to apply the update to the found location
            L[1][rule.vars["$query"]]=L[0] #Bind the $query variable
            L[1][rule.vars["$textquery"]]=L[0] #Bind the $query variable
            L[1][rule.vars["$module"]]=AST #Bind the $query variable
            hold = LM.EvalMetaExpression(if_code,L[1])
            if hold:
                listlocs.append(L)#LM.repr.get_parent(L))
    log.event("    applied.")
    try :
        log.event("  storing in DB...")
        DB.save(listlocs,origRuleHash,origASTHash,rid)
    except:
        pass
    #pdb.set_trace()
    return listlocs    


def dumpVars (LM,vars):
    for (k,v) in vars.items():
        print >>Debug(), ("%s -> %s"%(k,LM.repr.to_string(v)))

