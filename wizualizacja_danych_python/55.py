class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


tomasz = Pracownik("tomasz", "tomaszynski", 342332)
bartosz = Menadzer("bartosz", "bartoszewski", 3234342234)
print(isinstance(tomasz, Menadzer))
print(isinstance(tomasz, Pracownik))
print(isinstance(tomasz, Osoba))
print(isinstance(bartosz, Menadzer))
print(isinstance(bartosz, Pracownik))
print(isinstance(bartosz, Osoba))
print(issubclass(Osoba, Menadzer))
print(issubclass(Osoba, Pracownik))
print(issubclass(Osoba, Osoba))
print(issubclass(Menadzer, Menadzer))
print(issubclass(Menadzer, Pracownik))
print(issubclass(Menadzer, Osoba))
print(issubclass(Pracownik, Menadzer))
print(issubclass(Pracownik, Pracownik))
print(issubclass(Pracownik, Osoba))