students= ['Nisrine', 'Amal', 'Mido', 'Alex', 'Tata', 'Idriss', 'Najat', 'Nadia', 'May', 'Nass']
gender  = [   'F'   ,   'F' ,  'M'  ,   'M' ,  'F'  ,    'M'  ,  'F'   ,   'F'  ,  'M'  ,  'M' ]
groups  = [    3    ,    1  ,   1   ,    3  ,   3   ,     1   ,   2    ,    2   ,   1   ,   3  ]
#notes   = {'DS': length of DS is the number of DS
#                  The element of each DS is the mark of each student
#           'TP': length of TP is the number of TP
#                  The element of each TP is the mark of each student
notes   = {'DS' : [[36, 58, 46, 96, 9, 82, 83, 66, 35, 47],
                   [46, 50, 55, 21, 22, 76, 51, 90, 96, 48],
                   [56, 54, 53, 17, 31, 74, 11, 53, 98, 67],
                   [77, 38, 8, 74, 39, 39, 52, 66, 38, 86],
                   [93, 21, 7, 33, 10, 97, 48, 96, 24, 7],
                   [97, 98, 95, 75, 64, 9, 48, 51, 45, 82]],

           'TP': [[48, 63, 98, 47, 25, 90, 100, 21, 41, 44],
                  [73, 79, 78, 39, 11, 100, 57, 96, 13, 99],
                  [93, 21, 7, 33, 10, 97, 48, 96, 24, 7],
                  [46, 50, 55, 21, 22, 76, 51, 90, 96, 48]]}
#---------------------------------------------------------------------------------------------------
# attendance = { Day : [ Duration_session : [ delay of 10 sessions]]}
attendance = {'Monday'    : [60, [3, 31, 1, 56, 15, 49, 48, 20, 2, 38]],
              'Tuesday'   : [120,[8, 3, 2, 7, 5, 9, 4, 0, 6, 1]],
              'Wednesday' : [60, [2, 7, 14, 6, 9, 15, 12, 13, 10, 0]],
              'Friday'    : [120,[12, 50, 0, 15, 11, 10, 3, 6, 14, 2]]}
#---------------------------------------------------------------------------------------------------
# min_att = {Attendance_statut : Late_Minute}
min_att = {'Present': range(0,1,1), 'Late' : range(1,6,1), 'Absent': range(6,180,1)}
# dic_att = { Attendance_statut : rate}
dic_att = {'Present': 1.0, 'Late': 0.96, 'Absent': 0.9}
# q1 : names of the female students
l=[]
for i in range(len(students)):
    if gender[i]=='F':
        l.append(students[i])
print(l)

# q3 : student's names with no absences
for i in range(len(attendance['Monday'][1])):
    if attendance['Monday'][1][i] in min_att['Present'] or attendance['Monday'][1][i] in min_att['Late'] :
        print(students[i])

# q2 : the number of members of each grp
dict1={1:[],2:[],3:[]}
l1=[]
for i in range(len(students)):
    dict1[groups[i]].append(students[i])
print(dict1)

# q4 : students' names that validate  one tp at least
mat1=[[0 for i in range(len(notes['TP']))]for j in range(len(notes['TP'][0]))]
for i in range(len(notes['TP'])):
    for j in range(len(notes['TP'][i])):
        mat1[j][i]=notes['TP'][i][j]
print(mat1)
for i in range(len(mat1)):
    if any(j>=60 for j in mat1[i]):
        print(students[i])

# q5 : average mark of ds for students in each grp
def sumi(group):
    s=0
    for i in range(len(groups)):
        if groups[i]==group:
            s+=1
    return s
dict6={1:0,2:0,3:0}
mat2=[[0 for i in range(len(notes['DS']))]for j in range(len(notes['DS'][0]))]
for i in range(len(notes['DS'])):
    for j in range(len(notes['DS'][i])):
        mat2[j][i]=notes['DS'][i][j]
print(mat2)
l2=[]
for i in range(len(mat2)):
    sum1=sum(mat2[i])
    sum1/=len(mat2[0])
    l2.append(sum1)
print(l2)
for i in range(len(l2)):
    dict6[groups[i]]+=l2[i]
for k in range(1,4):
    dict6[k]/=sumi(k)
print(dict6)

# q6 : print the mean mark of tps for each student
dict1={}
for j in range(len(notes['TP'][0])):
    s=0
    for i in range(len(notes['TP'])):
        s+=notes['TP'][i][j]
    av=s/len(notes['TP'])
    dict1[students[j]]=av
print(dict1)

# q7 : the minimum mark of tps for each gender in each group
dict8 = {1:{'F':0,'M':0},2:{'F':0,'M':0},3:{'F':0,'M':0}}
res8=[[0 for i in range(len(notes['TP']))] for j in range(len(notes['TP'][0]))]
for i in range(len(notes['TP'])):
    for j in range(len(notes['TP'][0])):
        res8[j][i]=notes['TP'][i][j]
l9=[]
for i in range(len(res8)):
    min1=min(res8[i])
    l9.append(min1)
for k in range(1,4):
    l=[]
    l1=[]
    for j in range(len(l9)):
        if groups[j] == k and gender[j] == 'F':
            l.append(l9[j])
        elif groups[j] == k and gender[j] == 'M':
            l1.append(l9[j])
    if len(l) !=0  :
        dict8[k]['F'] = min(l)
    if len(l1) != 0:
        dict8[k]['M'] = min(l1)
print(dict8)


# q8 : for each grp , print the students' names that validated
# each tp
for i in range(len(res8)):
    if all(x>=60 for x in res8[i]):
        print(students[i])

# q9 : for each student print the mean mark of ds
dict0={}
for i in range(len(mat2)):
    sum1=sum(mat2[i])
    av=sum1/len(mat2[i])
    dict0[students[i]]=av
print(dict0)

# q10 : identify and list the names of students who have shown improvement
# in their marks
for i in range(len(res8)):
    for j in range(0,2):
        if any(x<=y and y<=z for x,y,z  in zip(res8[i][j:],res8[i][j+1:],res8[i][j+2:])):
            print(students[i])

# q11 : for each student calculate the final mark based on the following formula
from statistics import median