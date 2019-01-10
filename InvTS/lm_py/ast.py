import pdb
import inspect
import compiler
import pyunparse
import parser
import re
import util
from util import *
from sets import Set
from types import *
from StringIO import *
from compiler.visitor import ASTVisitor
from compiler import parse, walk
from compiler.consts import *
from optparse import OptionParser

def ast2string(ast):
    file=StringIO()
    pyunparse.ast2py(ast,file)
    #pyunparse.Unparser(ast,file)
    return file.getvalue()

def ast_strip(ast):
    """Returns the AST stripped of module headers.
    """
    AST=ast
    #dprint AST
    if isinstance(AST, compiler.ast.Module) :
        AST=ast.node
    if isinstance(AST, compiler.ast.Stmt) :
        if len(AST.nodes)==1:
            AST=AST.nodes[0]
        else:
            AST=ast
    if isinstance(AST, compiler.ast.Discard) :
        AST=AST.expr
    if isinstance(AST,compiler.ast.Expression):
        AST=AST.node
    return AST

def ast_dump (ast):
    #dprint "astdump: ",ast
    #dprint ast.__dict__ 
    #if 'node' in ast.__dict__:
    #    dprint ast_dump(ast.node)
    dprint (`ast2string(ast)`)
    dprint (len(ast.getChildren()), ast.getChildren())
    
    for n in ast:
        #ast_dump(n)
        if isinstance(n, compiler.ast.Node) :
            dprint (n.__class__)
            ast_dump(n)
        else:
            dprint (n.__class__, n)
def allowed_classes(ast1,ast2):
    tv=False
    tv=tv or (isinstance(ast1,compiler.ast.Discard) and isinstance(ast2,list))
    tv=tv or (isinstance(ast1,compiler.ast.Tuple) and isinstance(ast2,compiler.ast.AssTuple)) 
    tv=tv or (isinstance(ast2,compiler.ast.Tuple) and isinstance(ast1,compiler.ast.AssTuple)) 
    tv=tv or (isinstance(ast1,compiler.ast.Name) and isinstance(ast2,compiler.ast.AssName)) 
    tv=tv or (isinstance(ast2,compiler.ast.Name) and isinstance(ast1,compiler.ast.AssName)) 
    tv=tv or (isinstance(ast1,compiler.ast.Name) and isinstance(ast2,compiler.ast.AssAttr)) 
    tv=tv or (isinstance(ast2,compiler.ast.Name) and isinstance(ast1,compiler.ast.AssAttr)) 
    tv=tv or (isinstance(ast1,compiler.ast.Name) and isinstance(ast2,compiler.ast.Getattr)) 
    tv=tv or (isinstance(ast2,compiler.ast.Name) and isinstance(ast1,compiler.ast.Getattr)) 
    tv=tv or (isinstance(ast1,compiler.ast.Getattr) and isinstance(ast2,compiler.ast.AssAttr)) 
    tv=tv or (isinstance(ast2,compiler.ast.Getattr) and isinstance(ast1,compiler.ast.AssAttr))
    if tv or (ast1.__class__ == ast2.__class__):
        #dprint "ALLOWED: ",ast1,ast2
        return True
    return False
