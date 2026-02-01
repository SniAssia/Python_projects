from sympy import symbols,expand,diff,Eq, solve , Matrix,cos,sin
import numpy as np
# methode de newton raphson
x= symbols('x')
y=symbols('y')
z = symbols('z')
def calcul(f,x_0,y_0):
    expr = expand(f)
    return expr.subs({x:x_0,y:y_0})

def calcul_jacob(f,n,x_0,y_0,symbols):
    # f liste des fct
    # symbols liste des symboles
    l = [[0 for _ in range(n)]for _ in range(n)] # matrice jacobienne
    for i in range(n):
        for j in range(n):
            l[i][j] = calcul(diff(f[i],symbols[j]),x_0,y_0)
    return l
f = [x+2*y-2,pow(x,2)+4*pow(y,2)-4]
print(calcul_jacob(f,2,1,2,[x,y]))

def newton_raphson(f,epsilon,x_0,y_0,n):
    x_prime = x_0
    y_prime = y_0
    x_ancienne = 0
    y_ancienne =0

    while (abs(x_prime-x_ancienne)>epsilon or abs(y_prime-y_ancienne)>epsilon ):
        l = calcul_jacob(f,n,x_prime,y_prime,[x,y]) # matrice jacobienne
        b1 = [ -calcul(f[0],x_prime,y_prime) , -calcul(f[1],x_prime,y_prime) ]
        A = Matrix(l)
        b = Matrix(b1)
        # resoudre le systeme lineaire calcul_jacob(f,n,x_0,y_0,[x,y])*s=-calcul(f,x_0,y_0)
        s = A.LUsolve(b)
        # s retourne dict
        x_ancienne = np.float64(x_prime)
        y_ancienne = np.float64(y_prime)
        x_prime += np.float64(s[0])
        y_prime += np.float64(s[1])
        print(x_prime,y_prime)
    return x_prime,y_prime
print(newton_raphson(f,10**(-2),1,2,2))

# la methode de la secante
def secante(f,epsilon,x_0,y_0,n):
    B_ini = calcul_jacob(f,n,x_0,y_0,[x,y])
    x_prime = x_0
    y_prime = y_0
    x_ancienne =0
    y_ancienne =0
    while (abs(x_prime -x_ancienne)>epsilon and abs(y_prime -y_ancienne)>epsilon):
        b1 = [-calcul(f[0], x_prime, y_prime), -calcul(f[1], x_prime, y_prime)]
        A = Matrix(B_ini)
        b = Matrix(b1)
        # resoudre le systeme lineaire calcul_jacob(f,n,x_0,y_0,[x,y])*s=-calcul(f,x_0,y_0)
        s_k = A.LUsolve(b)
        # s retourne matrice
        x_ancienne = np.float64(x_prime)
        y_ancienne = np.float64(y_prime)
        x_prime += np.float64(s_k[0])
        y_prime += np.float64(s_k[1])
        y_k_1 = calcul(f[0],x_prime,y_prime)-calcul(f[0],x_ancienne,y_ancienne)
        y_k_2= calcul(f[1],x_prime,y_prime)-calcul(f[1],x_ancienne,y_ancienne)
        y_k =Matrix([y_k_1,y_k_2])
        s_k_m = Matrix(s_k)
        B_ini_m = Matrix(B_ini)
        v1 = y_k - B_ini_m*s_k_m
        B_ini_m += (v1*s_k_m.T)/ (s_k_m.T*s_k_m)[0]
        B_ini = B_ini_m
        print(x_prime, y_prime)
    return x_prime,y_prime
print(secante(f,10**(-3),1,2,2))


# la methode du point fixe
g = [-cos(x)/81+pow(y,2)+sin(z)/3,sin(x)/3+cos(z)/3,-cos(x)/9+y/3+sin(z)/6]
def calcul_f(f,x_0,y_0,z_0):
    expr = expand(f)
    return expr.subs({x:x_0,y:y_0,z:z_0})

def point_fixe(g,epsilon,x_0,y_0,z_0,n):
    x_next = x_0
    y_next = y_0
    z_next = z_0

    x_ancienne =0
    y_ancienne =0
    z_ancienne =0

    while (abs(x_next-x_ancienne)>epsilon or abs(y_next-y_ancienne)>epsilon or abs(z_next-z_ancienne)>epsilon):
        x_ancienne = x_next
        y_ancienne = y_next
        z_ancienne = z_next
        x_next = np.float64(calcul_f(g[0],x_ancienne,y_ancienne,z_ancienne))
        y_next = np.float64(calcul_f(g[1], x_ancienne,y_ancienne,z_ancienne))
        z_next = np.float64(calcul_f(g[2], x_ancienne,y_ancienne,z_ancienne))
        print(x_next,y_next,z_next )
    return x_next,y_next,z_next

print(point_fixe(g,10**(-3),1,1,1,2))