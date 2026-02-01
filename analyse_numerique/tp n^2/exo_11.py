import numpy as np
def algo_de_kahan():
    n=1000000
    erreur=0
    sum1=0
    iter=1
    while (n>0) :
        x = np.float64(1 / iter)
        y = x - erreur
        #print("la valeur de x :",x)
        s=sum1+y #ajouter la valeur exacte apres la soustraction de l'erreur
        erreur =np.float64( s - sum1- y) # s = fl(sum1+y)
        #print("erreur :",erreur)
        sum1 = s
        iter+=1
        n-=1
    return  sum1
print("la somme apres implementation de l'algo : ",algo_de_kahan())

s=0
ina=1
for i in range(1000000):
    x=np.float64(1/ina)
    s+=x
    ina+=1
print("la somme normale sans implementer l'algo de kahan",s)

