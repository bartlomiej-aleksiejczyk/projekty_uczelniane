class slowa:
    lista_pomocnicza=[]
    lista_pomocnicza2=[]
    def __init__(self,slowo1,slowo2):
        self.zerowanie_se_listy()
        self.zerowanie_se_listy2()
        self.slowo1=slowo1
        self.slowo2=slowo2
    def zerowanie_se_listy(self):
        for x in range(27):
            self.lista_pomocnicza.append(0)

    def zerowanie_se_listy2(self):
        for x in range(27):
            self.lista_pomocnicza2.append(0)
    def sprawdz_czy_palindrom (self):
        self.odp1="slowo 1 jest palindromem"
        self.odp2="slowo 2 jest palindromem"
        for x in range(len(self.slowo1)):
            if self.slowo1[x-1]!=self.slowo1[-x]:
                self.odp1 = "slowo 1 nie jest palindromem"
                break
        for x in range(len(self.slowo2)):
            if self.slowo2[x-1]!=self.slowo2[-x]:
                self.odp2 =  "slowo 2 nie jest palindromem"
                break
        return self.odp1,self.odp2
    def sprawdz_czy_metagramy(self):
        self.roznica=0
        if len(self.slowo1)!=len(self.slowo2):
            return "wyrazy nie sa metagram"
        for x in range(len(self.slowo1)):
            if self.slowo1[x]!=self.slowo2[x]:
                self.roznica+=1
        if self.roznica>1:
            return "wyrazy nie sa metagram"
        else:return "wyrazy sa metagram"
    def sprawdz_czy_anagramy(self):
        self.lista1=self.lista_pomocnicza
        self.lista2=self.lista_pomocnicza2
        for x in self.slowo1:
            self.lista1[(ord(x))-96]+=1
        for x in self.slowo2:
            self.lista2[ord(x)-96]+=1
        for x in range(27):
            if self.lista1[x-1]!=self.lista2[x-1]:
                return "to nie anagramy"
        return "to anagramy"

    def wyświetl_wyrazy(self):
        return self.slowo1, self.slowo2
slowa=slowa("dana","kajak")
print(slowa.wyświetl_wyrazy())
print(slowa.sprawdz_czy_palindrom())
print(slowa.sprawdz_czy_metagramy())
print(slowa.sprawdz_czy_anagramy())
