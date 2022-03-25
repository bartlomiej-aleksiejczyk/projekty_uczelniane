
#zadanie1
a = input("Wpisz zdanie:")
wynik = a.count(" ")
print(wynik)
#zadanie2
import sys
print("Podaj pierwsza liczba")
x = sys.stdin.readline()
x=int(x)
print("Podaj druga liczba")
y = sys.stdin.readline()
y=int(y)
wynik2=x*y
wynik2=str(wynik2)
sys.stdout.write(wynik2+"\n")
#zadanie3
#https://docs.python.org/3/library/stdtypes.html#comparisons
#zadanie4
import math
a = input("Wpisz liczbe:")
a=int(a)
wynik4 = math.fabs(a)
print(wynik4)
#zadanie5
liczba1 = input("Liczba pierwsza to:")
liczba1=int(liczba1)
liczba2 = input("Liczba druga to:")
liczba2=int(liczba2)
liczba3 = input("Liczba trzecia to:")
liczba3=int(liczba3)
if liczba1<=10 and liczba1>=0:
    if liczba1>liczba2 or liczba2>liczba3:
        print("wszystkie liczby spelniaja warunki")
    else:
        print("liczby a, b, c nie spelniaja warunkow")
else:
    print("Liczba 1 nie spelnia warunku")





