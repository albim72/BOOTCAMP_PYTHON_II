print((lambda k: k + 3)(5))
b = lambda u: u * 6
print(b(8))

def policz(u):
    return u*6
print(policz(7))

y = lambda a,b,c=8:a*c-b
print(y(5,6,7))
print(y(5,6))

def multi(n):
    return lambda a:a*n

print(multi(7)(9))

liczby = [2*i+43 for i in range(10000) if i%2==0]
print(liczby)

nb = [45,55,56,7,8,2,3,5,7,10,0,-11,-90,100,1001,-8]

#stwórz listę nparz i przekaż do niej wszystkie wartości parzyste z listy nb
#użyj funkcji standardowej filter -> gdzie pierwszym parameterm filter jest funkcja definiująca warunek
#filtrowania, drugi parametr to źródło danych

nparz = list(filter(lambda x:x%2==0,nb))
print(nparz)

def warunek(x):
    return x%2==0

nparz2 = list(filter(warunek,nb))
print(nparz2)
