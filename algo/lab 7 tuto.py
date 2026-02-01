
#q1
#link every single login to its password using a dictionary
dict = {"Salem":"12345","Youssef":"password","Amal":"Brown"}
#asking the user to enter its login
login = input("enter your login :")
newlogin = login.capitalize()
#asking the user to enter its password
password = input("enter your password :")
#cheking if they are true or wrong
if newlogin in dict and password == dict[login]:
    print("Welcome ,", login)
elif newlogin in dict and password != dict[login]:
    print('Wrong Password')
else :
    print("Your login isn't available")

#q3
#how to merge two dictionaries
#display the first dictionary where we will store its values
dict1 = {}
n = int(input("Enter the number of pairs of Key-value:"))
#asking the user to enter the keyvalues and the values
for i in range (n):
    keyvalue = int(input("Enter a value for the key"+str(i+1)+":"))
    value = int(input("Enter a value for the value"+str(i+1)+":"))
    dict1[keyvalue]=value
#display dict1
print(dict1)
#repeating the same steps for the second dictionary
dict2 = {}
p = int(input("Enter the number of pairs of Key-value:"))
for j in range (p):
    keyvalue2 = int(input("Enter a value for the key"+str(j+1)+":"))
    value2 = int(input("Enter a value for the value"+str(j+1)+":"))
    dict2[keyvalue2]=value2
print(dict2)
#displaying a third dictionary where we will store the values of the merged dictionary
merged_dict= {}
#adding all dict1 elements to the merged dictionary
for x in dict1:
    merged_dict[x]=dict1[x]
#checking if they keyvalues are equal if they are , we ask the user to add their values
for x in dict2 :
    if x in merged_dict:
        merged_dict[x]+=dict2[x]
    else :
        merged_dict[x]=dict2[x]
#displaying the merged dictionary
print(merged_dict)

#q4
#column sum of a 2D list
rows = int(input("enter the number of rows :"))
columns = int(input("enter the number of columns :"))
matrix = []
mylist = []
for i in range (rows):
    matrix.append([])
    for j in range (columns):
        num = int(input("enter a value for row"+str(i)+",column"+str(j)+":"))
        matrix[i].append(num)
#create a list where the sum of columns will be stored
sum_columns = []
#calclating the sum of columns by adding every single value that display at the same column 
for i in range (columns):
    sum_columns.append(0)
for i in range(columns):
    for k in range(rows):
        sum_columns[i] += matrix[k][i]

print(sum_columns)

#q2
#initialize the values of rows and columns of the two matrixes
column_1 = int(input("enter the number of column of the first matrix:" ))
row_1 = int(input("enter the number of rows in the first matrix:"))
column_2 = int(input("enter the number of column of the second matrix:"))
row_2 = int(input("enter the number of rows in the second matrix:"))
#check if the matrixes that the user enter can be multiplied or not
if column_1 != row_2:
    print("the matrix can not be multiplied , please enter different values for column1 and row2")
else :
#initialize empty lists where the matrixes will be stored
    matrix_1 = []
    matrix_2 = []
#combining between the two matrixes , its rows and its columns
    combine_matrix = [matrix_1,matrix_2]
    row_3 = [row_1, row_2]
    column_3 = [column_1,column_2]
#add elements to your list
    for a in range(0,2):
        for i in range(row_3[a]):
            list = []
            for j in range(column_3[a]):
                num = int(input("enter a number"+str(j+1)+"of matrix"+str(a+1)+":"))
                list.append(num)
            combine_matrix[a].append(list)
    combine_matrix = []
#check the process of multiplying matrixe's elements
    for b in range(row_1):
        row_3 = []
        for e in range (column_2):
            sum_1 = 0
            for k in range(column_1):
                sum_1 = sum_1 + matrix_1[b][k] * matrix_2[k][e]
            row_3.append(sum_1)
        combine_matrix.append(row_3)
#displaying the final matrix
    print("the result of multiplication of those matrixes is :",combine_matrix)





