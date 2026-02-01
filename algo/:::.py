num = "369"
for x in range(2):
     if (int(num[x]) % 3) == 0:
              print(num[x])

import math
radius = 2
if radius >= 0:
      area = radius * radius * math.pi
      print("The area circ. of radius", radius, "is", area)
print("let us continue")

num = 77
if num % 2 == 0:
    print("nuu")
else:
    print("num is odd")
x = 3
y = 3
if x > 2 :
    if y > 2 :
        z = x + y
        print("z is",z)
else :
    print("x is ",x)

num = 123
s = str(num)
print(s)
print(s[1])
title = "chapter" ,3
print(title)

sum = 0
i = 1
while i < 10:
    sum = sum + i
    i = i + 2
print(sum)


i = 1
while i < 10:
    if i % 2 == 0:
        print(i)
    i = i + 1

sum = 0
number = 0

while number < 20:
   number += 1
   sum += number

   if sum >= 30:
      break

print("The number is", number)
print("The sum is", sum)

balance = 10
while True:
   if balance < 9:
      break
   balance = balance - 9

print("Balance is", balance)



for num in range(10, 14):
   for i in range(2, num):
       if num%i == 1:
          print(num)
          break

x = 0
while (x < 100):
  x+=2
print(x)

for l in 'Jhon':
   if l == 'o':
      pass
      print(l, end=", ")


x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    print(x)

a, b = 12, 5
if a + b:
    print('True')
else:
  print('False')



x = 0
a = 0
b = -5
if a > 0:
    if b < 0:
        x = x + 5
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

for num in range(-2,-5,-1):
    print(num, end=", ")

