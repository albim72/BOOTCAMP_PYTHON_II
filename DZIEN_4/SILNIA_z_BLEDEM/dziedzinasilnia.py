class DziedzinaSilnia(Exception):
    def __init__(self,n):
        self.n = n

    def __str__(self):
        return f"wartość n = {self.n} jest poza zakresem dziedziny funckji silnia. Zakres ten to liczby większe " \
               f"lub równe 0"
