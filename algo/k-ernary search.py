# x le nombre recherché
import random
l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
x=13
def div_k(l1,k):
    if k<= 0 or k> len(l1):
        return False
    else :
        l=[]
        n = len(l1)//k
        rest = len(l1)%k
        start =0
        for i in range(k):
            end = start + n + (1 if i<rest else 0)
            l.append(l1[start:end])
            start = end
    return l

print(div_k(l1,4))

def search(x,l,k):
    a=0
    b=len(l)-1
    while b-a > 1 :
        positions = [a]
        for i in range(k):
            positions.append(int(a+ (b-a)*(i+1)/k))
        for i in range(k):
            if x>=l[positions[i]] and x<=l[positions[i+1]]:
                a=positions[i]
                b=positions[i+1]
    if l[a]==x or l[b]==x :
        print("trouvé")
    else :
        print("non")
print(search(15,l1,4))
