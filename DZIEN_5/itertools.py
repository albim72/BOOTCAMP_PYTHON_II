import itertools

#przypadek1
#operator nieskończony
for i in itertools.count(5,5):
    if i == 145:
        break
    else:
        print(f"i wynosi: {i}")

#przypadek2 -> cykle
count = 0
for i in itertools.cycle('AB'):
    if count > 6:
        break
    else:
        print(f'i={i}')
        count += 1

#przypadek3
zawody = ['trening','siła','pływanie','podbiegi','dieta']
iterators = itertools.cycle(zawody)
for i in range(13):
    print(next(iterators),end="  ")

#przypadek4

print("wyświetlanie wartości liczbowych..")
print(list(itertools.repeat(25,4)))

print("wyświetlanie iloczynu kartezjańskiego")
print(list(itertools.product([1,2],repeat=2)))

print("wyświetlanie iloczynu kartezjańskiego kontenerów: ")
print(list(itertools.product(['trening','siła','pływanie','podbiegi','dieta'],['2','3'],repeat=2)))

#przypadek5

print("permutacje")
print(list(itertools.permutations([1,'Kraków',55],3)))

print("kombinacje")
print(list(itertools.combinations('ABC',2)))
