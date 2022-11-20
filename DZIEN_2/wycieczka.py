#funkcja kwota(transport,nocleg_wyzywienie,wycieczki,ubezpieczenie,inne,rabat) ->
#--> (transport+nocleg_wyzywienie)*(1-rabat)+wycieczki+ubezpieczenie+inne

def kwota(t,nw,w,u,i,rab=0):
    if rab >= 0 and rab <= 35:
        return (nw + t) * (1 - rab / 100) + w + u + i
    else:
        return "podaj rabat mniejszy niż 36% lub większy od 0"

print("kwota do zapłaty",kwota(100,100,50,50,50),"zł")
print("kwota do zapłaty",kwota(100,100,50,50,50,25),"zł")
print("kwota do zapłaty",kwota(100,100,50,50,50,75),"zł")

#przbuduj funkcję kwota tak aby przyjmowała tylko rabat w zakresie <1,35>
