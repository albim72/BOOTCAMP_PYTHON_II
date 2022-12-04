#vanilla method
class Count:
    def __init__(self,count):
        self._count = count
    def __add__(self, other):
        total_count = self._count + other._count
        return Count(total_count)
    def __str__(self):
        return 'Count: % i' %self._count

c1 = Count(2)
c2 = Count(5)
c3 = c1+c2
print(c3)
