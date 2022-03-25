def ciag(* liczby):
    # jeżeli nie ma argumentów to
    if len(liczby) == 0:
        return 0.0
    else:
        iloczyn = 1
    for i in liczby:
        iloczyn *= i
    return iloczyn

print(ciag())
print(ciag(2,1,3,7))