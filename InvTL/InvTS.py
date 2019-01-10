#import needed python modules
from path import path as Path
import pdb
import __builtin__
import traceback
import pickleshare
import pprint
import lm_py.py as py
import re
import rule
import ruleparser
import sys,os
import traceback 
import util 

log = None

def init_main(argv):
    global log
    log = py.log.Producer("InvTS:main") 
    #import util
    #py.log.setconsumer("InvTS:main event", util.eventlog) #

    #define local functions for path manipulations, etc...

    if len(argv)<2 or argv[1]=='--help':
        print r"""
    InvTS (c) Michael Gorbovitski 2005-2010
    The Invariant-Driven Transformation System
    Standard Usage:
      python InvTS.py [OPTIONS] Language_Module rules_db rules input driverfile output
      Transforms input into output using all rules in rules.invtl.
      This has the sideeffect of creating or updating the database in 
      rulefile.invtl.invts_db, the cache for InvTS.

      OPTIONS:
          --clean    Forces a flush of the cache DB, as well as wiping the output.
          --verbose  Output more information during the transformation.
          --force    Forces output to appear even if it does not pass testing.
          --view     Visualizes the transformation. Activates --clean.
      For an example, see rule.invtl in sample/rbac/
      To run the example, run:
      python InvTS.py lm_py sample/rbac/rule\_db.invt  sample/rbac/rule.invtl 
        sample/rbac/RBAC.py sample/rbac/driver.py sample/rbac/RBACOPT.py

    Custom Usage:
      python InvTS.py --view-CFG Language_Module input driverfile
      This analyzes input, and displays an interactive graph with the results.
    """
        sys.exit()
    class Flags:
        pass
    flags=Flags()
    flags.offset=1
    flags.clean=False
    flags.verbose=False
    flags.force=False
    flags.check_only=False
    flags.view=False
    while argv[flags.offset][:2]=="--":
        flag=argv[flags.offset]
        if flag=="--clean":
            flags.clean=True
        if flag=="--clean":
            flags.clean=True
        if flag=="--verbose":
            flags.verbose=True
        if flag=="--force":
            flags.force=True
        if flag=="--view":
            flags.view=True
            flags.clean=True
        if flag=="--view-CFG":
            flags.check_only=True
        flags.offset+=1
    lm=argv[flags.offset+0]

    rulefile=""
    outfile=""
    ruledb=""
    i=2
    if not flags.check_only:
        ruledb=argv[flags.offset+1]
        rulefile=argv[flags.offset+2]
        outfile=argv[flags.offset+5]
        i=0
    infile=argv[flags.offset+3-i]
    driverfile=argv[flags.offset+4-i]
    if len(argv)>flags.offset+6:
        object=argv[-1]
    else:
        object=None
    res=init_invts(lm,ruledb,rulefile,infile,driverfile,outfile,flags,object)
    return res

def main(argv):
    res = init_main(argv+[None])
    res = do_rules(*res)
    finish(*res)


def check(LM,infile,originfile,driverfile,db=None):
    global log
    try:    
        log.event("Initial analysis of %s"%infile)
        res=LM.check_program(infile,originfile,driverfile,db)
        log.event("  Succeeded")
        res.view()
        return 0
    except:
        log.event("  failed!")
        log.ERROR("Sanity Check Failed!!")
        LM.check_program(infile,originfile,driverfile,db,True)
        return 1

def init_invts(lm,ruledb,rulefile,infile,driverfile,outfile,flags,lm_object):
    """Processes the ruleset. Return values:
        0  :  Ok
        1  :  General Error
        2  :  Could not initialize Language Module 
    """
    global log
    log.Warning("lm_object: %s"%lm_object)
    try:
        langmodule=__builtin__.__import__(lm.split(":")[0],None,None,['LanguageModule'])
    except Exception, inst:
        log.ERROR("Cannot load Language Module: %s"%lm.split(":")[0])
        log.ERROR(str(inst))
        return 2
    LM=langmodule.LanguageModule(lm.split(":")[1:]+[lm_object])
    if LM is None:
        log.ERROR("Cannot initialize Language Module: %s with parameters: %s"%(lm,lm.split(":")[1:]))
        return 2;
    if flags.verbose:
        log.event("Switching verbose mode on")
        util.printer=LM.verbose_logger
        LM.set_log_output(util.printer)

    log.status("%s -> %s using ruleset %s, driver is %s"%(infile,outfile,rulefile,driverfile))
    try:
        originfile=LM.load(infile)
        try:
            LM.save(infile+".backup",originfile)
            log.event("Original input file has been saved to: %s"%(infile+".backup"))
        except:
            pass

    except Exception, inst:
        log.ERROR("Cannot read input file: %s"%infile)
        log.Warning(str(inst))
        return 1
