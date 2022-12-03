from prostokat import Prostokat
from tojkat import Trojkat

pr = Prostokat(6.4,4.3)
print(f'pole figury: {pr.__class__.__name__} wynosi: {pr.policz_pole()} cm2')

tr = Trojkat(4.5,7.2)
print(f'pole figury: {tr.__class__.__name__} wynosi: {tr.policz_pole()} cm2')
