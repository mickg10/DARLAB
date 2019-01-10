import sys
import __builtin__
class RollbackImporter:
    def __init__(self):
        "Creates an instance and installs as the global importer"
        self.previousModules = sys.modules.copy()
        self.realImport = __builtin__.__import__
        __builtin__.__import__ = self._import
        self.newModules = {}
        
    def _import(self, name, globals=None, locals=None, fromlist=[]):
        result = apply(self.realImport, (name, globals, locals, fromlist))
        self.newModules[name] = 1
        return result
    def stop(self):
        __builtin__.__import__ = self.realImport
    def start(self):
        self.realImport = __builtin__.__import__
        __builtin__.__import__ = self._import

    def uninstall(self):
        for modname in self.newModules.keys():
            if not self.previousModules.has_key(modname):
                # Force reload when modname next imported
                try:
                    del(sys.modules[modname])
                except:
                    print "Cannot unload module: %s"%modname
                    pass
        __builtin__.__import__ = self.realImport
