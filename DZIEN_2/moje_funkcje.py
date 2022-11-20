def witaj():
    print("witaj nowy użytkowniku")
    print("opłać abonament")
    print("zaloguj się")

witaj()
witaj()

# for _ in range(255):
#     witaj()

for i in range(0,255,5):
    print(f"___________ wywołanie nr {i+1} ____________")
    witaj()