def ast_eq(ast1,ast2,matches,bound_pat,comp_ignore,bound_vars,anntree):
    if not allowed_classes(ast1,ast2):
        return False
    A1=[n for n in ast1]
    A2=[n for n in ast2]

    if comp_ignore and isinstance(ast1,compiler.ast.Name) and isinstance(ast2,compiler.ast.AssAttr): 
        if ast1.name==ast2.attrname :
            return True

    if comp_ignore and isinstance(ast1,compiler.ast.Name) and isinstance(ast2,compiler.ast.Getattr):
        #pdb.set_trace()
        if ast1.name==ast2.attrname :
            return True

    if len(A1)!=len(A2) and not allowed_classes(ast1,ast2):
        #dprint "LENGTH MISMATCH"
        return False
    tv=True
    #print "1",ast1
    #print "2",ast2
    #print bound_pat
    #print "b",bound_vars
    #print matches
    if isinstance(ast1,compiler.ast.GenExprFor) and isinstance(ast2,compiler.ast.GenExprFor):
        if len(A1)!=len(A2):
            return False
    #pdb.set_trace()
    for i in range(min(len(A1),len(A2))):
        #print "a=",i
        #print "a:", allowed_classes(A1[i],A2[i]) 
    
        if allowed_classes(A1[i],A2[i]) :
            if isinstance(A1[i], compiler.ast.Stmt):
                if len(A1[i].nodes)==1:
                    if isinstance(A1[i].nodes[0],compiler.ast.Discard):
                        if isinstance(A1[i].nodes[0].expr,compiler.ast.Name):
                            if ast_eq(A1[i].nodes[0],[A2[i]],matches,bound_pat,comp_ignore,bound_vars,anntree):
                                #pdb.set_trace()                
                                exception=True
            elif isinstance(A1[i],compiler.ast.Node) and isinstance(A2[i],str):
                pdb.set_trace()
                tv= (tv and ast_eq(A1[i],A2[i],matches,bound_pat,comp_ignore,bound_vars,anntree))
            elif isinstance(A1[i], compiler.ast.Node) :
                tv= (tv and ast_eq(A1[i],A2[i],matches,bound_pat,comp_ignore,bound_vars,anntree))
            elif isinstance(A1[i],list) and isinstance(A2[i],list):
                tv= (tv and ast_eq(A1[i],A2[i],matches,bound_pat,comp_ignore,bound_vars,anntree))
            else:
                #print A1[i], (A2[i])
                exception=False
                try:
                    #pdb.set_trace()
                    #dprint bound_vars
                    if not (isinstance(bound_pat,dict) and A1[i] in bound_pat.values()):
                        #print "AAAAAAAAAA"
                        if bound_pat and re.search("_EXPR_",A1[i]) and A1[i] and A1[i] not in bound_vars:
                            #pdb.set_trace()
                            #dprint A1[i]
                            if A1[i] in matches :
                                if ast_eq(matches[A1[i]],ast_strip(ast_from_code(A2[i],'eval')),matches,False,False,bound_vars,anntree):
                                    exception=True
                                    #dprint ("LOCAL BOUND MATCH",A1[i],`ast2string(matches[A1[i]])`)
                            else:
                                matches[A1[i]]=ast_strip(ast_from_code(A2[i],'eval'))
                                exception=True
                        #if bound_pat and re.search("_VAR_",A1[i]) and A1[i] and A1[i] not in bound_vars:
                        #    matches[A1[i]]=ast_strip(ast_from_code(A2[i],'eval'))
                        #   exception=True
                except Exception, ex:
                    #dprint ex
                    pass
                tv= (tv and A1[i]==A2[i] or exception) 
                #print tv
                exception=False
        else:
            exception=False
            #do pattern match, if necessary
            if isinstance(A1[i], compiler.ast.Name) :
                if bound_pat and re.search("_EXPR",A1[i].name):
                    if not (isinstance(bound_pat,dict) and A1[i].name in bound_pat.values()):
                        #print "10",A1[i]
                        #print "20",ast2string(A1[i]) not in bound_vars
                        if ast2string(A1[i]) not in bound_vars:
                            #dprint "T", in bound_vars,bound_vars
                            if A1[i].name not in matches :
                                matches[A1[i].name]=A2[i]
                                exception=True
                            else:
                                #dprint "TEST",`ast2string(ast1)`
                                #dprint "TEST",`ast2string(ast2)`
                                #dprint "TEST",A1[i].name
                                #dprint "TEST",matches[A1[i].name]
                                #dprint "TEST",A2[i]
                                if ast_eq(matches[A1[i].name],A2[i],matches,False,False,bound_vars,anntree):
                                    exception=True
                        else:
                            pass
                            #dprint bound_vars
            if isinstance(A1[i], compiler.ast.AssName) :
                if bound_pat and re.search("_EXPR",A1[i].name) :
                    if not (isinstance(bound_pat,dict) and A1[i].name in bound_pat.values()):
                        if ast2string(A1[i]) not in bound_vars:
                            if A1[i].name not in matches :
                                matches[A1[i].name]=A2[i]
                                exception=True
                            else:
                                if ast_eq(matches[A1[i].name],A2[i],matches,False,False,bound_vars,anntree):
                                    exception=True
                        else:
                            pass
                            #dprint bound_vars
            if not exception:
                #dprint "Class Mismatch:",A1[i].__class__ ,A2[i].__class__,type(A1[i]),type(A2[i])
                #dprint A1[i]
                #dprint A2[i]
                return False
            exception=False
    #print "<=",tv
    return tv

