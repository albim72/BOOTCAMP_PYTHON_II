#funkcja nr 1
def witaj():
    print("witaj nowy użytkowniku")
    print("opłać abonament")
    print("zaloguj się")

witaj()
witaj()

# for _ in range(255):
#     witaj()

# for i in range(0,255,5):
#     print(f"___________ wywołanie nr {i+1} ____________")
#     witaj()

#funkcja nr 2

def obywatel(nrtelefonu,kraj="Polska"):
    print(f"kraj pochodzenia: {kraj}, numer telefonu: {nrtelefonu}.")

obywatel(53453453,"Turcja")
obywatel(563634656,"USA")
obywatel(876876867,"Chiny")
obywatel(423465656,"Norwegia")
obywatel(98756565)

#funkcja nr 3
def pt(n):
    return n**3

def oblicz(a:int,b:int,x:int) -> int:
    __fm = (a+b)*x + pt(b)
    return __fm

print(oblicz(3,6,2))
print(oblicz(6.88,-1.7,22))
print(pt(5))
print(oblicz(True,True,True))

#funkcja nr 4
def miasta(miasto3,miasto2="Rzeszów",miasto1="Kraków",miesiąc="styczeń"):
    print(f"miesiąc zestawienia: {miesiąc} -- miasto miesiąca: {miasto1}, "
          f"drugie miejsce: {miasto2}, trzecie miejsce: {miasto3}")


miasta("Toruń","Kielce","Gdynia")
miasta("Toruń","Kielce")
miasta("Toruń")
#wpisz maisto3 oraz miasto1, pozostaw domyślne miasto Rzeszów

miasta("Zamość",miasto1="Wrocław",miesiąc="luty")


