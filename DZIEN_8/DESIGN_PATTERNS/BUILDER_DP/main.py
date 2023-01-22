from builder import Builder
from director import Director
from concretebuilder1 import ConcreteBulider1

director = Director()
builder = ConcreteBulider1()
director.builder = builder

print("Produkt podstawowy:")
director.build_minial_variable_product()
builder.product.list_parts()

print("\n")

print("Produkt pełny:")
director.build_full_featured_product()
builder.product.list_parts()

print("\n")

print("Produkt - wersja użytkownika:")
builder.produce_part_a()
builder.produce_part_c()
builder.product.list_parts()
