from oldresistor import OldResistor


r0 = OldResistor(10.2E2)
print(f"______________ {r0.__class__.__name__} _______________")
print(r0)
print(r0._ohms)
r0.set_ohms(2.34E3)
print(r0.get_ohms())
