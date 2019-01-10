#Set up import environment for local large libs
#import local things
from path import path as Path
import new

#define log
def LOG(message):
    if printer==None:
        pass
    else:
        printer(message)

eventlog=LOG
printer=None

from pypy.tool.ansi_print import ansi_log

from ast import *
from util import *

##IMPORTANT
#This imports all availible functions that may be called
from rule_func import *

class Repr:
    """This class wraps the representation of the subject language"""
    def parse_file(self, infile):
        return compiler.parseFile(infile)
    def get(self,string):
        return ast_from_code(string)
    def get_basic(self,repr):
        return ast_from_code(ast2string(repr))
    def get_basic_analyzed(self,repr,driver,fnametemp=[0]):
        fnametemp[0]+=1
        rpr = ast2string(repr).replace("__EXPR__","__REPR__")
        print "Transforming @%d.py^"%fnametemp[0]
        f=open("temp/%d.py"%fnametemp[0],'w')
        f.write(rpr)
        f.close()
        ast=ast_from_code(rpr)
        return ast
    def make_statement(self,stmt):
        while (not (isinstance(stmt, compiler.ast.Stmt) or isinstance(stmt, compiler.ast.Module))) and "parent" in dir(stmt):
            stmt=stmt.parent
        return stmt
    def reanalyze(self,ast):
        sys.stdout.write(",")
        return ast
    def prepare(self,repr):
        ast_make_full(repr)
    def get_bare(self,repr):
        return ast_strip(repr)
    def bare_from_code(self,code):
        return ast_strip(ast_from_code(code))
    def to_string(self,repr):
        return ast2string(repr)
    def annotate(self,infile,contents,driver,DB=None,error=False):
        return do_annotations(infile,contents,driver,DB,error)
    def find_locs(self,pattern,ast,parent,pat,bound_vars,comp_ignore,debug,anntree=None):
        """ Tries to match ast2 to ast1, at all subnodes of ast2.
        Basically, re.search(ast1,ast2)
        pat is whether to match patterns
        """
        locs=ast_compare(pattern,ast,parent,pat,bound_vars,comp_ignore,debug,anntree=None)
        for L in locs:
            for kv in L[1].keys():
                R=ast_compare(L[1][kv],L[0],L[2],True,{},False,False)
                if R:
                    val=R[0][0]
                else:
                    val=L[1][kv]
                L[1][kv]=val
        return locs
    def get_parent(self,loc):
        return loc[2]
    def replace(self,parent,source,target):
        ast_replace(parent,source,target,False)
    def replace_all(self,repr,dct):
        ast_replace_all(repr,dct)
    def prepend(self,src,repr):
        ast_prepend(src,repr)
    def postpend(self,src,repr):
        ast_postpend(src,repr)
    def find_function(self,src,name):
        return ast_find_function(src,name)
class LanguageModule:
    def __init__(self,params):
        self.ConditionalCode=ConditionalCode
        self.SubjectCode=Code
        self.LanguageID="py"
        self.LanguageName="python"
        self.repr=Repr()
        self.verbose_logger=ansi_log
        #self.funcs=rule_func
    def __getstate__(self):
        odict = self.__dict__.copy() # copy the dict since we change it
        del odict['verbose_logger']              # remove filehandle entry
        return odict

    def __setstate__(self,dict):
        self.__dict__.update(dict)   # update attributes
        self.verbose_logger = ansi_log                 # save the file object
    def save(self,name,data):
        if isinstance(data, dict):
            for (k,v) in data.items():
                self.save(name+"/"+k,v)
        else:
            ifile=open(name,'wb')
            ifile.write(data)
            ifile.close()
    def load(self,name):
        ifile=open(name,'rb')
        data=ifile.read()
        ifile.close()
        self.repr.filename=name
        return data
    def set_log_output(self,logger):
        global printer
        printer=logger

    def check_program(self,infile,contents,driver,DB=None,debug=False):
        return do_annotations(infile,contents,driver,DB,debug)


    def EvalMetaExpression(self,code,bindings):
        """ Evaluates the code, with variable bindings in the dict bindings"""
        _code=""
        for Var in bindings.keys():
            _code+=("%s=param['%s']\n"%(Var,Var))
            #bindings[Var].__getattr__=new.instancemethod(G,bindings[Var],bindings[Var].__class__)
            if not hasattr(bindings[Var].__class__,"__getattr__"):
                bindings[Var].__class__.__getattr__=new.instancemethod(G,None,bindings[Var].__class__)

        #_code=(_code+"pdb.set_trace()\n\n")
        _code=(_code+"ret="+code+"\n\n")
        ret=None
        try:
            #print _code
            #print bindings.keys()
            #print "ret"
            ret= eval_query(_code,bindings,"ret")
        except NameError , inst:
            dprint (inst)
            ret=None
        except Exception, inst:
            dprint ("A\n")
            dprint(_code)
            dprint(bindings)
            #pdb.set_trace()
            raise Exception, inst
        finally:
            pass
            #for Var in bindings.keys():
            #    try:
            #        del bindings[Var].__class__.__getattr__
            #    except:
            #        pass
        return ret

