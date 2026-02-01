from sympy import symbols,expand,diff,sin,exp
import math
import matplotlib.pyplot as plt
x = symbols('x')
fct1=x*x-2
def calculer_fi(fct,x_0):
    expr= expand(fct)
    return expr.subs(x,x_0)
def dichotomy_method(f,a,b,tol):
    if math.copysign(1,calculer_fi(f,a)) == math.copysign(1,calculer_fi(f,b)):
        print("please enter different values of a and b in which the sign of their images is different")
        return
    l=[] # tableau des erreurs
    n=0
    while((b-a)>tol):
        c =(a+b)/2
        d=(b-a)/2
        l.append(abs(d))
        if math.copysign(1,calculer_fi(f,a)) != math.copysign(1,calculer_fi(f,c)):
            b=c
        else :
            a=c
        print("a",a)
        print("b",b)
        print("c",d)

        n+=1
    return l,n
fct_1 = x*x*x-x+1
fct_2= sin(x)-0.5
fct_3 = exp(x) - 2
fct_4 = pow(x,5)-4*pow(x,4) +3*pow(x,3)+2*pow(x,2)-7*x + 10


y,n=dichotomy_method(fct_4,-4,4,10**(-2))
x=list(range(1,n+1))
# Tracer la courbe
plt.plot(x, y, marker='o')  # marker='o' pour afficher les points
plt.title("Courbe de l'erreur en fct de nombre des iterations pour la method de la dichotomie")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()






#dichotomy_method(fct_1,-3,3,10**(-6))
#print("#####################################################################################")
#dichotomy_method(fct_2,-3,3,10**(-6))
#print("#####################################################################################")
#dichotomy_method(fct_3,-3,3,10**(-6))
#print("#####################################################################################")
#dichotomy_method(fct_4,-3,3,10**(-6))
