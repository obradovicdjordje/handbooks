import glob
import re, sys, types

class XDoc:
    """
        XDoc class is modification of the Piter Norvig's class
        http://norvig.com/docex.html
    """
    def __init__(self, modules):
        self.dictionary = {}
        self.already_seen = {}
        for module in modules:
            self.run_module(module)

    def run_module(self, object):
        #print object.__name__
        #if not self.seen(object):
        #    self.dictionary.update(vars(object)) # import module into self
        name = object.__name__
        self.run_docstring(object)
        names = object.__dict__.keys()
        names.sort()
        for name in names:
            if name[:2] != '__':
                val = object.__dict__[name]
                try:
                    print name, val
                except:
                    pass
                if isinstance(val, types.ClassType):
                    self.run_class(val)
                elif isinstance(val, types.ModuleType):
                    print val
                    self.run_module(val)
                    pass
                elif not self.seen(val):
                    self.run_docstring(val)

    def run_class(self, object):
        if not self.seen(object):
            self.run_docstring(object)
            names = object.__dict__.keys()
            names.sort()
            for name in names:
                self.run_docstring(object.__dict__[name])

    def run_docstring(self, object):
        if hasattr(object, '__doc__'):
            s = object.__doc__
            if isinstance(s, str):
                #if(s.startswith("api")):
                print s

    def seen(self, object):
        result = self.already_seen.has_key(id(object))
        self.already_seen[id(object)] = 1
        return result

def main(args):
    modules = []
    import os
    for root, dirs, files in os.walk("app"):
        for file in files:
            if file.endswith(".py"):
                pfile = os.path.join(root, file)
                tt = pfile.replace("/", ".")
                tt = tt[:-3]
                print tt
                modules.append(__import__(tt))
    #print modules
    XDoc(modules)

if __name__ == '__main__':
    main(sys.argv[1:])
