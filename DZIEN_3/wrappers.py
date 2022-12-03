import math
import time

def pomiarczasu(funkcja):
    def wrapper():
        starttime = time.perf_counter()
        funkcja()
        endtime = time.perf_counter()
        print(f"czas wykonania funckji: {endtime-starttime} s")
    return wrapper

def sleep(funkcja):
    def wrapper():
        time.sleep(4)
        return funkcja()
    return wrapper

@pomiarczasu
@sleep
def big_lista():
    sum([i**18 for i in range(1000000)])

big_lista()

lt = [i**18 for i in range(1000000)]
@pomiarczasu
def szybszaopcja():
    sum(lt)

szybszaopcja()

