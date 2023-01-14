from collections import Counter

litery = ['B','A','B','C','B','C','B','A','B','C','B','C','B','A','B','C','B','C','B','A','B','C','B','C']
print(Counter(litery))

literydict = {'X':34,'Y':111,'Z':2}
print(Counter(literydict))

print(Counter(D=4,F=8,G=10,E=12))

print("____update_____")
cn = Counter()

nb_1 = [1,3,5,2,1,2,3,4,1,2]
nb_2 = [1,5,7,2,9]

cn.update(nb_1)
print(cn)
cn.update(nb_2)
print(cn)

print('_____różnica____')

c1 = Counter(A=4,B=3,C=10)
c2 = Counter(A=10,B=3,C=4)

c1.subtract(c2)
print(c1)

z = ['blue','red','yellow','blue','blue','red','yellow','blue','blue','red','yellow','blue']
print(Counter(z))
