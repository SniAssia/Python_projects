# precision machine
import numpy as np
import random



def calcul_precision_machine32():
    epsilon = 1.0
    while (1+epsilon) >  1 :
        epsilon = np.float32(epsilon) / 2.0
    return epsilon
print("resultat pour simple prec :",calcul_precision_machine32())
def calcul_precision_machine64():
    epsilon = 1.0
    while (1+epsilon) >  1 :
        epsilon = np.float64(epsilon) / 2.0
    return epsilon
print("resultat pour simple prec :",calcul_precision_machine64())

print("simple precision : ", 2**(-24))
print("double precision : ", 2**(-53))