def int_ast_compare (pat,ast,res,parent,patt,comp_ignore,debug,bound_vars,anntree):
    if (debug):
        dprint (`ast2string(ast)`,"==",`ast2string(pat)`)
        dprint ('\t',ast,'\n==\n\t',pat)
        dprint (len(ast.getChildren()), ast.getChildren())
        dprint (comp_ignore)
    m={}
    brk=False
    #if ast2string(ast)=='set((u for u in self.USERS for (name,c,) in self.SsdNC if len(set((r for r in set((r for r in self.ROLES if (u,r) in self.UR)) if (name,r) in self.SsdNR))) > c))':
    #    brk=True
    #    pdb.set_trace()
    if ast_eq(pat,ast,m,patt,comp_ignore,bound_vars,anntree):
        #dprint '\tTrue'
        i_d=[ast,m,parent]
        #i_d.__dict__["parent"]=parent
        #i_d.match=ast
        #i_d.bindings=m
        res.append( i_d )
    #if brk:
    #    pdb.set_trace()
    for n in ast:
        #ast_dump(n)
        if isinstance(n, list):
            #pdb.set_trace()
            int_ast_compare(pat,n,res,ast,patt,comp_ignore,debug,bound_vars,anntree)
        if isinstance(n, compiler.ast.Node):
            #dprint n.__class__
            int_ast_compare(pat,n,res,ast,patt,comp_ignore,debug,bound_vars,anntree)

def ast_compare(pattern,ast,parent,pat,bound_vars,comp_ignore,debug,anntree=None):
    """ Tries to match ast2 to ast1, at all subnodes of ast2.
    Basically, re.search(ast1,ast2)
    pat is whether to match patterns
    """
    #dprint `ast2string(ast)`,`ast2string(pattern)`
    #dprint len(ast.getChildren()), ast.getChildren()
    res=[]
    #dprint comp_ignore
    #pdb.set_trace()
    int_ast_compare(pattern,ast,res,parent,pat,comp_ignore,debug,bound_vars,anntree)
    return res

def ast_compare_result_print(res):
    for i in res:
        dprint ("Match: ",`ast2string(i[0])`)
        dprint ("Contained in: ",`ast2string(i[2])`)
        for k,v in i[1].items():
            dprint ('\t',k,":",`ast2string(v)`)

def load_suite(source_string):
    ast = parser.suite(source_string)
    return {"ast":ast, "code":ast.compile()}

def load_expression(source_string):
    ast = parser.expr(source_string)
    return {"ast":ast, "code":ast.compile()}

def ast_replace(parent,src,tgt,verbose=False):
    #pdb.set_trace()
    if isinstance(tgt,compiler.ast.Node):
        tgt.parent=parent
    #dprint parent.__dict__
    #pdb.set_trace()
    if isinstance(src,compiler.ast.Getattr) and isinstance(tgt,compiler.ast.Name):
        src.attrname=tgt.name
        tgt=src        
    if isinstance(src,compiler.ast.AssAttr) and isinstance(tgt,compiler.ast.Name):
        src.attrname=tgt.name
        tgt=src        
    debug=verbose
    for k,v in parent.__dict__.items():
        if debug:
            dprint (k)
            dprint ("\t", type(v))
        if isinstance(v, str) or isinstance(v,int):
            if src==v or `src`==`v`:
                parent.__dict__[k]=tgt
        elif isinstance(v,list) : 
            if len(v)>0 and isinstance(v[0],tuple):
                if debug:
                    dprint (v[0])
                    dprint ("\t", type(v[0]))
                l=[]
                for i in v[0]:
                    #dprint "COMPARING: ",src
                    #dprint "TO: ", i
                    if src==i:
                        l.append(tgt)
                    else:
                        l.append(i)
                v[0]=tuple(l)
            if verbose: 
                dprint ("REPLACE: ",v)
                dprint ("REPLACE: ",src)
                dprint ("REPLACE: ",tgt)
                dprint (src in v)
            if src in v:
                pos=parent.__dict__[k].index(src)
                del parent.__dict__[k][pos]
                parent.__dict__[k].insert(pos,tgt)
        else:
            if src==v:
                parent.__dict__[k]=tgt
    #pdb.set_trace()
