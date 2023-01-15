def short_repr(cls):
    cls.__repr__ = lambda self:super(cls,self).__repr__()[:8]
    return cls

@short_repr
class ClassWithRelLongName:
    pass

if __name__ == '__main__':
    print(f'prawdziwa nazwa klasy: {ClassWithRelLongName.__name__}')
    print(f"Instancja reprezentacji(dekorowana), {ClassWithRelLongName()}")
