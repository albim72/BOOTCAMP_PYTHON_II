# -*- coding: utf-8 -*-

# -- Sheet --

import numpy as np

np.zeros(6)

ar = np.ones(9)
print(ar)

np.empty(8)

u=np.arange(1,77,3)
print(u)

h = [4,8,99,1,3,55,3]
print(type(h))
print(type(u))

k = np.linspace(0,10,num=5)
print(k)

mlista = np.array([45,7,89,7,5,4,22,34])
print(mlista)
print(type(mlista))

dlista = np.array(h)
print(dlista)
print(type(dlista))

kl = (9,4,5,2,44,5,7)
npk = np.array(kl)
print(npk)

zb = {5,3,2,44,6,7,7,8,7}
zbk = np.array(zb)
print(zbk)
print(type(zbk))

nb = [45,7,8,3,1,35,77,-99,0,12,112,-654,1235]
nnb = np.array(nb)
print(nnb)

nb.sort()
nb

nnb.sort()
nnb

a=np.array([1,5,8,11])
b=np.array([2,5,9,13])
c=np.array([56,99])
big = np.concatenate((a,b,c))
print(big)

#twrzorzenie macierzy
x = np.array([[3,4],[19,6]])
print(x)

y = np.array([[7,11],[45,2]])
print(y)
zx = [[3,4],[19,6]]
print(zx)

p = np.concatenate((x,y),axis=0)
print(p)

prosta = np.arange(12)
print(prosta)

pp = prosta.reshape(3,4)
print(pp)

fp = pp.reshape(12)
print(fp)

ar = np.array([1,6,78,9,112,7,80,-5,12,34,55,67,89])
print(ar.shape)

print(ar[:4])

print(ar[5:])

print(ar[3:7])

w = np.array([[1,2,3,4],[99,34,56,77],[21,13,14,35]])
print(w)

print(w[w<5])

pc = (w>=5)
print(w[pc])

pv = (w%2==0)
print(w[pv])

c = w[(w>2)&(w<21)]
print(c)

s = w[(w<8)|(w>50)]
print(s)

dane = np.array([1,3,8])
ones = np.ones(3,dtype=int)
tw = np.array([2,2,3])

print(dane+ones)

print(dane-ones)

print(dane*tw)

print(dane/tw)

tab = np.array([[1,6],[27,19]])
print(tab)

print(tab.sum(axis=0))
print(tab.sum(axis=1))

print(tab*1.896)

print(tab.max())
print(tab.min())
print(tab.mean())

