# heap =tas
l=[1,2,3,4,5,6,7,8,9]
def switch2(l,p):
    e1=2*p+1
    e2=2*p+2
    largest=p
    if e1<len(l) and l[e1]>l[p]:
        largest = e1
    if e2 < len(l) and l[e2]>l[largest]:
        largest = e2
    if largest != p :
        l[p],l[largest]=l[largest],l[p]
        return largest
    return -1

print(switch2(l,0))

def repare(l,q):
    sum =q
    while sum != -1:
        sum = switch2(l,q)


L = [673, 720, 163, 319, 216,
     947, 848, 439, 913, 566, 823, 561,
     898, 254, 545, 41, 683, 3, 626, 417]
def heapsort(l):
    k=len(l)
    while k>=0:
        repare(l,k)
        k-=1
    l1=[]
    while len(l) > 1:
        l1.append(l[0])
        l[0] = l.pop()
        k = len(l) - 1  # dernier élement
        while k >= 0:
            repare(l,k)
            k -= 1
    l1.append(l[0])
    return l1

print(heapsort(L))


# version modifiée de heapsort
# tas n-aire
# reparer de maniere recurssive
# tas inversé

L = [673, 720, 163, 319, 216,
     947, 848, 439, 913,]
relations = {0: [1, 2, 3],  # A -> B, C, D
             1: [4, 5, 6],  # B -> E, F,G
             2:[ ],
             3: [7, 8]}    # D -> H, I
def switch2(l,dict,p,i):
    largest=p
    if dict[i]!=[]:
        for j in range(1,len(dict[i])):
            for a,b in dict.items() :
                if i in b :
                    ba=len(b)
            ei = p*ba+j
            if ei<len(l) and l[ei]>l[largest]:
                largest=ei
        if largest != p :
            l[largest],l[p]= l[p], l[largest]
            return largest
    return -1
print(switch2(L,relations,3,3))



# heapsort modifie
L = [673, 720, 163, 319, 216, 947, 848, 439, 913, 566, 823, 561, 898, 254, 545, 41, 683, 3, 626, 417]
L2 = []

def switch3(l,p,m):
    emin = p
    for i in range(m):
        e=m*p+1+i
        if e<len(l) and l[e]<l[emin]:
            emin = e
        if l[p]>l[emin]:
            l[p],l[emin]= l[emin],l[p]
            return emin
        else :
            return -1
# fontion reparer recurssive
def repa(l,q,m):
    switch = q
    if switch != -1:
        switch = switch3(l,q,m)
        repa(l,switch,m)

# la meme fct heapsort




