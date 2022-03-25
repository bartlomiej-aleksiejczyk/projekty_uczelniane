class Ciag:
    wartosci={}
    def wyświetl_dane(self):
         return self.wartosci
    def pobierz_elementy(self,idElementu,wartosc):
        (self.wartosci)[idElementu]=wartosc
    def pobierz_parametry(self,pierwszaWartosc,Roznica,ileobliczyc):
        (self.pierwszaWartosc)=pierwszaWartosc
        self.Roznica = Roznica
        self.ileobliczyc=ileobliczyc
    def policz_sume(self):
        values = self.wartosci.values()
        suma = sum(values)
        return  suma
    def policz_elementy(self):
        (self.wartosci)[0]=self.pierwszaWartosc
        for x in range(1,self.ileobliczyc):
            (self.wartosci)[x] = self.pierwszaWartosc+x*self.Roznica
sledz=Ciag()
sledz.pobierz_elementy(0,3)
print(sledz.wyświetl_dane())
sledz.pobierz_parametry(5,2,10)
sledz.policz_elementy()
print(sledz.wyświetl_dane())
print(sledz.policz_sume())

