# moving only one disk at time
# you should always move disks and the sorting should be held
tour={}
tour[1]=[6,5,4,3,2,1] # first road
tour[2]=[] # auxiliary road
tour[3]=[] # target road
# for a puzzle with n disks the minimum moves is 2^(n)-1
def hanoi(n,source,target,auxialary):
    if n==0 :
        return
    hanoi(n-1,source,auxialary,target)
    print(source,auxialary,target)
    target.append(source.pop())
    hanoi(n-1,auxialary,target,source)
hanoi(len(tour[1]),tour[1],tour[3],tour[2])
print(tour[1])
print(tour[2])
print(tour[3])


# methode iterative
def hanoi1(n,source,target,aux):
    stack=[]
    stack.append((n,source,target,aux))
    while stack :
        n,source,target,aux=stack.pop()
        if n==1:
            print("move disk from source to target")
        else :
            stack.append((n-1,aux,target,source))
            stack.append((1,source,target,aux))
            stack.append((n-1,source,aux,target))

hanoi1(len(tour[1]),tour[1],tour[3],tour[2])
print(tour[1])
print(tour[2])
print(tour[3])

