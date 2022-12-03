from prostokat import Prostokat
from tojkat import Trojkat
from trapez import Trapez
from kolo import Kolo

pr = Prostokat(6.4,4.3)
print(f'pole figury: {pr.__class__.__name__} wynosi: {pr.policz_pole():.2f} cm2')

tr = Trojkat(4.5,7.2)
print(f'pole figury: {tr.__class__.__name__} wynosi: {tr.policz_pole():.2f} cm2')

trp = Trapez(8.3,6.2,5.1)
print(f'pole figury: {trp.__class__.__name__} wynosi: {trp.policz_pole():.2f} cm2')

kl = Kolo(5.5)
print(f'pole figury: {kl.__class__.__name__} wynosi: {kl.policz_pole():.2f} cm2')
