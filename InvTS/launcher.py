#This script shows you how to launch InvTS Programmically.
import sys
sys.path+=["."] #path to InvTS
import InvTS
InvTS.main("dummy lm_py sample/rbac/rule_db.invtl sample/rbac/rule.invtl sample/rbac/RBAC.py sample/rbac/driver.py sample/rbac/output.py".split(" "))

