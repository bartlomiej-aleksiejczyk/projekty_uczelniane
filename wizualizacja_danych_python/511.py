def ciagfibonacziego():
    a=1
    b=1
    while True:
        yield a
        schowek=a
        a=b
        b=schowek+b
sdfds = ciagfibonacziego()

for i in range(213):
    print(next(sdfds))