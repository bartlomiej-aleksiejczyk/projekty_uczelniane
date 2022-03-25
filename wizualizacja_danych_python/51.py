class Atrybuty:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj= rodzaj
        self.dlugosc=dlugosc
        self.szerokosc=szerokosc

    def wyświetl_nazwę(self):
        return self.__class__.__name__

class Ubrania(Atrybuty):
    rozmiar="sdsdfs"
    kolor="ddfsdf"
    dla_kogo ="sdsfsdf"
    def wyświetl_dane(self):
        return(self.rozmiar,self.kolor, self.dla_kogo,self.rodzaj)

class Sweter(Ubrania):
    rodzaj="test"
    def wyświetl_dane(self):
        return(self.rozmiar,self.kolor, self.dla_kogo,self.rodzaj)
kardigan= Sweter("oficjanle", "dlugi","szeroki")
print(kardigan.wyświetl_nazwę())
print(kardigan.wyświetl_dane())
kardigan= Sweter("formalny", "sredni","turewcki")
print(kardigan.wyświetl_nazwę())
print(kardigan.wyświetl_dane())
kardigan= Sweter("nieformalny", "krotki","golf")
print(kardigan.wyświetl_nazwę())
print(kardigan.wyświetl_dane())
