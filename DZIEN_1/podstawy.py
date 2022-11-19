print("to jest pierwsza aplikacja Pythona")
#zmienna i typ
"""
komentarz wieloliniowy -> dokumentacyjny
drugq linia
"""

a=45
print(a)
print(type(a))

a = "jedynka"
print(a)
print(type(a))

g:float
g=8.34
print(g)
print(type(g))

g = True
print(g)
print(type(g))

#powielenie linii -> CTR+D
#CTRL+/    zakomentowanie/odkomentowanie linii
p1 = "pora roku - jesień"
p2 = "pora roku - zima"
r = 2022

print(p1+", "+p2+",rok: "+str(r))
print(p1,p2,r,sep=", ")


y = 8
print(8*y)
ys = "68"

print(6*ys)
print(eval(ys)*6)
print(float(ys)*6)

print(type(float(ys)))
print(type(eval(ys)))

g1 = 10
g2 = 11
print(type(g1))
print(type(g2))
print(g1+g2,g1-g2,g1*g2,g1/g2,g1%g2,g1**g2,sep=" ; ")
print(type(g1/g2))

print(pow(g1,g2))
import math
print(math.sqrt(g1))
d = 8.9976555
print(round(d))
print(round(d,5))

i = 5
i+=1 #i=i+1
print(i)
i-=2
print(i)
i/=3
print(i)

s = 'lajkonik'
print(s)
print(type(s))

print(s[0])
print(s[1])
print(s[2:6])
print(s[2:])
print(s[:4])
print(s[-1])
print(s[-3])
print(s[1:4:2])
print(s[::2])
