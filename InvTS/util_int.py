import __builtin__
import pickle
import sha
import optparse
import re
import sys
import gc
import pprint
import compiler
import string
import inspect
import os
from UserList import UserList
import difflib
import rule
#from sets  import Set

#change this to any other logging
printer=None
def LOG(message):
    if printer==None:
        pass
    else:
        printer(message)
eventlog=LOG

#sys.path.append(os.path.realpath(os.path.split(os.path.split(os.path.realpath(os.path.dirname(__file__)))[0])[0]+"/pypy-dist/pypy"))


import py
log2 = py.log.Producer("InvTS:util") 
py.log.setconsumer("InvTS:util", eventlog) #

FILTER=''.join([(len(repr(chr(x)))==3) and chr(x) or '.' for x in range(256)])
def dump(src, length=8):
    N=0; result=''
    while src:
       s,src = src[:length],src[length:]
       hexa = ' '.join(["%02X"%ord(x) for x in s])
       s = s.translate(FILTER)
       result += "%04X   %-*s   %s\n" % (N, length*3, hexa, s)
       N+=length
    return result

class Debug:
    debug=False
    def __init__(self, stream=sys.stdout):
        self.stream=stream
        self.separator=""
        self.incheck=True
        print >>self
        self.incheck=False
        self.last_separator=True
    def write(self, text, s=None):
        if not Debug.debug:
            return
        if self.incheck:
             self.separator=text
             return
        if s==None:
             s=inspect.stack()[1]
        if (self.separator in text) and not text==self.separator:
             l = text.split(self.separator)
             for i in range(len(l)):
                 self.write(l[i], s)
                 if i!=len(l)-1:
                     self.write(self.separator, s)
             return
        if (self.last_separator):
             self.stream.write("# %s:%d @ %s # %s"%(os.path.basename(s[1]), s[2], s[3], text))
        else:
             self.stream.write(text)
        self.last_separator=(text==self.separator)




def getHash(S):
    return sha.new(S).hexdigest()

def iprint(args):
    import sys
    for i in args:
        sys.stdout.write( str(i)+" ")
    sys.stdout.write('\n')
def dprint (*args):
    test=not not False
    if test:
        s=inspect.stack()[1]
        #for k,v in s[0].__dict__.items():
        #    print k , ": ",v
        #print (inspect.getargvalues(s[0]))
        iprint(("#","%s:%d"%(os.path.basename(s[1]),s[2]),"@",s[3]," : ")+args)

class HugeLog:
    def __init__ (self):
        self.apps=list()
    def last(self):
        return self.apps[-1]
    def first(self):
        return self.apps[0]
    def new(self):
        self.apps.append(Application())
class Application:
    def __init__ (self):
        self.rule=None
        self.pre=None
        self.post=None
        self.apps=list()


def get_blocks_diff(a,b):
    d=difflib.Differ()
    res_r=[]
    cb_r=[]
    res_l=[]
    cb_l=[]
    change_l=False
    change_r=False
    result=list(d.compare(a.splitlines(), b.splitlines()))
    #from pprint import pprint
    #pprint(result)
    for i in result:
        data=i[2:]
        if i[:2]=='? ':
            continue
        if i[:2]=='  ':
            if not change_l and not change_r:
                cb_r.append(data)
                cb_l.append(data)
            elif not change_l and change_r:
                res_r.append(cb_r)
                cb_r=UserList([data])
                cb_l.append(data)
            elif change_l and not change_r:
                res_l.append(cb_l)
                cb_l=UserList([data])
                cb_r.append(data)
            elif change_l and change_r:
                res_r.append(cb_r)
                cb_r=UserList([data])
                res_l.append(cb_l)
                cb_l=UserList([data])
            change_r=False
            change_l=False
        elif i[:2]=='- ':
            if not change_l:
                res_l.append(cb_l)
                cb_l=UserList([data])
            elif change_l:
                cb_l.append(data)
            cb_l.added=True
            change_l=True
            #print "1"
        elif i[:2]=='+ ':
            if not change_r:
                res_r.append(cb_r)
                cb_r=UserList([data])
            elif change_r:
                cb_r.append(data)
            cb_r.added=True            
            change_r=True
    if len(cb_r)>0: res_r.append(cb_r)
    if len(cb_l)>0: res_l.append(cb_l)
    return res_l, res_r

import lm_py

