from sympy import expand,symbols,diff
import matplotlib.pyplot as plt
import numpy as np

x=symbols('x')
def calcule_fi(fct,x_0 ):
    #convertir la string a une expr simpify
    expr = expand(fct)
    return expr.subs(x, x_0)

fct=pow(x,5)-4*pow(x,4) +3*pow(x,3)+2*pow(x,2)-7*x + 10
#fct= x*x*x-x+1

def methode_newton(f, f_prime, x_o, tol, max_iter):
    n = 0
    x = x_o
    l=[] #liste des valuers de l'erreur
    while (abs(calcule_fi(f, x)) > tol) and (n < max_iter):

        temp = x
        x -= (calcule_fi(f, x) / calcule_fi(f_prime, x)).evalf(100)
        erreur = abs(temp - x)  # la valeur des ordonnées dans mon graphe
        l.append(erreur)
        # la valeur des abscisses (num_d'iter)
        print("x",x)
        print("temp",temp)
        print("erreur" ,erreur)

        n += 1
    n_final=n
    print(n_final)
    return l,n_final

y,n=methode_newton(fct,diff(fct,x),0,10**(-32),1000)
x=list(range(1,n+1))
# Tracer la courbe
plt.plot(x, y, marker='o')  # marker='o' pour afficher les points
plt.title("Courbe de l'erreur en fct de nombre des iterations pour la method de newton")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()