def G(self,key):
    #pdb.set_trace()
    if "_contexts" in self.__dict__:
        res=set()
        for c1 in self._contexts.values():
            for comp in c1:
                if key not in comp._namespace:
                    raise AttributeError("Attribute lookup for metavariable failed! Object: Unknown, Field: %s"%(key))
                for l in comp._namespace[key]:
                    res.add(l)
        if len(res)==0:
            raise AttributeError("Attribute lookup for field %s failed!"%key)
        return res
    else:
        raise AttributeError("Attribute lookup for field %s failed!"%key)

def funcToMethod(func,clas,method_name=None):
    method = new.instancemethod(func,None,clas)
    if not method_name: method_name=func.__name__
    clas.__dict__[method_name]=method

class ConditionalCode:
    def __init__(self, code,strip=True):
        if code is None:
            self.code=""
            return
        if strip and code.startswith('{') and code.endswith('}'):
            lines = code[1:-1].splitlines()
        else:
            lines = code.splitlines()
        while lines and blank_line_re.match(lines[0]):
            lines.pop(0)
        while lines and blank_line_re.match(lines[-1]):
            lines.pop(-1)
        if lines:
            #res=[]
            indents = [len(indent_re.match(line).group(0)) for line in lines]
            indent = indents[0]
            if min(indents) >= indent:
                lines = [line[indent:] for line in lines]

            lines=[line.rstrip() for line in lines]
            if False:
                ls=[]
                if (len(lines)>1):
                    indents = [len(indent_re.match(line).group(0)) for line in lines[1:]]
                    mi=min(indents)
                    if lines[0].rstrip()[-1]==':' and mi!=0:
                        mi-=1
                    ls=[line[mi:] for line in lines[1:]]
                lines=[lines[0].lstrip()]+ls
        self.code = "".join([line+"\n" for line in lines])
        #dprint( lines)
        #dprint( self.code)
    def __getstate__(self):
        return self.code

    def __setstate__(self, args):
        self.code=args
    def empty(self):
        return False
    def gen_code(self, dict={},dict2={},indent=None, counters=None, pos=None):
        if indent is None:
            ret=self.code.strip()
        else:
            ret= "\n".join([indent+line for line in self.code.splitlines()])
        #lst.reverse()
        #dprint([K for K,V in lst])
        #dprint([K for K,V in lst])
        sl=sorted([(K,V) for K,V in dict.items()],lambda x,y: -1*cmp(x,y))#order_substring_tuple)
        for K,V in sl:
            #dprint K,V
            ret=ret.replace(K,V)
        for K,V in sorted([(K,V) for K,V in dict2.items()],order_substring_tuple):
            #dprint K,V
            ret=ret.replace(K,V)
        return ret
    def get_vars (self):
        return set(re.findall(r'\$[a-zA-Z]\w*',self.code))
class Code(ConditionalCode):
    def __init__(self, code,strip=True):
        ConditionalCode.__init__(self,code,strip)

########################################################################
#                    Internal things. Not required.                    #
########################################################################
blank_line_re = re.compile("^\s*$")
indent_re = re.compile("^\s*")

def eval_query (code,param,retarg="ret"):
    #dprint code
    #dprint(code)
    exec(load_suite(code)["code"]) #code uses param internally to lookup
    return eval(retarg)

