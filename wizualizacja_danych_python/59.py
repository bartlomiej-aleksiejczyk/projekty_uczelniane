def codrugi(data):
    if (len(data)-1)%2==1:
        for index in range(len(data)-2, -1, -2):
            yield data[index]
    if (len(data) - 1) % 2 == 0:
        for index in range(len(data)-1, -1, -2):
            yield data[index]
gen = codrugi("123456")
print(next(gen))
print(next(gen))
print(next(gen))
gen = codrugi("1234567")
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



