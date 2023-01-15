def power(values):
    for value in values:
        print(f"potęgowanie: {value}")
        yield value**2

def adder(values):
    for value in values:
        print(f"dodawanie: {value}")
        if value%2 == 0:
            yield value + 3
        else:
            yield value

if __name__ == '__main__':
    elements = list(range(5))
    print(f"procesowanie listy: {elements}")
    print(f'wynik = {list(adder(power(elements)))}')
    print()

    print(f"procesowanie listy: {list(adder(power(elements)))}")
    print(f'wynik = {list(adder(power(elements)))}')
    print()

