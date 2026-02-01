handle = open("bill.txt","r")
l3=[]
for i in handle :
    l=i.split()
    l3.append(l)
print(l3)

#define a function to convert this number to any base
def convert(n,base):
    if n == 0:
        return "0"
    result = ""
    while n>0:
        count = n%base
        result = str(count)+ result
        n//=base
    return result

#define a function to check if this number is palindrome or not
def palind(n,base):
    s=convert(n,base)
    return s == s[::-1]

#call function
for i in range(len(l3)):
    for j in range(len(l3[i])-1):
        if palind(int(l3[i][j]),int(l3[i][j+1])) ==True :
            return True