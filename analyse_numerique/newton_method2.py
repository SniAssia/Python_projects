from sympy import diff,symbols,expand
import math
x=symbols('x')
def calculer_fi(fct,x_0):
    fc=expand(fct)
    return fc.subs(x,x_0)

def newton2(f,f_prime,f_second,x_0,tol,max_iter):
    n=0
    l=[] #liste des erreurs
    x=x_0
    while (abs(calculer_fi(f_prime, x)) > tol) and (n < max_iter):
        delta= (calculer_fi(f_prime,x))**2-2*calculer_fi(f_second,x)*calculer_fi(f,x)

        if delta>=0:
            resultat_1= -(calculer_fi(f_prime,x)-math.sqrt(delta))/(calculer_fi(f_second,x))
            resultat_2 =(-calculer_fi(f_prime,x)+math.sqrt(delta))/(calculer_fi(f_second,x))
            resultat_final= min(calculer_fi(resultat_1,x),calculer_fi(resultat_2,x))
            print("x",x)
            x+=resultat_final

            print("res",resultat_final)
            l.append(resultat_final)
            if abs(calculer_fi(f, x)) < tol:
                return l,n
    return l,n
fct_4 = pow(x,5)-4*pow(x,4) +3*pow(x,3)+2*pow(x,2)-7*x + 10
newton2(fct_4,diff(fct_4,x),diff(diff(fct_4,x),x),1,10**(-12),200)