from sympy import symbols,diff,expand,sin,exp
import matplotlib.pyplot as plt
x = symbols('x')
def calculer_fi(fct,x_0):
    expr= expand(fct)
    return expr.subs(x,x_0)





def methode_secante(f,x_0,x_1,tol,max_iter):
    n=0
    x_ancienne = x_0
    x = x_1
    l=[] #tableau des erreurs
    while (abs(calculer_fi(f,x)) > tol) and (n<max_iter):
        print(x)
        temp = x
        x-= (calculer_fi(f,x)*((x-x_ancienne)/(calculer_fi(f,x)-calculer_fi(f,x_ancienne)))).evalf(100)
        x_ancienne=temp
        erreur=abs(x-x_ancienne)
        l.append(erreur)
        n+=1
    n_max=n
    return l,n_max
fct = x**2-2
#methode_secante(fct,-5,-6,10**(-8),1000)

#test


fct_1 = x*x*x-x+1
fct_2= sin(x)-0.5
fct_3 = exp(x) - 2
fct_4 = pow(x,5)-4*pow(x,4) +3*pow(x,3)+2*pow(x,2)-7*x + 10

y,n=methode_secante(fct_4,1,2,10**(-32),50)
x=list(range(1,n+1))
# Tracer la courbe
plt.plot(x, y, marker='o')  # marker='o' pour afficher les points
plt.title("Courbe de l'erreur en fct de nombre des iterations pour la method de la secante")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()





methode_secante(fct_1,1,2,10**(-8),50)
print("#####################################################################################")
#methode_secante(fct_1,0,1,10**(-8),50)
print("#####################################################################################")
#methode_secante(fct_1,0,0,10^(-8),50)
print("#####################################################################################")
#methode_secante(fct_1,0,0,10^(-8),50)
