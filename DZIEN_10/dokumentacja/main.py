import autobus
import os

if os.path.exists("autobus.txt"):
    os.remove("autobus.txt")

strg_ = repr(autobus.__doc__)
print(strg_)

f = open("autobus.txt","a",encoding="utf-8")
f.write(strg_ + "\n")
f.close()


msg_ = repr(autobus.opis.__doc__)
print(msg_)

f = open("autobus.txt","a",encoding="utf-8")
f.write(msg_ + "\n")
f.close()

def palindrom(word):
    """Zwraca wartość True, jeśli podane słowo jest palindromem ->
    czyli słowem które pisane w obu kierunkach jest identyczne
    np. kajak"""
    return word == word[::-1]

paldoc = repr(palindrom.__doc__)
f = open("autobus.txt","a",encoding="utf-8")
f.write(paldoc + "\n")

f.close()

class Driver:
    """
    To jest klasa opisująca kierowcę.
    """
    def __init__(self,id,latapracy):
        self.id = id
        self.latapracy = latapracy

drvdoc = repr(Driver.__doc__)
f = open("autobus.txt","a",encoding="utf-8")
f.write(drvdoc + "\n")

f.close()


