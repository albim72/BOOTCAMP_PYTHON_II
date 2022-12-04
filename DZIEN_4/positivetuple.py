#krotka jest reprezentowana przez klasę o nazwie: tuple
#napisz własną klasę która będzie służyła do tworzenia krotek na podstawie zadanych struktur danych 
#w taki sposób że nowa krotka przechwyci tylko wartości dodatnie lub równe 0
#wartości odrzycone zliczy odpowiednim counterem i wyświetli

class PositiveNumberTuple(tuple):
    def __new__(cls, *numbers):
        skipped_negative = 0
        positive_numbers = []
        for x in numbers:
            if x >= 0:
                positive_numbers.append(x)
            else:
                skipped_negative += 1
                
        instance = super().__new__(cls,tuple(positive_numbers))
        instance.skipped_negative = skipped_negative
        return instance
    
pos = PositiveNumberTuple(-4,7,12,34,505,0,-67,-89,-34,-555,122,1,7)
