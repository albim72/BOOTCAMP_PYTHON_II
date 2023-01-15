nr_dnia = 12

match nr_dnia:
    case 1:
        print("Poniedziałek")
    case 2:
        print("Wtorek")
    case 3:
        print("Środa")
    case 4:
        print("Czwartek")
    case 5:
        print("Piątek")
    case 6:
        print("Sobota")
    case 7:
        print("Niedziela")
    case _:
        print("niewłaściwa wartość")
