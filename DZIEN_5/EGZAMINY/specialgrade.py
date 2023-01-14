from weakref import WeakKeyDictionary

class Grade:
    def __init__(self):
        self._value = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self._value.get(instance,0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError('ocena musi być wartością z przedziału: 0-100')
        self._value[instance] = value


class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()
