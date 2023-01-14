from collections import OrderedDict,defaultdict,ChainMap

print("_____________ OrderedDict_____________")
print("To jest słownik (dict):\n")
d= {}
d['id']=4
d['nazwa']='czerwony'
d['paleta']='Base'

for key,value in d.items():
    print(f'{key}: {value}')


print("\nTo jest OrderedDict:\n")
od = OrderedDict()
od['id']=4
od['nazwa']='czerwony'
od['paleta']='Base'
print("przed zmianą:")
for key,value in od.items():
    print(f'{key}: {value}')

od.pop('id')
od['id']=66
print("\npo zmianie:\n")
for key,value in od.items():
    print(f'{key}: {value}')

print("_____________ defaultdict_____________")

d = defaultdict(int)
liczba = [1,3,4,5,7,2,3,1]
for i in liczba:
    d[i] += 1
print(d)

print("_____________ ChainMap_____________")

d1 = {'a':3,'b':7}
d2 = {'c':12,'d':2}
d3 = {'e':8,'f':9}

c = ChainMap(d1,d2,d3)

print(c)
print(c['a'])
print(c.values())
print(c.keys())
print(c.items())

d4 = {'n':8,'m':9,'k':7}
c2 = c.new_child(d4)

print("_________klucze_________")
for x in c2.keys():
    print(x)
print("_________wartości_________")
for y in c2.values():
    print(y)
print("_________pary_________")
for x,y in c2.items():
    print(f'{x}: {y}')

