# trover la borne sup
def sup(n):
    b=1
    while b<=n:
        b=2*b
    return b

# dichotomie sur [0,b]
def dichotomie(n):
    b=sup(n)
    min = 0
    max=b
    while max-min>1 :
        m=int((min+max)//2)
        if n>m:
            min=m
        elif n <m:
            max=m
        return min ,max
print(dichotomie(110))


