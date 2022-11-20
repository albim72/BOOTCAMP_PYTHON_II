a=45
b=7
print("To jest wartość a = ", end=" ")
print(a,end="")
print(", to jest druga wartość b =",end=" ")
print(b)

mecz = "mecz miesiąca\nklub sportowy: \"Orły Wisła\" - \tTrener: Jan Kot\nlokalizacja: Janowo\n" \
       "vs\nklub sportowy: \"Strome Wzgórza KS\" - \tTrener: Adam Nowak\nlokalizacja: Strome Wzgórza\n"

print(mecz)

str_ = "        niezwykle ważna i Tajna wiadomość        ; ERT6556566454;        zaszyfrowana przez Aden Knot;" \
       "i równie Tajna pRzEsYłKA"

print(str_.upper())
print(str_.lower())
print(str_.strip())
print(str_.replace("Tajna","Utajniona"))
txt = str_.split(";")
print(type(txt))
print(txt)

for i,k in enumerate(txt):
       txt[i] = k.strip()

print(txt)

print(str_.find("Tajna"))

# for _ in str_:
#        print(str_.find("Tajna"))

print(str_.endswith("ka"))
print(str_.endswith("KA"))

d = "pionierzy"
e = "10023"
print(d.isalpha())
print(e.isdigit())
t=99
print(str(t).isdigit())

