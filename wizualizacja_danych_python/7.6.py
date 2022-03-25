import numpy
a = numpy.array([[1, 2, 3], [4, 5, 6]])
b = numpy.array([[numpy.cos(a[0, 0]), numpy.cos(a[0, 1]), numpy.cos(a[0, 2])], [numpy.cos(a[1, 0]), numpy.cos(a[1, 1]), numpy.cos(a[1, 2])]])
print(b)
