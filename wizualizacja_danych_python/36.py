import math
def kolo(a=1,b=1,x=1,y=1):
    promien = math.sqrt(((x-a)**2)+((y-b)**2))
    return promien
print(kolo(1,4,2,1))