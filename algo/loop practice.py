count = 0
sum = 0
num = int(input("enter a number :"))
while count < num :
    count = count + 1
    sum = sum + count
print(sum)




count = 0
positiveNum = 0
negativeNum= 0
divisible_2 =0
divisible_5=0
while count < 5:
    count = count + 1
    num = int(input("enter a number :"))
    if num>0 :
        positiveNum = positiveNum +1
    elif num<0:
        negativeNum = negativeNum + 1
    elif num%2 ==0 :
        divisible_2 = divisible_2 + 1
    elif num%5 ==0:
        divisible_5 = divisible_5 + 1
print(positiveNum)
print(negativeNum)
print(divisible_2)
print(divisible_5)


count = 0
result = 0
n = int(input("enter a number :"))
while count < n :
    count = count + 1
    result = result + count
print(result)

for i in range(1, 6):
    print(' ' * (6 - i) + '#' * i)
