from sympy import symbols
import numpy as np
import math
x= symbols('x')
fct = 1e-3*(x**2)+1e5*x+1

delta = np.float64(1e10 - 4*1e-3)
print(math.sqrt(delta))
print("dddd")
res1 = np.float64(-1e5 + math.sqrt(delta) ) /  (2*1e-3)
res2 = np.float64(-1e5 - math.sqrt(delta) ) /  (2*1e-3)
print(res1)
print(res2)

re1= 2/ np.float64(-1e5 + math.sqrt(delta) )
re2 = 2/np.float64(-1e5 - math.sqrt(delta) )
print(re1)
print(re2)




erreur1 = abs(np.float64(res1)-np.float64(re2))

erreur2 = abs(np.float64(res2)-np.float64(re1))

print(erreur1)
print(erreur2)

# -10**-5 -10**-8
