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
