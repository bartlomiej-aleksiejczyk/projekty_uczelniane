produkty = {"mleko": "litry",
"ryż": "sztuki",
"smalec": "beczki",
"buty": "sztuki",
"mięso": "kilogramy",
"papierosy": "sztuki",
"frytki": "sztuki",
"kosmici": "ciała"}
lista = [x for x in produkty.keys() if produkty[x] ==('sztuki')]
print(lista)
