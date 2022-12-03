#przykład 1
def liczby():
    for i in range(19):
        yield i


for p in liczby():
    print(p)

#przykład 2

def wznowienie(n,k):
    print("wstrzymanie działania...")
    yield 1001
    print("wznowienie działania....")

    print("wstrzymanie działania...")
    yield n+k
    print("wznowienie działania....")

    print("wstrzymanie działania...")
    yield n-k
    print("wznowienie działania....")

    print("wstrzymanie działania...")
    yield n*k
    print("wznowienie działania....")

    print("wstrzymanie działania...")
    yield n/k
    print("wznowienie działania....")
    #return n*8+10*k

for i in wznowienie(7,8):
    print(f'zwrócono wartość: {i}')

