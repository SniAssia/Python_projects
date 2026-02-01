students= ['Nisrine', 'Amal', 'Mido', 'Alex', 'Tata', 'Idriss', 'Najat', 'Nadia', 'May', 'Nass']
gender  = ['F','F', 'M',   'M',  'F',    'M',  'F'   ,   'F'  ,  'M'  ,  'M' ]
groups  = [3,1,1,3,3,1,2,2,1,3  ]
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
attendance = {'Monday': [60, [3, 31, 1, 56, 15, 49, 48, 20, 2, 38]],
              'Tuesday': [120,[8, 3, 2, 7, 5, 9, 4, 0, 6, 1]],
              'Wednesday': [60, [2, 7, 14, 6, 9, 15, 12, 13, 10, 0]],
              'Friday': [120,[12, 50, 0, 15, 11, 10, 3, 6, 14, 2]]}
# min_att = {Attendance_statut : Late_Minute}
min_att = {'Present': range(0,1,1), 'Late' : range(1,6,1), 'Very Late': range(6,15,1), 'Absent': range(15,180,1)}
# dic_att = { Attendance_statut : rate}
dic_att = {'Present': 1.0, 'Late': 0.97, 'Very Late': 0.93, 'Absent': 0.9}
# q1:print the names of the members of group 3
l=[]
for i in range(len(students)):
    if groups[i]==3:
        l.append(students[i])
print(l)

#q2: print the number of each gender in each group
group_gender = {1 : {'F' : 0, 'M': 0},
                2 : {'F' : 0, 'M': 0},
                3 : {'F' : 0, 'M': 0}}

for i in range(len(groups)):
    group_gender[groups[i]][gender[i]] += 1
print(group_gender)
#q3: names of students who were absent during monday
l2=[]
for k in range(len(attendance['Monday'][-1])):
    if attendance['Monday'][-1][k]>=15:
        l2.append(students[k])
print(l2)
#q4:students who scored more than 50 marks in all their exams
l=[]
for i in range(len(notes['Exams'])):
    l3=[]
    for j in range(len(notes['Exams'][i])):
        if notes['Exams'][i][j]>=50:
            l3.append(students[j])
    l.append(l3)