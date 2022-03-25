import numpy
c = numpy.array([[1, 2, 3], [4, 5, 6]])
d = numpy.array([[9, 33, 3], [331, 7, 16]])
a = numpy.array([[numpy.sin(c[0,0]), numpy.sin(c[0,1]), numpy.sin(c[0,2])] ,[numpy.sin(c[1,0]), numpy.sin(c[1,1]), numpy.sin(c[1,2])]])
b = numpy.array([[numpy.cos(d[0, 0]), numpy.cos(d[0, 1]), numpy.cos(d[0, 2])], [numpy.cos(d[1, 0]), numpy.cos(d[1, 1]), numpy.cos(d[1, 2])]])
print(a)
print(numpy.add(a,b))