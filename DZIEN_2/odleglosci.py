def policz_odl_1(metry, jedn):
	if jedn == 1:
		return f"odległość wynosi: {round(metry / 1852, 2)} -> miara: mila morska"
	elif jedn == 2:
		return f"odległość wynosi: {round(metry / 1609.344, 2)} -> miara: mila lądowa"
	elif jedn == 3:
		return f"odległość wynosi: {round(metry / 0.9144, 2)} -> miara: jard"
	elif jedn == 4:
		return f"odległość wynosi: {round(metry / 0.30477, 2)} -> miara: stopa"
	elif jedn == 5:
		return f"odległość wynosi: {round(metry / 0.0254, 2)} -> miara: cal"
	else:
		return "nie ma takiej miary"


miary = {
	1: [1852, "mila morska"],
	2: [1609.344, "mila lądowa"],
	3: [0.9144, "jard"],
	4: [0.30477, "stopa"],
	5: [0.0254, "cal"]
}

def policz_odl_2(metry, jedn):
	return f"odległość wynosi: {round(metry / miary[jedn][0], 2)} -> miara: {miary[jedn][1]}"

m = float (input ("Podaj odległość w metrach: "))
j = int (input ("Podaj miarę: 1- mila morska, 2 - mila lądowa, "
                "3 - jard, 4 - stopa, 5 - cal: "))
print (f"warunkowo: {policz_odl_1 (m, j)}")
print (f"słownikowo: {policz_odl_2 (m, j)}")


