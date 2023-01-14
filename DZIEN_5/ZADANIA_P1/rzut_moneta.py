# importujemy potrzebne biblioteki

import random
import time

# ustawiamy początkowy wynik dla użytkownika oraz komputera
user = 0
computer = 0

while True:

    # wczytujemy wybór uzytkownika
    x = input("podaj 0 - koniec gry, o - orzeł, r -reszka: ")
    if x == '0':
        break
    elif x == 'o':
        x = "orzeł"
    elif x == 'r':
        x = "reszka"
    else:
        print("Proszę dokonać prawidłowego wyboru:")
        print("o - orzeł")
        print("r - reszka")
        print("0 - zakończenie gry")

        # jezeli użytkownik nie wybrał ani, o, r, 0, to wróć do początku wykonywania pętli
        continue

    # rzucamy monetą
    y = random.choice(["orzeł", "reszka"])

    # Odliczamy 3,2,1
    for i in range(0, 3):
        print(3 - i)
        time.sleep(1)

    print("Wynik rzutu: ", y)

    # sprawdzamy kto wygrał
    if x == y:
        user += 1
    else:
        computer += 1

    # Drukujemy podsumowanie
    print("Wyniki łacznie.")
    print("Użytkownik: ", user)
    print("Komputer: ", computer)

