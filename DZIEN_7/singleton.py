class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonClass(metaclass=Singleton):pass
class Regular:pass

x = Regular()
y = Regular()

print(x==y)
print(x)
print(y)

a = SingletonClass()
b = SingletonClass()

print(a==b)
print(a)
print(b)
