import time
import asyncio

def count():
    print("Jeden")
    time.sleep(1)
    print("Dwa")

def main():
    for _ in range(3):
        count()

async def count_async():
    print("Jeden")
    await asyncio.sleep(1)
    print("Dwa")

async def main_spec():
    await asyncio.gather(count_async(),count_async(),count_async())


if __name__ == '__main__':
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} wykonany w {elapsed:0.2f} s.")

    s = time.perf_counter()
    asyncio.run(main_spec())
    elapsed = time.perf_counter() - s
    print(f"{__file__} wykonany w {elapsed:0.2f} s.")
