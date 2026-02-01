#print first 10 natural numbers using while loop
count = 0
while count < 10:
    count = count + 1

    print( count )
for i in range (1,2) :
    for j in range (2,3):
        for k in range (3,4):
            for a in range (4,5):
                for b in range (5,6):
                    print(i)
                    print(i,j)
                    print(i,j,k)
                    print(i,j,k,a)
                    print(i, j ,k ,a ,b )
#calculate the sum of all numbers from 1 to a given number
count = 0
sum = 0
n = int(input("enter a number "))
while count < n :
    count = count + 1
    sum = sum + count
print(sum)
#print multiplication table of a given number
count = 0
n = int(input("enter a number :"))
while count < 10:
    count = count + 1
    square  = n * count
    print(n,"*",count,"=", square)
#display numbers from a list using loop
numbers = [12,75,150,180,145,525,50]
for x in numbers :
    if x > 500 :
        break
    if x > 150 :
        continue
    if x%5 == 0:
        print(x)

#count the total number of digits in a number
n = int(input("enter a number:"))
count = 0
while n != 0 :
    n = n //10   #integer division
    count = count + 1
print(count)

#print the following pattern
for i in range (1,2) :
    for j in range (2,3):
        for k in range (3,4):
            for a in range (4,5):
                for b in range (5,6):
                    print(i, j ,k ,a ,b )
                    print(i,j,k,a)
                    print(i,j,k)
                    print(i,j)
                    print(i)
#print list in reverse order using loop
list = [10,20,30,40,50]
print(list[-1])
print(list[-2])
print(list[-3])
print(list[-4])
print(list[-5])
#display numbers from -10 to -1 using for loop
count = -11
while count <-1:
    count = count + 1
    print(count)

for i in range(5):
    print(i)
print("done")

#write a python program to display all prime numbers within a range

a = int(input("enter an integer :"))
b = int(input("enter another integer :"))

print("prime numbers between ",a ,"and",b ,"are :")
for n in range (a,b+1):
    if n>1:
        for i in range (2, n ):
            if n%i==0 :
                break
        else:
            print(n)

#display fibonacci series
sum = 0
count = 0
result = 1
num = 1
n = int(input("enter an integer :"))
while count < n:
    count = count +1
    sum = result
    result = num
    num = result + sum
    print(num)

#reverse a given integer number
n = int(input("enter an integer :"))
count =  0
while n > 0 :
    num = n%10
    count = (count *10)+num
    n = n//10
print(count)

#the cube of all numbers from 1 to a given number
n = int(input("enter a number :"))
count = 0

while count < n :
    count = count + 1
    result = count**3
    print(result)


#find the sum of the series upto n terms
n = int(input("enter an integer :"))
a = 2
count = 0
for i in range(0,n):
    count = count +a
    a = (a*10)+ 2
print(count)






