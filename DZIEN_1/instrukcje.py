a = 1
b = 1

if a>b:
    print("a jest większe niż b")
elif a==1 & b==1:
    print("a = 1 i b = 1")
elif a==b:
    print("a jest rowne b")
else:
    print("a jest mniejsze niż b")

kolor = "zółty"

match kolor:
    case "czarny":
        print("twój wybór to czarna koszulka")
    case "zielony":
        print("twój wybór to zielony kapelusz")
    case "czerwony":
        print("twój wybór to czerwony płaszcz")
    case _:
        print("nie ma ciuchów w taakim kolorze!")
