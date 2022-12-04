from tywin import Tywin
from tyrion import Tyrion
from cersei import Cersei

tyw = Tywin("Lannister","m",8,6,9)
tyr = Tyrion("Lannister","m",6,9,10)
cer = Cersei("Lannister","k",4,9,9)

print("___________ lord Tywin ____________")
tyw.walka()
tyw.negocjacja()
tyw.uczta()

print("___________ lord Tyrion ____________")
tyr.walka()
tyr.negocjacja()
tyr.uczta()

print("___________ królowa Cerei ____________")
cer.walka()
cer.negocjacja()
cer.uczta()
