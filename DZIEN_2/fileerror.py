import sys

try:
    f = open("waznedane.txt","r",encoding="utf-8")
    s = f.readline()
    i = int(s.strip())
    raise Exception(d=i/0)
    #d = i/0
except  OSError as err:
    print(f"błąd systemowy: {err}")
    g = open("waznedane.txt","w",encoding="utf-8")
    g.write("     gjrgjkj    ")
    g.close()
    print("nie było pliku, ale już jest!!!")
except ValueError:
    print("nie można przekonwertować danych ze str do int!")
except Exception as exc:
    print(f"klasa błędu: {type(exc)}")
    print(exc.args)
    print(exc)
except:
    print(f"Ogólny błąd: {sys.exc_info()[0]}")
