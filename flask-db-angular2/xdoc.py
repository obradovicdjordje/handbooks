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

    def run_module(self, obj):
        #print obj
        #if not self.seen(object):
        #    self.dictionary.update(vars(object)) # import module into self
        name = obj.__name__
        self.run_docstring(obj, obj)
        names = obj.__dict__.keys()
        names.sort()
        for name in names:
            if name[:2] != '__':
                val = obj.__dict__[name]
                #try:
                #    print name, val, type(val).__name__, "xxxxxxxxxxxxxxxxxx"
                #except:
                #    pass
                ttype = type(val).__name__
                if(ttype == 'MethodViewType'):
                    self.run_class(val, name)
                if isinstance(val, types.ClassType):
                    self.run_class(val, name)
                elif isinstance(val, types.ModuleType):
                    #print val.__name__, '=========='
                    #self.run_module(val)
                    pass
                elif not self.seen(val):
                    self.run_docstring(val, obj)

    def run_class(self, object, class_name):
        if not self.seen(object):
            self.run_docstring(object, object)
            names = object.__dict__.keys()
            names.sort()
            for name in names:
                #print name, "............."
                self.run_docstring(object.__dict__[name], object, class_name)

    def run_docstring(self, object, parent, class_name=''):
        if hasattr(object, '__doc__'):
            s = object.__doc__
            if isinstance(s, str):
                if(s.startswith("api")):
                    #for d in dir(object):
                    #    print d
                    print  object.__module__, '|', class_name, '|', object.__name__
                    print s[3:]

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
                #print tt
                modules.append(__import__(tt, globals(), locals(), ['object'], -1))
    #print modules
    XDoc(modules)

if __name__ == '__main__':
    main(sys.argv[1:])
