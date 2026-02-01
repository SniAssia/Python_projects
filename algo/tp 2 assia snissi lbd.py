students= ['Nisrine', 'Amal', 'Mido', 'Alex', 'Tata', 'Idriss', 'Najat', 'Nadia', 'May', 'Nass']
#---------------------------------------------------------------------------------------------------
gender  = [   'F'   ,   'F' ,  'M'  ,   'M' ,  'F'  ,    'M'  ,  'F'   ,   'F'  ,  'M'  ,  'M' ]
groups  = [3, 1, 1,3,3,1,2,2,1,   3  ]
#---------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------
#q1
l=[]
for i in range(len(students)):
    if gender[i]=='F':
        l.append(students[i])
print(l)
#q2
dict1={1:0,2:0,3:0}
dict1[1]=0
dict1[2]=0
dict1[3]=0
for i in range(len(students)):
    if groups[i]==1:
        dict1[1]+=1
    elif groups[i]==2:
        dict1[2]+=1
    elif groups[i]==3:
        dict1[3]+=1
print(dict1)
#q3
l=[]
for i in attendance :
    l1=[]
    for j in range(len(attendance[i][1])):
        if attendance[i][1][j] not in min_att['Absent'] :
            l1.append(students[j])
    l.append(l1)
c=l[0]
for i in range(len(l)):
    if len(l[i])<len(c):
        c=l[i]
print(c) # output
#q4
l7=[]
for i in range(len(notes['TP'])):
    l8=[]
    for j in range(len(notes['TP'][i])):
        if notes['TP'][i][j]>=60:
            l8.append(students[j])
    l7.append(l8)
l9=[]
for i in range(len(l7)):
    for j in range(len(l7[i])):
        if l7[i][j] not in l9:
            l9.append(l7[i][j])
print(l9) #output
#q5
dict={1:0,2:0,3:0}
for i in range(len(notes['DS'])):
    av=0
    av1=0
    av2=0
    for j in range(len(notes['DS'][i])):
        if groups[j]==1:
            av+=notes['DS'][i][j]
            av12=av/dict1[2]
            dict[1] = av12
        elif groups[j]==2:
            av1 += notes['DS'][i][j]
            av11=av1/dict1[1]
            dict[2]=av11
        elif groups[j]==3:
            av2+=   notes['DS'][i][j]
            av22=av2/dict1[3]
            dict[3]=av22
print(dict)
#q6
dict2={}
for j in range(len(notes['TP'][0])):
    sum=0
    for i in range(len(notes['TP'])):
        sum+=notes['TP'][i][j]
        average=sum/len(notes['TP'])
    dict2[students[j]]=average
print(dict2) #output
#q7
dict4={1:0,2:0,3:0}
for j in range(len(notes['TP'][0])):
    sum=0
    dict4[groups[j]]=0
    for i in range(len(notes['TP'])):
        sum+=notes['TP'][i][j]
        average=sum/len(notes['TP'])
        if groups[j]==1:
            dict4[groups[j]]+=average/dict1[1]
        elif groups[j]==2:
            dict4[groups[j]]+=average/dict1[2]
        elif groups[j]==3:
            dict4[groups[j]]+=average/dict1[3]
print(dict4) #output
#q8
l7=[]
for i in range(len(notes['TP'])):
    l8=[]
    for j in range(len(notes['TP'][i])):
        if notes['TP'][i][j]>=60:
            l8.append(students[j])
    l7.append(l8)
print(l7)
l=[]

