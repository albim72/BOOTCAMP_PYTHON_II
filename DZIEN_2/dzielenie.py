def dzielenie(x,y):
    try:
        wynik = x/y
    except ZeroDivisionError:
        print("dzielenie przez 0")
    except NameError:
        print("brak danych")
    else:
        print(f"wynik dzielenia: {wynik}")
    finally:
        print("policzmy coś jeszcze!!!")