def ast_prepend(src,ast):
    if isinstance(src,compiler.ast.Node):
        res=ast_of_type(src,compiler.ast.Stmt)
        if res!=None:
            for i in range(len(res.nodes)):
		if hasattr(src,"repl_tag") and hasattr(res.nodes[i],"repl_tag") and src.repl_tag==res.nodes[i].repl_tag:
                    res.nodes.insert(i,ast)
                    ast.parent=res
                    return
        if res!=None:
            for i in range(len(res.nodes)):
                if ast_compare(src,res.nodes[i],res,False,{},False,False)!=[]:
                    res.nodes.insert(i,ast)
                    ast.parent=res
                    break
def ast_postpend(src,ast):
    if isinstance(src,compiler.ast.Node):
        #dprint src.parent
        #dprint ast
        res=ast_of_type(src,compiler.ast.Stmt)
        if res!=None:
            for i in range(len(res.nodes)):
		if hasattr(src,"repl_tag") and hasattr(res.nodes[i],"repl_tag") and src.repl_tag==res.nodes[i].repl_tag:
                    res.nodes.insert(i+1,ast)
                    ast.parent=res
                    return
        if res!=None:
            for i in range(len(res.nodes)):
                if ast_compare(src,res.nodes[i],res,False,{},False,False)!=[]:
                    res.nodes.insert(i+1,ast)
                    ast.parent=res
                    break
        #dprint src.parent

def ast_insertafter(src,ast):
    if isinstance(src,compiler.ast.Node):
        #dprint src.parent
        #dprint ast
        res=ast_of_type(src,compiler.ast.Stmt)
        if res!=None:
            for i in range(len(res.nodes)):
		if hasattr(src,"repl_tag") and hasattr(res.nodes[i],"repl_tag") and src.repl_tag==res.nodes[i].repl_tag:
                    res.nodes.insert(i+1,ast)
                    ast.parent=res
                    return
        if res!=None:
            for i in range(len(res.nodes)):
                if ast_compare(src,res.nodes[i],res,False,{},False,False)!=[]:
                    res.nodes.insert(i+1,ast)
                    ast.parent=res
                    break
        #dprint src.parent        
def ast_replace_all(AST,dct):
    for lhs in dct.keys():
        locs=ast_compare(lhs,AST,AST,False,{},False,False)
        if len(locs)>0:
            #ast_compare_result_print(locs)
            for L in locs:
                ast_replace(L[2],L[0],dct[lhs],False)
    return AST
def ast_make_full(AST):
    for A in AST:
        if isinstance(A,compiler.ast.Node):
            A.parent=AST
            ast_make_full(A)

def ast_of_type(node,cl=compiler.ast.Class):
    if isinstance(node,cl):
        return node
    if isinstance(node,compiler.ast.Node) and 'parent' in node.__dict__:
        if node.parent!=None:
            if isinstance(node.parent,cl):
                return node.parent
            else:
                return ast_of_type(node.parent,cl)
    return None            

def ast_of_type2(node,cl=compiler.ast.Class):
    print node
    if isinstance(node,compiler.ast.Node) and 'parent' in node.__dict__:
        if node.parent!=None:
            if isinstance(node.parent,cl):
                return node.parent
            else:
                return ast_of_type2(node.parent,cl)
    return None            

            
def ast_find_function(ast,name):
    class FunctionVisitor(ASTVisitor):
        def __init__ (self,res):
            ASTVisitor.__init__(self)
            self.res=res
        def visitFunction(self,node):
            if node.name==name:
                res.append(node)
    res=[]
    f=FunctionVisitor(res)
    f.preorder(ast,f)
    return res

def ast_find_class(ast,name):
    class ClassVisitor(ASTVisitor):
        def __init__ (self,res):
            ASTVisitor.__init__(self)
            self.res=res
        def visitClass(self,node):
            if node.name==name:
                res.append(node)
    res=[]
    f=ClassVisitor(res)
    f.preorder(ast,f)
    return res
