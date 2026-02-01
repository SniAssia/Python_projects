import math
import numpy as np


x = 2
for i in range(20) :
    x = math.sqrt(x)

for i in range(20) :
    x = x**2
# la valeur n'est pas exactement 2 parceque il y'a l'erreur de la machine quand on a fait la racine plusieurs foois
print(x)