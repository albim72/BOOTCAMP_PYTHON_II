def dzielenie(x,y):
    try:
        wynik = x/y
    except ZeroDivisionError:
        print("dzielenie przez 0")
    except NameError:
        print("brak danych")
    except TypeError:
        print("nie dziel używając tekstu!!!")
    else:
        print(f"wynik dzielenia: {wynik}")
    finally:
        print("policzmy coś jeszcze!!!")

try:
    dzielenie(6,7)
    dzielenie(6,0)
    dzielenie(0,0)
    dzielenie(0.00056,712)
    dzielenie(1566,True)
    dzielenie(-0.009,False)
    dzielenie("sggssd",56)
    dzielenie(3)
except TypeError:
    print("zbyt mała liczba argumentów -> podaj dwa argumety: x,y")
