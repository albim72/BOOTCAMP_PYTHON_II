import autobus

strg_ = repr(autobus.__doc__)
print(strg_)

f = open("autobus.txt","a",encoding="utf-8")
f.write(strg_)
f.close()
