#funkcja kwota(transport,nocleg_wyzywienie,wycieczki,ubezpieczenie,inne,rabat) ->
#--> (transport+nocleg_wyzywienie)*(1-rabat)+wycieczki+ubezpieczenie+inne

def kwota(t,nw,w,u,i,rab=0):
    return (nw+t)*(1-rab/100)+w+u+i

print("kwota do zapłaty",kwota(100,100,50,50,50),"zł")
print("kwota do zapłaty",kwota(100,100,50,50,50,25),"zł")
print("kwota do zapłaty",kwota(100,100,50,50,50,75),"zł")
