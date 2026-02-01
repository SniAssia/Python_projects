#while loop

count= 0       #initialize loop control variables

while count <= 10 :     #check the loop control variables
    count = count + 1      #update the loop control variable
    print(count)



#write a python program to add the first 10 numbers

count = 0
iresult = 0
while count < 10 :
    count = count + 1
    iresult = iresult + count
print(iresult)

#write a python program with while loop to add any 6 numbers giving by the user
count= 0
result = 0

#loop
while count < 6 :
    num = int(input(" enter a number :"))
    result = result + num
    count=count + 1

#display result
print(result)
average = result/6
print(average)


#write a python program using a loop to find the average of n numbers
count=0
result=0
n =int(input("enter a number "))
while count< n :
    num = int(input("enter another number :"))
    result = result + num
    count=count+1

average=result/n
print(average)


#write a python program using a while loop to print the multiplication table of a number N


for i in range (0,15,1):
    print(i)

for i in range (20,25):
    print(i)

for i in range(100,0,-10):
    print(i)



sum = 0
i = 1
while i < 10:
    sum = sum + i
    i = i + 1

print(sum)



sum = 0
i = 1
while i < 10:
    sum = sum + i
    i = i + 2

print(sum)


string = input("enter a string : ")
for letter in string :
    print(letter)

weekDays = ["sunday","monday","tuesday","thursday"]

for letter in weekDays :
    print(letter)

for num in range(10):

    if num == 5:
        continue
    print("num is :",num)

numlist =[0,1,5]
alphalist = ["a","b","c"]
for num in numlist:
    for let in alphalist :
        print(num,let)
"""
#python program to check if a given number is prime or not
n = int(input("enter a number :"))
if n > 1 :
    for i in range (2,n):
        if (n%i)==0 :
            print(n,"is not a prime number ")
            break
    else :
        print(n,"is a prime number ")

else :
    print(n,"is not a prime number ")


x=4
y=0
while x>=0:
    x = x-1
    y = y+1

    if x==y:
        continue
    else:print (x,y)













































































