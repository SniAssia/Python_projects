# implementer une fct qui calcule la valeur du tanh(x) pour des valeurs assez grands ou petits
import numpy as np
from sympy import exp
def tanh1(x):
    if x >0 :
        a = np.float64(1+exp(-2*x))
        b = np.float64(exp(-2*x))
        res = 1/a - b/a
        return res
    else :
        a = np.float64(1 + exp(2 * x))
        b = np.float64(exp(2 * x))
        res =(b-1)/a
    return res
print(tanh1(-1000))
print(tanh1(1000))
