class Kwadrat:
    def __init__(self, x):
        self.x = x
        self.y = x
"""kw1 = Kwadrat(5)
kw2 = Kwadrat(5)
if kw1>kw2:
    print("wiekszy")
if kw1>=kw2:
    print("wiekszy lub rowny")
if kw1<kw2:
    print("mniejszy")
if kw1<=kw2:
    print("mniejszy lub rowny")
    Sa bledy jak uzywa sie nieprzeciazonych"""

class Kwadrat:

    def __init__(self, x):
        self.x = x
        self.y = x

    def __ge__(self,inny):
        return self.x>=inny.x
    def __gt__(self,inny):
        return self.x>inny.x
    def __le__(self,inny):
        return self.x<=inny.x
    def __lt__(self,inny):
        return self.x<inny.x
kw1 = Kwadrat(5)
kw2 = Kwadrat(5)
if kw1>kw2:
    print("wiekszy")
if kw1>=kw2:
    print("wiekszy lub rowny")
if kw1<kw2:
    print("mniejszy")
if kw1<=kw2:
    print("mniejszy lub rowny")

