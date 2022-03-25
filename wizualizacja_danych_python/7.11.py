import numpy as np
b = np.arange(12)
d = b.reshape((3,4))
d = d.ravel()
e = b.reshape((4,3))
e = e.ravel()
c = b.reshape((2,6))
c = c.ravel()
print(d)
print(e)
print(c)


