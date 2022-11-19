wiek = 37
miasto = "Lublin"
imie = "Olga"
kolor_oczu = "niebieskie"
#dodatkowe dane
wydzial="Automatyka, Elektronika i Informatyka"
kierunek = "Informatyka"
uczelnia = "Politechnika Śląska"
miasto_u = "Gliwice"

osoba = "dane osoby -> imię: {}, kolor_oczu: {}, wiek: {}, miasto: {}."
student = f"dane studenta -> imię: {imie}, wiek: {wiek}, uczelnia: {uczelnia}, wydział: {wydzial}, kierunek: {kierunek}," \
          f"miasto: {miasto_u}"

print(osoba.format(imie,kolor_oczu,wiek,miasto))
print(student)

id = 'abc01'
wart = 1.64346754675

formatowanie =  '%-30s = %.2f' %(id,wart)
print(formatowanie)

owoce = [
    ('awokado',6.99),
    ('jabłko',3.56),
    ('banan',4.99),
    ('mandarynka',9.88),
    ('winogrono',12.55)
]

eo = enumerate(owoce)
print(list(eo))

print("*********** CENNIK OWOCÓW ********************")
for i,(nazwa,cena) in enumerate(owoce):
    print('#%d: %-10s = %6.2f' %(i,nazwa,cena))


print("*********** CENNIK OWOCÓW INACZEJ ********************")
for i,(nazwa,cena) in enumerate(owoce):
    print('#%d: %-10s = %6.2f' %(
        i+1,
        nazwa.title(),
        round(cena,1)
    ))
