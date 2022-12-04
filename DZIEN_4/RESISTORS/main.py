from oldresistor import OldResistor
from resistor import Resistor


r0 = OldResistor(10.2E2)
print(f"______________ {r0.__class__.__name__} _______________")
print(r0)
print(r0._ohms)
r0.set_ohms(2.34E3)
print(r0.get_ohms())

r1 = Resistor(3.33E2)
print(f"______________ {r1.__class__.__name__} _______________")
r1.ohms = 9.045E3
print(f'układ elektryczny:\noporność: {r1.ohms} om\nnapięcie prądu: {r1.voltage} V,'
      f'\nnatężenie prądu: {r1.current} A')
