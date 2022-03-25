with open("zad3.txt", "w+") as plik:
    plik.write("marinero")
    plik.write('\n')
    plik.write("rybka")
    plik.write('\n')
    plik.write("kuntersztyn")
    plik.write('\n')
    plik.write("blumber")
    plik.write('\n')
with open("zad3.txt", "r") as plik:
    for tekst in plik:
        print(tekst)