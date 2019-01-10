import string, os,sys,re,types,pprint
import operator
import re
from types import *
import tpg
from sets import Set
from rule  import *
from StringIO import *
import pickle

import py
log = py.log.Producer("InvTS:ruleparser") 
import util_int
py.log.setconsumer("InvTS:ruleparser event", util_int.eventlog) #


def MATCH_BRACES(S):
    lev=0
    for i in S:
        if i=="{": lev+=1
        if i=="}": lev-=1
        if lev<0:
            return False
    if lev==0:
        return True
    return False

def MATCH_PARENS(S):
    #print S
    lev=0
    for i in S:
        if i=="(": lev+=1
        if i==")": lev-=1
        if lev<0:
            return False
    if lev==0:
        return True
    return False

def genParser(langid,aidd=True):
    TOKENS=r"""
        token var      '\$[a-zA-Z]\w*';
        token LANG            '%s';
        token MATCH_BRACES    '$call$' MATCH_BRACES;
        token MATCH_PARENS    '$call$' MATCH_PARENS;
    """%langid
    LEXER=r"""
        set lexer = ContextSensitiveLexer
        set lexer_multiline = True 
        set lexer_dotall = True 
        separator space '(\s)+';
    """    
    AI=r"""
              AIDD/aidd         ->  $iff=None$ $de=None$ AT/at IF/iff? (DEA/de)? DOA/do $aidd=AIDD(self.LM,at,iff,de,do)$;
               AT/R             -> 'at' LANGEXPR/R;
               IF/R             -> 'if' IFEXPR/R ;
               DEA/X             -> $de=[]$ 'de' (DEABODY/R $de.append(R)$)+ $X=de$;
                DEABODY/R        -> $l=None$ $once=False$ $at=False$ $end=True$ 'de'? ('once' $once=True$)? ( ('at' $at=True$ | 'in' ) )? (('beginning' $end=False$)| 'end')?  IFEXPR/cond (METHOD/R $l=R$ ) 
                                       $R={'once':once,'at':at,'in':not at,'beginning':not end,'end':end,'location':cond, 'code':l}$;
               DOA/R             -> 'do' ((DOABEFORE/R1 $R3=""$ (DOAINSTEAD/R3)? $R2=""$ (DOAAFTER/R2)? $R=[R1,R2,R3]$) | (DOAANY/R1 $R=["",R1,""]$) | (DOAINSTEAD/R1 $R=["","",R1]$)) ;
                DOABEFORE/R      -> 'do'? 'before' LANGEXPR/R;
                DOAAFTER/R       -> 'do'? 'after' LANGEXPR/R;
                DOAINSTEAD/R     -> 'do'? 'instead'  LANGEXPR/R;
                DOAANY/R         -> 'do'? ('after')? LANGEXPR/R;
    """
    if not aidd:        AI="\n\n\n"
    parserdef=LEXER+TOKENS+r"""
        START/R             ->  EXPR/R;
        EXPR/rules          ->  $rules=[]$ ((RULE/R | RULE2/R | RULE3/R)  $rules.append(R)$ )+;
         RULE2/R            ->  'match' LANGEXPR/P IDD/ID $A=[]$ $R=Rule(self.LM,"__replacer",P,A,ID)$;
         RULE/R             ->  'inv' var/V '=' LANGEXPR/P IDD/ID $A=[]$ ('\('? (AIDD/a $A.append(a)$)* '\)'?) $R=Rule(self.LM,V,P,A,ID)$;
         RULE3/R            ->  'inv' LANGEXPR/V '=' LANGEXPR/P IDD/ID $A=[]$ ('\('? (AIDD/a $A.append(a)$)* '\)'?) $R=Rule(self.LM,V,P,A,ID)$;
          IDD/aidd          ->  $iff="True"$ $de=None$ $do=None$ IF/iff? ( DE/de )? DO/do? $aidd=AIDD(self.LM,None,iff,de,do)$;
           IF/R             -> 'if' IFEXPR/R ;
               DE/X         -> $de=[]$ 'de' (DEBODY/R $de.append(R)$)+ $X=de$;
                DEBODY/R    -> $l=None$ $once=False$ $at=False$ $end=True$ ('de')? ('once' $once=True$)? ( ('at' $at=True$ | 'in' ) )? (('beginning' $end=False$)| 'end')?  IFEXPR/cond (METHOD/R $l=R$ ) 
                                       $R={'once':once,'at':at,'in':not at,'beginning':not end,'end':end,'location':cond, 'code':l}$;
             METHOD/R       -> LANGEXPR/R;
           DO/R             -> ((DOBEFORE/R1 $R3=""$ (DOINSTEAD/R3)? $R2=""$ (DOAFTER/R2)? $R=[R1,R2,R3]$) | (DOANY/R1 $R=["",R1,""]$) | (DOINSTEAD/R1 $R=["","",R1]$)) ;
            DOBEFORE/R      -> 'do'? 'before' LANGEXPR/R;
            DOAFTER/R       -> 'do'? 'after' LANGEXPR/R;
            DOINSTEAD/R     -> 'do'? 'instead'  LANGEXPR/R;
            DOANY/R         -> 'do'? ('after')? LANGEXPR/R;
%s
        IFEXPR/expr         ->  '\(' MATCH_PARENS/expr '\)'; 
        LANGEXPR/expr       ->  LANG/L '\{(\s)*'/S MATCH_BRACES/expr $expr=S+expr+'}'$'\}' $self.check_lang(L)$;
    """%AI

