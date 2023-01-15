nazwa_classic = ['samolot','mecz','miecz','Mieczysław','Konrad','wół',"Wisła","piorun","macierz","zenit","akronim","łódź","Łódź"]

def bsort_classic(a):
    for _ in range(len(a)):
        for i in range(1,len(a)):
            if a[i].lower() < a[i-1].lower():
                temp = a[i]
                a[i] = a[i-1]
                a[i-1] = temp


bsort_classic(nazwa_classic)
print(nazwa_classic)


nazwa_modern = ['samolot','mecz','miecz','Mieczysław','Konrad','wół',"Wisła","piorun","macierz","zenit","akronim"]

def bsort_modern(a):
    for _ in range(len(a)):
        for i in range(1,len(a)):
            if a[i].lower() < a[i-1].lower():
                a[i-1],a[i] = a[i],a[i-1]


bsort_modern(nazwa_modern)
print(nazwa_modern)

nb = [45,7,2,34,67,89]

nb[0],nb[1],nb[2],nb[5] = nb[2],nb[5],nb[1],nb[0]

print(nb)
