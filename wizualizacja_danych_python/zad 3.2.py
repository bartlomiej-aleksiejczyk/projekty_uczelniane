#zad3.2
import random

losowa_macierz = [[random.random() for j in range(4)] for i in range(4)]
print(losowa_macierz)
przekątna_macierz_lewo_prawo = [losowa_macierz[x][y] for x in range(4) for y in range(4) if x==y]
print(przekątna_macierz_lewo_prawo)

