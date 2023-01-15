def fibonacci():
    a,b=0,1

    while True:
        yield b
        a,b = b, a+b

if __name__ == '__main__':
    fib = fibonacci()
    print(f"typ funkcji fibonacciego: {type(fib)}")
    print(f"pierwszych 10 liczb fibonacciego: {[next(fib) for _ in range(10)]}")
    print(f"następnych 10 liczb fibonacciego: {[next(fib) for _ in range(10)]}")
    print(f"kolejne 10 liczb fibonacciego: {[next(fib) for _ in range(10)]}")
