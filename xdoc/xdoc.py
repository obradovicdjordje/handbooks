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
        if not self.seen(object):
            self.dictionary.update(vars(object)) # import module into self
            name = object.__name__
            self.run_docstring(object)
            names = object.__dict__.keys()
            names.sort()
            for name in names:
                if name[:2] != '__':
                    val = object.__dict__[name]
                    print name, val
                    if isinstance(val, types.ClassType):
                        self.run_class(val)
                    elif isinstance(val, types.ModuleType):
                        pass
                    elif not self.seen(val):
                        self.run_docstring(val)

    def run_class(self, object):
        if not self.seen(object):
            self.run_docstring(object)
            names = object.__dict__.keys()
            names.sort()
            for name in names:
                print name
                self.run_docstring(object.__dict__[name])

    def run_docstring(self, object):
        if hasattr(object, '__doc__'):
            s = object.__doc__
            if isinstance(s, str):
                if(s.startswith("api")):
                    print s

    def seen(self, object):
        result = self.already_seen.has_key(id(object))
        self.already_seen[id(object)] = 1
        return result

def main(args):
    modules = []
    for arg in args:
        for file in glob.glob(arg):
            if file.endswith('.py'):
                modules.append(__import__(file[:-3]))
    print modules
    XDoc(modules)

if __name__ == '__main__':
    main(sys.argv[1:])
