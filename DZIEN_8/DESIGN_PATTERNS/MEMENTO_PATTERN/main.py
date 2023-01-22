from filewriterutility import FileWriterUtitlity
from filewritercaretaker import FileWriterCaretaker

if __name__ == '__main__':
    caretaker = FileWriterCaretaker()
    writer = FileWriterUtitlity("mojedane.txt")
    #zapis danych do pliku z zużyciem obiektu writer

    writer.write("Pierwsza wersja moich danych!\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    #ponowny zapis z użyciem writera
    writer.write("Druga wersja moich danych!\n")

    print(writer.content + "\n\n")

    caretaker.undo(writer)
    print(writer.content+'\n\n')
