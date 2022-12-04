class MojaUsterka(Exception):
    def __init__(self,*args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print("wysłanie kounikatu błędu przez __str__")
        if self.message:
            return f'{self.__class__.__name__} -> {self.message}'
        else:
            return f'{self.__class__.__name__} została użyta'

try:
    raise MojaUsterka('mamy duży problem.....')
except MojaUsterka as mu:
    print(mu)
