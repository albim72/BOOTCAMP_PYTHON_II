drzewa = {"buk","jodła","dąb","jesion","baobab","jabłoń","buk"}
print(drzewa)
print(drzewa)
print(drzewa)

for d in drzewa:
    print(d)

print("osika" in drzewa)
drzewa.add("osika")
print(drzewa)

las = ["świerk","topola","brzoza","olszyna"]
drzewa.update(las)

print(drzewa)

liczby = [34,0,3,4,1,3,4,5,67,8,9,2,3,4,3,8,9,67,7,8,2,3,1,4,5,1,2,3,4]

liczby = list(set(liczby))
liczby.sort()
print(liczby)

frozen_liczby = frozenset(liczby)
print(frozen_liczby)
print(type(frozen_liczby))

drzewa.remove("osika")
print(drzewa)

drzewa.discard("jojoba")
print(drzewa)

drzewa.discard("dąb")
print(drzewa)


dzialka = {"jesion","sosna","brzoza","klon"}

print(drzewa.intersection(dzialka))


print(drzewa.difference(dzialka))
print(dzialka.difference(drzewa))
print(drzewa.issubset(dzialka))
print(dzialka.issubset(drzewa))

park = {"brzoza","klon"}

print(park.issubset(dzialka))
print(dzialka.issubset(park))
