class Wspak:
    def __init__(self, data):
        if isinstance(data, str) ==True:
            self.data = data
            self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        while self.data[self.index] not in ["a","e","i","o","u","y","A","E","I","O","U","Y"]:
            self.index-=1
        return self.data[self.index]
it = Wspak("RYBKAMARINERO")
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


