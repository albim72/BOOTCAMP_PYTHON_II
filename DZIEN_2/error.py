try:
    # x=1
    print(x)
except NameError:
    print("x nie istnieje!")
except:
    print("nieokreślony błąd!")
else:
    print(f"wartość y = {2*x}")
finally:
    print("to jest ostatni krok.....")

print("ciąg dalszy programu...")
