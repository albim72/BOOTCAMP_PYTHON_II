class ContextIllustration:
    def __enter__(self):
        print("*wprowadzenie kontekstu")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("*opuszczenie kontekstu")
        if exc_type is None:
            print("* wyjście bez błędów...")
        else:
            print(f"* wyjście z błędem: {exc_val}")

if __name__ == '__main__':

    print("Uruchomienie procesu ContextManagera...[bez błędu]")
    with ContextIllustration():
        print(">> wewnątrz kontekstu")
    print()

    print("Uruchomienie procesu ContextManagera...[z błędem]")
    try:
        with ContextIllustration():
            print(">> wewnątrz drugiego kontekstu")
            raise RuntimeError("Wyjątek wewnątrz CM")
    except RuntimeError:
        pass
