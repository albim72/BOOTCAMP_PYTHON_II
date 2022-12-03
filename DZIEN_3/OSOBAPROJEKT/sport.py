class Sport:
    def __init__(self,dysycyplina,lataupr,zyciowka):
        self.dysycyplina = dysycyplina
        self.lataupr = lataupr
        self.zyciowka = zyciowka
        
    def infosport(self):
        print(f'dyscyplina: {self.dysycyplina},lata uprawiania: {self.lataupr},'
              f'życiówka: {self.zyciowka}')
