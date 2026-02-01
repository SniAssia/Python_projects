#overflow
import numpy as np
val=1e308
a = val+val

val2=np.float64(10**308)
c =val2+val2
print(c)
b=10**308 + 10**308

print(a)
print(b)