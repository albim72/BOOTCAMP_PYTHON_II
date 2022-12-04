#zbuduj contextmanagera, którego nazwiesz FileManager i będzie służył do szybkiej obslugi plików
#będzie dawał możliwości utworzenia nowego pliku, dopisania do niego danych, wyświetlenia i wiele innych

class FileManager:
    def __init__(self,filename,mode,encod):
        self.filename = filename
        self.mode = mode
        self.encod = encod
        self.file = None

    def __enter__(self):
        self.file = open(self.filename,self.mode,encoding=self.encod)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager('test.txt','a','utf-8') as f:
    f.write('to jest bardzo ważny test\n')

print(f.closed)

with FileManager('test.txt','r','utf-8') as f:
    print(f.read())

