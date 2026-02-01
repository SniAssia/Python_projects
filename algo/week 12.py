"""
mylist = ['monday','ok','b','hi','hello']
mylist.reverse()
print(mylist)
print(mylist.count('monday'))
print(len(mylist))
my_list = [11,22,34,2,9,8,67]
my_list.sort()
print(my_list)
list1 = ['monday','tuesday']
list2 = [1,7]
print(list1+list2)

#check if elements are in a list or not
list = ['sunday','tuesday','hoho']
print('sunday' in list)
print('u' in list[0])
print(44 not in list)

mylist = ['banana','peach','apple']
for x in mylist :
    print(mylist)
for x in range (len(mylist)):
    print(x)
    print('i like to eat' + mylist[x] + 's')


mylists = [1,10,16,15,17,18]
sum = 0
for i in range (len(mylists)) :
    sum = sum + mylists[i]
print(sum)
#size of a list
mylist = []
n = int(input("enter the size of this list ."))
for i in range (0,n):
    element = input("give element"+str(i)+":")
    list.append(element)
print(list)

listss = ['hi',10,67,67,10]
newlists =[]
for x in listss :
    if x not in newlists:
        newlists.append(x)
print(newlists)



#split lists elements
name = "school of computer science "
list4=name.split()
print(list4)
list5=name.split("o")
print(list5)
list6=name.split("ol")
print(list6)

sent = input("enter a sentence ")
list9=sent.split()
print(list9)
print(len(list9))
"""

list56=[3,130,24,64,152,182,73]
a = 0
newlist7=[]
for x in list56:
    if x > 100:
        newlist7.append(a)
    else :
        newlist7.append(x)
print(newlist7)


nlist = ['monday','tuesday','wednesday','ddd']
print(nlist[2])
print(nlist[2][3])
nlist[2]="tuesday"
print(nlist)

mx = [[1,2,3],[4,5,6],[7,8,9]]
for row in range (len(mx)):
    for cool in range (len(mx[row])):
        print(mx[row][cool],end = " ")
    print()
mx = [[1,2,3],[4,5,6],[7,8,9]]
for i in mx:
    for j in i:
        print(j , end = " ")
    print()
sum = 0
mx1 = [[6, 7, 9], [8, 7, 6], [7, 8, 9]]
for row in mx :
    for j in row :
        sum = sum + j
print(sum)

sum = 0
mx = [[1,2,3],[4,5,6],[7,8,9]]
for row in range (len(mx)):
    for cool in range (len(mx[row])):
        sum = sum + mx[row][cool]
print(sum)









