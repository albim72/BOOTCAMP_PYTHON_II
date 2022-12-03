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

#dekorator pobierający nazwę wykonywanej funkcji

def debug(funkcja):
    def wrapper(*args,**kwargs):
        print(f'wołana funkcja to: {funkcja.__name__}')
        funkcja(*args)
    return wrapper

@debug
def info(i):
    print(f'informacja: {i}')

info("nr 4645869548694856945")

#dekorator typu repeater

def repeater(n):
    def wrapper(funkcja):
        def inner(*args):
            for i in range(n):
                funkcja(*args)
        return inner
    return wrapper

@repeater(n=5)
def komunikat(k,n):
    print(f'ważny komunikat: {k}, numer: {n}')

komunikat("idzie zima",67)
komunikat("Tomasz Tomaszewski",101)
