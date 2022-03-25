a = input("wpisz liczbe, welocyfrową\n")
suma = 0
robocza=0
x=0
while x<len(a):
    robocza=int(a[x])
    suma+=robocza
    x+=1
print(suma)