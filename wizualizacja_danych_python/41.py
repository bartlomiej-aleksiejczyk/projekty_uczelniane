import sys
import random
liczba1 = (random.randint(0,23392497394))*4
liczba2 = (random.randint(0,23392497394))*4
liczba1 = str(liczba1)
liczba2 = str(liczba2)
plik = open("zad1.txt", "w+")
plik.write(liczba1)
plik.write('\n')
plik.write(liczba2)
plik.write('\n')
plik.close()
