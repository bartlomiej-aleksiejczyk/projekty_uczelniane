class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyświetl_produkt(self):
        return self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed
    def ile_produktu(self):
        tekst =0
        tekst +=self.ilosc
        tekst = str(tekst)
        tekst +=" "
        tekst +=self.jednostka_miary
        return tekst
    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

sledz = NaZakupy("sledz",2,"kg",5)
print(sledz.ile_produktu())
print(sledz.ile_kosztuje())
print(sledz.wyświetl_produkt())
