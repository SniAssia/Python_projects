import numpy as np

a = np.float32(1e-38)
b = np.float32(2e-39)
c  = a/ b
print(c)


e = 2 / np.float32(3e45)
f= 2 / np.float64(3e45)
print("simple precision " , e)
print("double precision : ",f)