#"""
#           DE/X             -> 'de' $cm=[]$ $lpre=[]$ $lpost=[]$ $f=None$ (CLASS_METHOD/R $cm.append(R)$)* (LOCATION_PRE/R $lpre.append(R)$)* (LOCATION_POST/R  $lpost.append(R)$)* (FIELD/F $f=F$)? $X=[cm,f,lpre,lpost]$;
# 
#"""
    class ParserMeta(tpg.ParserMetaClass):
        def __init__(cls, name, bases, dict):
            dict['__doc__']=parserdef
            tpg.ParserMetaClass.__init__(cls,name,bases,dict)

    class IncRule(tpg.VerboseParser):
        __metaclass__ = ParserMeta
        #$print "\n===\n",A,"\n==="$
        verbose=0
        def __call__(self, input,lm, *args, **kws):
            self.LM=lm
            input=re.sub(r'//(.*?)\n','\n',input)     #Killing // comments
            return tpg.VerboseParser.parse(self,'START', input, *args, **kws)
        def  check_lang(self,lm):
            #print lm
            #print self.LM.LanguageID
            assert lm==self.LM.LanguageID
    return IncRule
def ParseRules(LM,stream=sys.stdin.read):
    if stream==sys.stdin.read:
        stream=sys.stdin.read()
    Parser=genParser(LM.LanguageID)
    imp=Parser()
    instr=stream
    res=imp(instr,LM)
    #print res

    for i in res:
        i.prep_vars()
    return res
def ParseLocs(LM,stream=sys.stdin.read):
    if stream==sys.stdin.read:
        stream=sys.stdin.read()
    Parser=genParser(LM.LanguageID,False)
    imp=Parser()
    instr=stream
    res=imp(instr,LM)
    #print res

    for i in res:
        i.prep_vars()
    return res
def ParseString(LM,src,DB):
    hsc=getHash(src)
    obj=None
    try:    
        res= DB.load(src)
        print res
        return res
    except: 
        log.event("Could not load rule with hash: %s from DB"%(hsc ))
    obj = ParseRules(LM,src)
    try:
        DB.save(obj,src)
        log.event("Stored in DB rule with hash: %s"%hsc)
    except:
        log.Warning("Could not store rule with hash: %s in DB"%(hsc ))
    return obj

def ParseFile(path,LM,DB):
    if DB is None: log.Warning("Cache is disabled!")
    res=[]
    f = open(path, "U")
    log.status("Loading rules from %s"%path)
    srclines = f.readlines()
    f.close()
    #load from cache, if possible
    src=[]
    cf=""
    for l in srclines:
        if l[:2]=="//" or l[:1]=="#":
            continue
        if (len(l)>3 and l[:3]=="inv" and cf!="") or (len(l)>5 and l[:5]=="match" and cf!=""):
            src.append(cf)
            cf=""
        cf+=(l)
    if cf[:3]=="inv" or cf[:5]=="match":
        src.append(cf)
    cf=""
    for s in src:
        #print s
        res+=ParseString(LM,s,DB)
    log.event("Loaded %d rules"%len(res))
    log.status("Loaded %d rules"%len(res))
    return res

def StoreRules(rules,path):
    f=open(path,"wb")
    pickle.dump(rules,f)
    f.close()
def LoadRules(path):
    f=open(path,"rb")
    res=pickle.load(f)
    f.close()
    return res

