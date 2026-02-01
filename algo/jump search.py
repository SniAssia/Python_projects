def bornesup(n,m):
    b=m
    while b<=n:
        b=b+m
    return b

def jumpsearch(n,m):
    b=bornesup(n,m)
    while b>0:
        if n==b :
            break
        else :
            b=b-1
    return b
print(jumpsearch(36,10))


