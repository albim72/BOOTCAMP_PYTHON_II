#vanilla method
class Count:
    def __init__(self,count):
        self._count = count
    def __add__(self, other):
        total_count = self._count + other._count
        return Count(total_count)
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)
    def __str__(self):
        return 'Count: % i' %self._count

c2 = Count(5)
c3 = 0+c2
print(c3)

