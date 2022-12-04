class Basic:
    def __init__(self):
        print("obiekt został utworzony...")

    def __call__(self,a,b):
        print("instancja jest wywołana przez funkcję specjalną  __call__")
        print(a*b)

fn = Basic()
fn(19,34)
