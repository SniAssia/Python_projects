# evaluation de fct
from sympy import sin
import numpy as np
epsilon = 1e-4
x = np.float32(sin(np.pi/2+epsilon))
print(x)