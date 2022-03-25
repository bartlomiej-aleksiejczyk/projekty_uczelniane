class Kwadrat:
    def __init__(self, x):
        self.x = x
        self.y = x

kw = Kwadrat(5)
#print(kw+5)
class Kwadrat:

    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self,dodac):
        return Kwadrat(self.x+dodac)
    def poka_dane (self):
        return (self.x, self.y)
kw1 = Kwadrat(5)
print(kw1.poka_dane())
print((kw1+1).poka_dane())
