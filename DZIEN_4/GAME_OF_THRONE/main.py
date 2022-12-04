from tywin import Tywin
from tyrion import Tyrion
from cersei import Cersei

tyw = Tywin("Lannister","Lord","m",8,6,9)
tyr = Tyrion("Lannister","Lord","m",6,9,10)
cer = Cersei("Lannister","Królowa","k",4,9,9)

print(f"___________ {tyw.get_tytul()} {tyw.__class__.__name__} ____________")
tyw.walka()
tyw.negocjacja()
tyw.uczta()

print(f"___________ {tyr.get_tytul()} {tyr.__class__.__name__} ____________")
tyr.walka()
tyr.negocjacja()
tyr.uczta()

print(f"___________ {cer.get_tytul()} {cer.__class__.__name__} ____________")
cer.walka()
cer.negocjacja()
cer.uczta()
