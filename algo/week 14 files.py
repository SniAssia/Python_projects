#create a function to display a matrix
"""
def matrix(r,c):
    l2=[]
    for i in range(r):
        l1= []
        for j in range (c):
            num = int(input("enter elements of this matrix : "))
            l1.append(num)
        l2.append(l1)
    return l2

def getlist(N):
    N=int(input("enter an integer :"))
    l1= []
    for i in range(N):
        num = int(input("enter a number to add to the list :"))
        l1.append(num)
    return l1
print(getlist(5))

def findmin(l1):
    l1.sort()
    return l1[0]
print(findmin([1,2,8,7,9]))



def findmax(l1):
    l1.sort()
    return l1[-1]
print(findmin([1, 2, 8, 7, 9]))


def comptavg(l1):
    sum = 0
    for i in range (len(l1)):
        sum = sum + i
        avg = sum//len(l1)
    return avg
#call a function
l2 = []
n = int(input("enter the number of elements of this list :"))

for i in range(n):
    num2 = int(input("enter elements of this list : "))
    l2.append(num2)
print(comptavg(l2))
"""
"""
def letteru(sent):
    l1=sent.split()
    l2= []
    for i in l1:
        if "u" in i:
            l2.append(i)
    return l2
sent2 = input("enter a sentence ")
print(letteru(sent2))



#openhello.txt to read from
handle = open("hello.txt","r")
#read all content of this file
text = handle.read()
#print variable text to screen
print(text)
handle.close()

#open hello.txt to read from
handle = open("hello.txt","r")
#read one line from the file
linelist = handle.readline()
#print line to screeen
print(linelist)
#close file
handle.close()

#open hello.txt to read from
handle = open("hello.txt","r")
#read one line from the file
lineslist = handle.readlines()
#print line to screeen
print(lineslist)
#close file
handle.close()

#open a file to read from
handle = open("hello.txt","r")
for line in handle :
    #print line to screen
    print(line)
#close
handle.close()

#writing a line to a file
#open a file to read from
handle = open("hello.txt","w")
#write a line to a file
handle.write('i like python ')
#close hello.txt
handle.close()



lineslist = ["salam students\n","i want you to practice python\n","file operations are easy\n"]
handle = open("hello.txt","w")
for line in lineslist:
    handle.write(line)
handle.close()

handle = open("hello.txt","w")
handle.writelines(lineslist)
handle.close()

handle = open("hello.txt","a")
handle.writelines(lineslist)
handle.close()
"""
def matrix(r,c):
    l2=[]
    for i in range(r):
        l1= []
        for j in range (c):
            num = int(input("enter elements of this matrix : "))
            l1.append(num)
            l1.sort()
        l2.append(l1)
        for k in l1:
            return l1[-1]
print(matrix(2,2))
































