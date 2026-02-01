students= ['Nisrine', 'Amal', 'Mido', 'Alex', 'Tata', 'Idriss', 'Najat', 'Nadia', 'May', 'Nass']
gender  = [   'F'   ,   'F' ,  'M'  ,   'M' ,  'F'  ,    'M'  ,  'F'   ,   'F'  ,  'M'  ,  'M' ]
groups  = [    3    ,    1  ,   1   ,    3  ,   3   ,     1   ,   2    ,    2   ,   1   ,   3  ]
# 'notes' is a dictionary where each key is a string representing the type of assessment,
# and its value is a list of lists. Each inner list contains numeric scores.
notes = {
    # 'Exams' key contains a list of lists, where each inner list represents the scores of a particular exam.
    'Exams': [
        [36, 58, 46, 96, 9, 82, 83, 66, 35, 47],   # Scores from exam 1
        [46, 50, 55, 21, 22, 76, 51, 90, 96, 48],  # Scores from exam 2
        [56, 54, 53, 17, 31, 74, 11, 53, 98, 67],  # Scores from exam 3
        [77, 38, 8, 74, 39, 39, 52, 66, 38, 86],   # Scores from exam 4
        [93, 21, 7, 33, 10, 97, 48, 96, 24, 7],    # Scores from exam 5
        [97, 98, 95, 75, 64, 9, 48, 51, 45, 82]    # Scores from exam 6
    ],

    # 'TP' key contains a list of lists, where each inner list represents the scores of a particular practical session.
    'TP': [
        [48, 63, 98, 47, 25, 90, 100, 21, 41, 44],  # Scores from practical session 1
        [73, 79, 78, 39, 11, 100, 57, 96, 13, 99]   # Scores from practical session 2
    ]
}
# attendance = { Day : [ Duration_session : [Delay of the 10 students in each session]]}
attendance = {'Monday'    : [60, [3, 31, 1, 56, 15, 49, 48, 20, 2, 38]],
              'Tuesday'   : [120,[8, 3, 2, 7, 5, 9, 4, 0, 6, 1]],
              'Wednesday' : [60, [2, 7, 14, 6, 9, 15, 12, 13, 10, 0]],
              'Friday'    : [120,[12, 50, 0, 15, 11, 10, 3, 6, 14, 2]]}
# min_att = {Attendance_statut : Late_Minute}
min_att = {'Present': range(0,1,1), 'Late' : range(1,6,1), 'Very Late': range(6,15,1), 'Absent': range(15,180,1)}
# dic_att = { Attendance_statut : rate}
dic_att = {'Present': 1.0, 'Late': 0.97, 'Very Late': 0.93, 'Absent': 0.9}
# q1: name of members of grp 3
for i in range(len(students)):
    if groups[i]==3:
        print(students[i])
# q2: number of each gender in each grp
group_gender = {1 : {'F' : 0, 'M': 0},
                2 : {'F' : 0, 'M': 0},
                3 : {'F' : 0, 'M': 0}}
for j in range(1,4):
    for i in range(len(groups)):
        if groups[i]==j and gender[i] == 'F':
            group_gender[j]['F'] += 1
        elif groups[i]==j and gender[i] == 'M':
            group_gender[j]['M'] += 1
print(group_gender)
# q3: names of students who were absent for monday's session
for i in range(len(attendance['Monday'][1])):
    if attendance['Monday'][1][i] in min_att['Absent']:
        print(students[i])
# q4 : names of students who have scored more than 50 marks
# in all their exams
# we use all to check if all elements satisfy the condition
# we use any ti check if at least one function satisfy the condition
mat=[[0 for i in range(len(notes['Exams']))] for j in range(len(notes['Exams'][0]))]
for i in range(len(notes['Exams'])):
    for j in range(len(notes['Exams'][i])):
        mat[j][i]=notes['Exams'][i][j]
for i in range(len(mat)):
    if all(j>50 for j in mat[i]):
        print("the students are: ",students[i])
# q5 : the average mark of the exams for all students in
# each grp and print results
dict1={1:[],2:[],3:[]}
for k in range(1,4):
    for i in range(len(mat)):
        sum=0
        for j in range(len(mat[i])):
            sum+=mat[i][j]
        average=sum/len(mat[i])
        if groups[i]==k:
            dict1[k].append(average)
print(dict1)
# q6 : print the session for each grp that has the lowest delay in minutes
dict1={1 : {'Monday':0,'Tuesday':0,'Wednesday':0,"Friday":0},
    2 : {"Monday":0,"Tuesday":0,"Wednesday":0,"Friday":0},
    3 : {"Monday":0,"Tuesday":0,"Wednesday":0,"Friday":0}
}
l1=[]
dict5={1:[],2:[],3:[]}
for k in range(1,4):
    l=[]
    for i in attendance:
        for j in range(len(attendance[i][1])):
            if groups[j]==k:
                l.append(attendance[i][1][j])
                break
    dict5[k]=l
for k in range(1,4):
    for i ,day in enumerate(attendance):
        pivot=dict5[k][i]
        for j in range(len(attendance[day][1])):
            if groups[j]==k:
                if attendance[day][1][j]<pivot:
                    pivot=attendance[day][1][j]
        dict1[k][day]=pivot
print(dict1)
for i,j in dict1.items():
    pivot=j['Monday']
    for o,k in j.items():
        if k<pivot:
            pivot=k
            print(i,o)

# q7 : name of student with the lowest mark for each gender
# across all exams
for i in range(len(notes['Exams'])):
    pivot = notes['Exams'][i][2]
    pivot1 = notes['Exams'][i][0]
    for j in range(len(notes['Exams'][i])):
        if gender[j]=='F':
            if notes['Exams'][i][j] < pivot1:
                pivot1 = notes['Exams'][i][j]
        elif gender[j]=='M':
            if notes['Exams'][i][j] < pivot:
                pivot = notes['Exams'][i][j]
    print("for female ",i+1,"exam",students[notes['Exams'][i].index(pivot1)])
    print("for male ", i + 1, "exam", students[notes['Exams'][i].index(pivot)])

# q8 : average marks of the tps for each gender
s1=0
s2=0
for i in range(len(gender)):
    if gender[i] == 'F':
        s1 += 1
    elif gender[i] == 'M':
        s2 += 1
for i in range(len(notes['TP'])):
    sum1 = 0
    sum2 = 0
    for j in range(len(notes['TP'][i])):
        if gender[j] == 'F':
            sum1 += notes['TP'][i][j]
        else:
            sum2 += notes['TP'][i][j]
    av1=sum1/s1
    av2=sum2/s2
    print(av1)
    print(av2)

# q9 : student's name with an average mark of more than 80 in the tps and an
# attendance rate of more than 0.95
l1=[]
for i in attendance:
    l1.append(attendance[i][1])
res=[[0 for i in range(len(l1))] for j in range(len(l1[0]))]
for i in range(len(l1)):
    for j in range(len(l1[i])):
        res[j][i]=l1[i][j]
for j in range(len(notes['TP'][0])):
    s=0
    for i in range(len(notes['TP'])):
        s+=notes['TP'][i][j]
    av=s/2
    if av>80 and all(i in min_att['Present'] or i in min_att['Late'] for i in res[j]):
        print(students[j])

# q10 : name of the student who has the highest minutes of delay in
# the third session
