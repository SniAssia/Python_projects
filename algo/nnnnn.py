"""
def matrix(mx):
    for row in range(len(mx)):
        for col in range(len(mx[row])):
            print(mx[row][col], end=" ")
        print()
    for row in range(len(mx)):
        for col in range(len(mx[row])):
            print(mx[2-row][2-col],end = " ")
        print()
    a=int(input("enter element : "))
    for i in mx[row]:
        if i != a :
            return False
    return True
print(matrix( [[1,2,3],[4,5,6],[7,8,9]] ))

def sortd(l):
    if len(l)<=1:
        return l
    else :
        pivot = l[0]
        less_than_pivot = []
        great_than_pivot = []
        for i in l[1:]:
            if i < pivot:
                less_than_pivot.append(i)
            else :
                great_than_pivot.append(i)
        return sortd(less_than_pivot)+[pivot]+sortd(great_than_pivot)
print(sortd([7,9,5,3,2]))
"""
# open hello.txt to read from
handle = open("hello", "r")
for line in handle:
#print line to screen
    print( line )
# close hello.txt
handle.close( )

