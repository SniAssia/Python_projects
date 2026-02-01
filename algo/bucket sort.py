import random
n = 100
m =10
k=int(n/m)
vmin =1000
vmax= 2000
l=[]
for i in range(n):
    x=random.randint(vmin,vmax)
    l.append(x)

# creer paniers
dict={}
for i in range(k):
    dict[i]=[]

for v  in l :
    r=(v-vmin)/(vmax-vmin)
    num_pan=int(r*k)
    dict[num_pan].append(v)

for i in range(k):
    dict[i].sort()

l2=[]
for i in range(k):
    l2+=dict[i]
print(l2)

# o(n+k)