import types

def notify(fn,*args,**kwargs):

    def fncomposite(*args,**kwargs):
        print(f'{fn.__name__} została uruchomiona...')
        rt = fn(*args,**kwargs)
        return rt

    return fncomposite

# fncomposite == wrapper

class Notifies(type):
    def __new__(cls, clsname,bases, adict):
        for name,value in adict.items():
            if type(value) is types.FunctionType or type(value) is types.MethodType:
                adict[name] = notify(value)
        return super(Notifies,cls).__new__(cls, clsname,bases, adict)

class Math(metaclass=Notifies):
    def multi(a,b):
        p = a*b
        print(p)
        return p

Math.multi(6,7)

class Info(metaclass=Notifies):
    def intro(self):
        print('to jest ważna informacja!')

i = Info()
i.intro()
