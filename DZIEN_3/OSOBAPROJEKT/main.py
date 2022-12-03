from osoba import Osoba


za = 8
print("______________ nowa osoba ________________")
os1 = Osoba("Jan",36,99,173)
os1.print_osoba()
print(f"wiek za {za} lat: {os1.wiek_za_x_lat(za)}")
print(f"czy osoba jest pracownikiem? ({os1.czypracownik()})")
