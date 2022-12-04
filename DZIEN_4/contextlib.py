import contextlib

@contextlib.contextmanager
def context_manager(n):
    print("wejście...")
    yield n*2+1
    print("wyjście...")



with context_manager(45) as cm:
    print(f"wartość cm wynosi: {cm}")
    
