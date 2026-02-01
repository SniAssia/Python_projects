# open txt to read from
handle = open("bill.txt", "r")
l3=[]
for i in handle:
    L = i.split()
    l3.append(L)
l4 = l3[1:]
print(l4)

# total of items
sum = 0
for i in range(len(l4)):
    sum = sum + float(l4[i][1])
print("The total is", sum)
# find the number of items in this file
print("There are total of", len(l3)-1, "items purchased.")
# find the most and the least expensive
l5=[]
for i in range(len(l4)):
    l5.append(float(l4[i][1]))
    l5.sort()
print("The most expensive item is", l5[-1])
print("The least expensive item is  ", l5[0])
# close bill.txt