import sys
import jiphy # pip install
from os import path
from types import ModuleType
import codecs

class JsFinder(object):
    def find_module(self, name, m_path):
        name += '.js'
        if m_path is not None:
            name = path.join(m_path[0], name)
        if path.exists(name):
            return JsLoader(name)


class JsLoader(object):
    def __init__(self, name):
        self.name = name
        content = codecs.open(name,"rb","utf-8")
        self.content = content.read()

    def load_module(self, name):
        module = ModuleType(name)
        exec(jiphy.to.python(self.content), module.__dict__)
        return module

sys.meta_path.append(JsFinder())