
"""
#open a file
handle = open("bill.txt","r")
#read all content of the file
content = handle.read()
print(content)
handle.close()

#how to read just one line from a file
handle = open("bill.txt","r")
line = handle.readline()
print(line)
handle.close()


#how to read all lines in a file as a list
handle = open("bill.txt","r")
lines = handle.readlines()
print(lines)
handle.close()

#how to read line by line using loop
handle = open("bill.txt","r")
for l in handle :
    print(l)
handle.close()

#how to write a line to a file
handle = open("bill.txt","w")
handle.write("I like myself")
handle.close()

#writing multiple lines iteratively
l6 =["hello","hhhhh","hhiii"]
handle = open("bill.txt","w")
for i in l6:
    handle.write(i+"\n")
handle.close()

#writing multiple lines at once
lines = ["hhh","jjj","oooo","ppppp"]
handle = open("hello","w")
handle.writelines(lines)
handle.close()

#appending a line to a file
handle = open("hello","a")
handle.writelines("hello world \n")
"""
"""
#read a text file
handle = open("bill.txt","r")
l=[]
sum = 0
for i in handle :
    l=i.split()
    sum = sum+len(l)
print(sum)
handle.close()

#count the number of times a letter appear in a text file
handle =open("bill.txt","r")
L=[]
times=0
for i in handle :
    L=i.split()
    for word in L:
        times = times + word.count("l")+word.count("L")
print(times)
#first method
handle = open("bill.txt","r")
l3=[]
for i in handle :
    l = i.split()
    l3.append(l)
l4 = l3[1:]
sum =0
for i in range(len(l4)-1):
    sum =sum +float(l4[i][1])
print(sum)
print("total is :", len(l4)-1)
l5=[]
for j in range(len(l4)-1):
    l5.append(l4[j][1])
print(l5)
l5.sort()

n = int(input("enter the number of test cases : "))
l1=[]
for i in range(n):
    l=[]
    for j in range(2):
        num= int(input("enter elements of every nested list : "))
        l.append(num)
    l1.append(l)
l4=[]
for i in range(n):
    l3=[]
    for j in range(2):
        x=l[0]+" "+l[1]
        l3.append(x)
    l4.append(l3)
print(l4)
handle = open("bill.txt","w")
for i in dict:
    handle.write(str(i))
    handle.write(str(dict[i])+"\n")
handle.close()
"""
"""
#write a program to write the input in a file
handle = open("bill.txt","r")
l3=[]
for i in handle :
    l=i.split()
    l.remove(l[0])
    l3.append(l)
l4=l3[1:]
l6=[]
for i in l4:
    l5=[]
    for j in i :
        s=int(j)
        l5.append(s)
        l5.sort()
    l6.append(l5)
print(l6)
"""
"""
#n base palindrome
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
    result = " "
    while n>0:
        count = n % base
        result = str(count)+ result
        n//=base
    return result
#define a function to check if this number is palindrome or not
def palind(n,base):
    s=convert(n,base)
    if s==s[::-1]:
        return True
    return False
#upload this information to file
handle1 = open("output","w")
for i in range(len(l3)):
    for j in range(len(l3[i])-1):
        if palind(int(l3[i][j]),int(l3[i][j+1])) is True :
            handle1.write("yes"+"\n")
        else :
            handle1.write("no"+"\n")
"""
"""
l3=[]
handle =open("output","r")
for i in handle :
    l1 = i.split(":00")
    for i in l1:
        l2=[]
        x=i.replace("-","")
        l2.append(x)
        l3.append(l2)
print(l3)
"""
"""
handle = open("input1", "r")
l3 = []
for i in handle:
    l = i.split()
    l3.append(l)
print(l3)


def convert(n, base):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        count = n % base
        result = str(count) + result
        n //= base
    return result


def palind(n, base):
    s = convert(n, base)
    if s == s[::-1]:
        return True
    return False


handle1 = open("output", "w")
for i in range(len(l3)):
    for j in range(len(l3[i]) - 1):
        if palind(int(l3[i][j]), int(l3[i][j + 1])) is True:
            handle1.write("yes" + "\n")
        else:
            handle1.write("no" + "\n")

for lines in handle1:
    c=1
    e=[]
    if n>0:
        list=lines.split()
        sum=0
        count =1
        while count<=int(list[0]) :
            sum = sum + count
            count =count +1
        print(sum)
"""
def sum_sum(numbers):
    total_sum = 0

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            total_sum += numbers[i] + numbers[j]

    return total_sum

# Test the function with some example numbers
numbers = [1, 2, 3, 4, 5]
result = sum_sum(numbers)
print("The sum of the sum of the numbers is:", result)