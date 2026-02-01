import numpy as np

def value_pi(n):
    sum =0
    epsilon =  2**(-24)
    elem=1
    while (n>0):
        x = 1/ np.float64(elem)
        print("x",x)
        elem+=2
        y = 1/np.float64(elem)
        print("y",y)
        sum+=x-y
        elem+=2
        n-=1
    return 4*sum
print(value_pi(1000))