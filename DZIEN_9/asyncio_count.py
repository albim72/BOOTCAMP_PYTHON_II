import time

def count():
    print("Jeden")
    time.sleep(1)
    print("Dwa")

def main():
    for _ in range(3):
        count()
        
        


if __name__ == '__main__':
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} wykonany w {elapsed:0.2f} s.")
