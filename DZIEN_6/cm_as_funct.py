from contextlib import contextmanager

@contextmanager
def context_illustration():
    print("wprowadzenie kontekstu")
    try:
        yield
    except Exception as e:
        print('opuszczanie kontekstu')
        print(f' - z błędem: {e}')
        raise
    else:
        print('opuszczanie kontekstu bez błędu')

if __name__ == '__main__':
    
    print("Uruchomienie procesu ContextManagera funkcyjnego...[bez błędu]")
    with context_illustration():
        print(">> wewnątrz kontekstu")
    print()

    print("Uruchomienie procesu ContextManagera funkcyjnego...[z błędem]")
    try:
        with context_illustration():
            print(">> wewnątrz drugiego kontekstu")
            raise RuntimeError("Wyjątek wewnątrz CM")
    except RuntimeError:
        pass
