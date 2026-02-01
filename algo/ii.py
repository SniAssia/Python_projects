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
