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

#instrukcja iteracyjna -> pętla

i=1
while i<=6:
    print(i)
    if i==4:
        break
    i+=1
else:
    print("ostatecznie i wynosi:",i)

owoce = ["jabłko","banan","kiwi","malina","pomarańcza"]

print(owoce)
print("___________lista owoców___________________")
for owoc in owoce:
    print(owoc)

cechy = ["kolorowy","elegancki","brudny","kosztowny","obdrapany"]
obiekty = ["smaochód","budynek","płaszcz","przystanek","kapelusz"]


for ch in cechy:
    for ob in obiekty:
        print(ch,ob)



