from sympy import symbols,expand,diff,sin,exp
import sys
import math
# calculer f d'une valeur
sys.set_int_max_str_digits(0)
x=symbols('x')

def calcule_fi(fct,x_0 ):
    #convertir la string a une expr simpify
    expr = expand(fct)
    return expr.subs(x, x_0)
fct = x**2-2
print(calcule_fi(fct,2))

#def deriv(fct_0,x_0):
  #  expr= expand(fct)
  #  der=diff(fct_0,x)
  #  return der.subs(x,x_0)
#print(deriv(fct,2))

def methode_newton(f,f_prime, x_o, tol,max_iter) :
    n=0
    x=x_o
    while (abs(calcule_fi(f,x))>tol) and (n<max_iter):
        print(x)
        temp=x
        x-= (calcule_fi(f,x)/calcule_fi(f_prime,x)).evalf(100)
        erreur = abs(temp-x) #la valeur des ordonnées dans mon graphe
        # la valeur des abscisses (num_d'iter)


        n+=1

#methode_newton(fct,diff(fct,x),1,10^(-8),50)


def methode_newton2(f, f_prime, x_o, tol, max_iter):
    n = 0
    x_ancienne=0
    x = x_o
    while (abs(x_ancienne-x) > tol) and (n < max_iter):
        print(x)
        x_ancienne = x
        x -= (calcule_fi(f, x) / calcule_fi(f_prime, x)).evalf(100)
        n += 1


fct_1 = x*x*x-x+1
fct_2= sin(x)-0.5
fct_3 = exp(x) - 2
fct_4 = pow(x,5)-4*pow(x,4) +3*pow(x,3)+2*pow(x,2)-7*x + 10


methode_newton(fct_4,diff(fct_4,x),0,10**(-2),1000)
print("#####################################################################################")
#methode_newton(fct_1,diff(fct_2,x),1,10**(-8),50)
#print("#####################################################################################")
#methode_newton(fct_1,diff(fct_3,x),0,10^(-8),50)
#print("#####################################################################################")
#methode_newton(fct_1,diff(fct_4,x),0,10^(-8),50)


