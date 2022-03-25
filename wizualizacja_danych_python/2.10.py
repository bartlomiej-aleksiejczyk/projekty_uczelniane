import sys
a = input("wpisz pysokosc wiezy, nie wieksza niz 10\n")
a=int(a)
for i in range(a):
    for j in range(a):
        if j<=i :
            sys.stdout.write('A')
        else:
            sys.stdout.write(' ')
    sys.stdout.write('\n')