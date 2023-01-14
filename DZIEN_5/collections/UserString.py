from collections import UserString

class MyString(UserString):
    def append(self,s):
        self.data+=s

    def remove(self,s):
        self.data = self.data.replace(s,"")


s1 = MyString("Biegi ultra")
print(f'ciąg oryginalny: {s1.data}')

s1.append(' w górach.')
print(f'ciąg po zmianie: {s1.data}')

s1.remove(' ultra')
print(f'ciąg po zmianie: {s1.data}')

s2 = MyString('hehehehehehehe ale ubaw')
s2.remove('h')
print(s2.data)