#    try:
    try:
        #db=shelve.open(rulefile+".invts_db")
        db=pickleshare.PickleShareDB(rulefile+".invts_db")   
        if flags.clean:
            log.event("Wiping DB")
            db.clear()
    except Exception, inst:
        log.Warning("Cache database '%s'cannot be initialized"%(rulefile+".invts_db"))
        log.Warning(str(inst))
        db=None
    if flags.check_only:
        return check(LM,infile,originfile,driverfile)
    # try:
    #     log.event("Initial analysis of %s"%infile)
    #     #LM.check_program(infile,originfile,driverfile,db)
    #     log.event("  Succeeded")
    # except Exception, inst:
    #     log.event("  failed!")
    #     log.ERROR("Sanity Check Failed!!")
    #     log.Warning(str(inst))
    #     #LM.check_program(infile,originfile,driverfile,db,True)
    #     return 1
    repr=LM.repr.parse_file(infile)
    match_rules=ruleparser.ParseFile(rulefile,LM,db)
    rules=ruleparser.ParseFile(ruledb,LM,db)
    #if len(argv)>5:
    #    rules=[rules[int(argv[5])]]
    return (db,LM,repr,outfile,flags,driverfile,infile,originfile,match_rules,rules,lm_object)
#    except Exception, inst:
#        raise inst
    
 
def do_rules(db,LM,repr,outfile,flags,driverfile,infile,originfile,match_rules,rules,lm_object):
    for i in range(3):
      for ap in range(len(match_rules)): #Go over all matching rule
          repr=LM.repr.get_basic_analyzed(repr,driverfile)
          locs=rule.GetLocs(LM,match_rules[ap],repr,str(ap),db,(infile,driverfile))
          index=0
          lset = []
          for l in locs:
	      query=l[0]
              match=False
              for ol in lset:
                  if match: break
		  if LM.repr.to_string(query) == LM.repr.to_string(ol[0]):
		      match=True
		      ol.append(l)
		      break
              if not match:
                  lset.append(l)
          for l in lset:
              applied=False
              for XY in range(len(rules)):
                  #print "Applying ", rules[XY], ' to ', l
                  test,applied=rule.ApplyRule(LM,rules[XY],repr,"%s_%s_%s"%(i,str(XY),str(index)),db,(infile,driverfile),l)
                  if applied:
                      #repr=LM.repr.get_basic_analyzed(repr,driverfile)
                      index+=1
                      break
    return (db,LM,repr,outfile,flags,driverfile,infile,originfile,match_rules,rules,lm_object) 

def finish(db,LM,repr,outfile,flags,driverfile,infile,originfile,match_rules,rules,lm_object):
    try:
        try:
            try:
                db.close()
            except:
                pass
            #Sanity check of result
            try:
                LM.save(outfile,LM.repr.to_string(repr))
            except Exception, inst:
                log.ERROR("Could not write output file %s"%outfile)
                log.Warning(str(inst))
                return 1
            #if not flags.force:
            #    log.event("Sanity-checking %s..."%outfile)
            #    try:
            #        LM.check_program(outfile,LM.repr.to_string(repr),driverfile,db)
            #        log.event("  succeeded")
            #    except Exception,inst:
            #        log.event("  failed!")
            #        log.ERROR("Sanity Check Failed!!")
            #        log.Warning(str(inst))
            #        LM.check_program(outfile,LM.repr.to_string(repr),driverfile,db,True)
            if flags.view:
                import graph
                graph.MyGraphPage().display()
        except Exception, inst:
            traceback.print_exception(sys.exc_type, sys.exc_value, sys.exc_traceback,file=sys.stderr)
            log.Exception(str(inst))
    finally:
        try:
            log.event("Restoring original input file %s"%infile)
            LM.save(infile,originfile)
            return 0
        except Exception, inst:
            outdata=""
            print inst
            log.ERROR(inst)
            try:
                ofile=open(infile,'rb')
                outdata=ofile.read()
                ofile.close()
            finally:
                if originfile!=outdata:
                    log.ERROR("Input file %s has been corrupted!!!!"%infile)
                    try:
                        LM.save(infile+".backup2",originfile)
                        log.ERROR("Original input file has been saved to: %s"%(infile+".backup2"))
                    except:
                        pass


    

if __name__ == "__main__":
    sys.exit(main(sys.argv))
#test2(rulefile,infile,driverfile,outfile)
