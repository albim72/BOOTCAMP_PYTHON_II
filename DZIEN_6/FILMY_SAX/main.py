import xml.sax

class UchwytFilmu(xml.sax.ContentHandler):
    
    def __init__(self):
        self.CurrentData = ""
        self.id = ""
        self.tytul = ""
        self.rok = ""
        self.kraj = ""
        self.czas_t = ""
        self.gatunek = ""
        
    def startElement(self,tag,attributes):
        self.CurrentData = tag
        if tag == "film":
            print("_____________ FILM _________________")
            
    def endElement(self,tag):
        if self.CurrentData == "id_filmu":
            print(f'identyfikator filmu: {self.id}')
        elif self.CurrentData == "tytul":
            print(f'tytuł filmu: {self.tytul}')
        elif self.CurrentData == "rok":
            print(f'rok produkcji filmu: {self.rok}')
        elif self.CurrentData == "kraj":
            print(f'kraj produkcji filmu: {self.kraj}')
        elif self.CurrentData == "czas_trwania":
            print(f'czas trwania filmu: {self.czas_t}')
        elif self.CurrentData == "gaatunek":
            print(f'gatunek filmu: {self.gatunek}')
