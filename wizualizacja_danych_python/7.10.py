import numpy as np
b = np.arange(81).reshape(9,9)
c = b.reshape((1,81))
c = b.reshape((3,3,3,3))
c = b.T
c = b.ravel()
#przekształcac można aby mnożenie elemntow całkowitych sie zgadzało
print(c)
