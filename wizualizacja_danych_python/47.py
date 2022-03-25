class robot:
    # definicja konstruktora
    def __init__(self, x, y, krok, xa,ya):
        if xa>x or ya>y or xa<1 or ya<1:
            print("robocik spadl z planszy :(")
            del self
        else:
            self.x=x
            self.xa = xa
            self.y = y
            self.ya = ya
            self.krok = krok
    def pokaz_gdzie_jestes(self):
        return self.xa, self.ya
    def idz_w_gore(self,ile_krokow):
        if self.ya+ile_krokow>self.y:
            print("robocik spadl z planszy :(")
            del self
        else:
            self.ya+=ile_krokow
    def idz_w_dol(self, ile_krokow):
        if self.ya - ile_krokow < 1:
            print("robocik spadl z planszy :(")
            del self
        else:
            self.ya -= ile_krokow
    def idz_w_prawo(self,ile_krokow):
        if self.xa+ile_krokow>self.x:
            print("robocik spadl z planszy :(")
            del self
        else:
            self.xa+=ile_krokow
    def idz_w_lewo(self,ile_krokow):
        if self.xa-ile_krokow<1:
            print("robocik spadl z planszy :(")
            del self
        else:
            self.xa-=ile_krokow
    def __del__(self):
            print("koniec programu")

sledz = robot(10,10,1,2,1)
print(sledz.pokaz_gdzie_jestes())

sledz.idz_w_gore(4)
print(sledz.pokaz_gdzie_jestes())

sledz.idz_w_prawo(4)
print(sledz.pokaz_gdzie_jestes())

sledz.idz_w_dol(2)
print(sledz.pokaz_gdzie_jestes())

sledz.idz_w_lewo(4)
print(sledz.pokaz_gdzie_jestes())
