import datetime
def jedensiedem(dzien_tygodnia):
    if (dzien_tygodnia>7) or (dzien_tygodnia<1):
        return ("zly typ danych")
    if dzien_tygodnia==1:
        return("poniedzialek")
    if dzien_tygodnia == 2:
        return("wtorek")
    if dzien_tygodnia == 3:
        return("sroda")

    if dzien_tygodnia == 4:
        return("czwartek")

    if dzien_tygodnia == 5:
        return("piatek")

    if dzien_tygodnia ==  6:
        return("sobota")

    if dzien_tygodnia == 7:
        return("niedziela")

def datajakidzien(dzien=24, miesiac=3, rok=2021):
    dzionek = (datetime.date(rok,miesiac,dzien).weekday())+1
    return jedensiedem(dzionek)
