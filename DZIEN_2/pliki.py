import os

print("_________ czytanie zawartości pliku za pomocą readline() ____________")
f = open("dane.txt","r",encoding="utf-8")
print(f.readline(),end="")
print(f.readline(),end="")
print(f.readline(),end="")
print(f.readline())
f.close()

print("\n_________ czytanie zawartości pliku za pomocą read() ____________")
f = open("dane.txt","r",encoding="utf-8")
print(f.read())
f.close()

print("\n_________ czytanie zawartości pliku za pomocą pętli for ____________")
f = open("dane.txt","r",encoding="utf-8")
for linia in f:
    print(linia, end="")
f.close()

print("\n_________ tworzenie nowego pliku ____________")
f = open("message.txt","a",encoding="utf-8")
f.write("to jest ważna informacja\n")
f.close()

f = open("message.txt","r",encoding="utf-8")
print(f.read())
f.close()

if os.path.exists("message.txt"):
    os.remove("message.txt")
    print("plik został usunięty!")
else:
    print("plik nie istnieje!")
    
