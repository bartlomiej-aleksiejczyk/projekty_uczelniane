a = input("wpisz dowolne liczby podzielone szpacjami\n")
a=str(a)
a=a.split(" ")
a = (int(x) for x in a)
wynik = [x**2 for x in a]
print(wynik)