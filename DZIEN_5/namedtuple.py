from collections import namedtuple

Student = namedtuple('Student',['firstname','lastname','age','nb'])

s = Student('Adrian','Kot',23,3435)

print(s)
print(f"nr indeksu studenta: {s[3]}")
print(f"imię studenta: {s.firstname}")
print(f"Wiek studenta: {getattr(s,'age')} lat/a")

s2 = ['Benek','Nowik',21,45455]
s3 = {'firstname':'Paweł','lastname':'Kloc','age':34,'nb':355656}
print(f"Nazwana krotka utworzona na podstawie listy: {Student._make(s2)}")
print(f"Nazwana krotka utworzona na podstawie słownika: {Student(**s3)}")
print(f"wszystkie pola krotki: {s._fields} ")
print(s._replace(firstname="Adam"))
print(s)
