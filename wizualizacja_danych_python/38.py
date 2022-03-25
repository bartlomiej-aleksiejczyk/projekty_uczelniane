import math
def ciag(a1=7,r=4,ile_elementów=20 ):
    suma = (((2*a1)+(ile_elementów-1)*r)/2)*ile_elementów
    return suma
print(ciag())