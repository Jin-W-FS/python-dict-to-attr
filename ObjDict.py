false = False
true = True

class ObjDict(dict):
    def __init__(self, obj):
        dict.__init__(self, obj)
        self.__dict__ = self

def build(obj):
    if isinstance(obj, dict):
        return ObjDict({ k : build(obj[k]) for k in obj })
    elif isinstance(obj, list):
        return [ build(v) for v in obj ]
    else:
        return obj

def loads(str):
    return build(eval(str))

def load(file):
    return loads(file.read())

if __name__ == "__main__":
    from sys import argv
    from pprint import pprint
    pprint(load(file(argv[1])))
