def miesiace():
    a=1
    nazwy=["styczen","luty","marzec","kwiecien",'maj','czerwiec','lipiec','siepien','wrzesien','pazdziernik','listopad','grudzien']
    while True:
        yield nazwy[a]
        a+=1
        if a>=12:
            a=1
sdfds = miesiace()

for i in range(213):
    print(next(sdfds))