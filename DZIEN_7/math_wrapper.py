from functools import wraps

def debug(func):
    @wraps
    def wrapper(*args,**kwargs):
        print(f'Pełna nazwa metody: {func.__qualname__}')
        return func(*args,**kwargs)
    return wrapper

def debugmethods(cls):
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
    return cls

