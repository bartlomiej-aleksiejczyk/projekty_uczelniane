def lista_zakupow(** rzeczy):
    suma =0
    for cos in rzeczy:
        suma+=rzeczy[cos]
    return suma
print(lista_zakupow(czekolada=10, wodka=12))