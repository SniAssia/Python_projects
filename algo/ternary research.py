# trover la borne sup
def sup(n):
    b=1
    while b<=n :
        b=2*b
    return b

def ternary(n):
    a=0
    b=sup(n)
    tiers=(b-a)//3
    m1=a+tiers
    m2=a-tiers
    while (b-a)//2:
        if n<m1:
            b=m1
        elif n>m2:
            a=m2
        else :
            a=m1
            b=m2
    for i in range(b-a):
        if n==i:
            return i
