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
