dic_delay = {range(0,1):"present" ,
             range(1, 6):"late",
             range(6, 180):"absent"
             }

class Attendance:
    def __init__(self,total_minutes,late_minutes,days):
        self.total_minutes = total_minutes
        self.late_minutes = late_minutes
        self.days=days  # day of the week
        self.status = self.get_attendance_status(self.late_minutes)
    def get_ttl_min(self):
        return self.total_minutes
    def set_ttl_min(self,total_minutes):
        self.total_minutes=total_minutes
    def get_late(self):
        return self.late_minutes
    def set_late(self,late_minutes):
        self.late_minutes=late_minutes
    def get_days(self):
        return self.days
    def set_days(self,days):
        self.days=days
    def get_status(self):
        return self.status
    def get_late(self):
        return self.late_minutes
    def set_latemin(self,late_minutes):
        self.status = self.get_attendance_status(self.late_minutes)
        self.late_minutes=late_minutes
    def get_attendance_status(self,minutes):
        for i in dic_delay :
            if minutes in i :
                return dic_delay[i]
import random
class assessement:
    used_ids=[]
    def __init__(self, type, grade):
        self.type = type
        self.grade = grade
        self.ID = self.get_unique_id()
    def get_type(self):
        return self.type
    def set_type(self,type):
        self.type=type
    def get_grade(self):
        return self.grade
    def set_grade(self,grade):
        self.grade=grade
    def get_id(self):
        return self.ID
    def set_id(self,ID):
        self.ID=self.get_unique_id()
    def get_unique_id(self):
        id_generated=random.randint(0,2**12)
        # we use assessement.used_ids instead of used_ids
        # because this list is defined outside the function
        while id_generated in assessement.used_ids :
            id_generated = random.randint(0,2**12)
        assessement.used_ids.append(id_generated)
        return id_generated

class students :
    def __init__(self,name,gender,group):
        self.name=name
        self.gender=gender
        self.group=group
        self.subject_grades={}
        self.attendance={}
    def get_name(self):
        return self.name
    def set_name(self,name):
        self.name=name
    def get_gender(self):
        return self.gender
    def set_gender(self,gender):
        self.gender=gender
    def get_grp(self):
        return self.group
    def set_grp(self,group):
        self.group=group
    def add_subject_grades(self,subject,assessment_type,grade):
        if subject not in self.subject_grades :
            self.subject_grades[subject]=[]
        self.subject_grades[subject].append(assessement(assessment_type,grade))
    def add_attendance(self,subject,total_min,late_min,day):
        if subject not in self.attendance:
            self.attendance[subject]=[]
        self.attendance[subject].append(Attendance(total_min,late_min,day))
    def print_info(self):
        print("\nName : ",self.name,
              "\nGender : ",self.gender,
              "\nGroup : ",self.group)
        print("\nGrades : ")
        types = ["TP", "TD", "Exam", "Quiz"]
        for subject , ass in self.subject_grades.items():
            print(subject ,":")
            l1 = {i: [] for i in types}
            for i in ass :
                for itype in types :
                    if i.type == itype:
                        l1[itype].append((i.ID,i.grade))
            for i in l1 :
                if l1[i] == []:
                    continue
                else :
                    print(i,l1[i])
        dict1={}
        print("\nAttendances : ")
        for subject, att in self.attendance.items():
            print(subject)
            dict1 = {}
            for attendance in att:
                dict1[attendance.days] = attendance.status
            for i in dict1:
                print("-",i,":",dict1[i],"(delay:", attendance.late_minutes ,"minutes)")

student1 = students("John", "Male", "A")
student1.add_subject_grades("Math", "Exam", 90)
student1.add_subject_grades("Math", "Quiz", 85)
student1.add_subject_grades("Physics", "Exam", 88)
student1.add_subject_grades("Physics", "Quiz", 82)

student1.add_attendance("Math", 180, 5, "03/12")
student1.add_attendance("Physics", 180, 5, "04/12")
student1.print_info()







