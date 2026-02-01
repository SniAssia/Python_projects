#a program to manipulate files
# open hello.txt to read from
handle = open ("sample.txt", "r")
count = 0
time = 0
for i in handle :
    l = i.split()
    for word in l :
        count = count + 1
        time = time + word.count("a") + word.count("A")
print(count)
print(time)
handle.close()

o = open("bill.txt","r")
for i in o :
    print(i)
dic={}
for i in o :
    L=[]
    i.split()
    L.append(i)


