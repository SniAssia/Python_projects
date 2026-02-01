max_days = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
                    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

def format_date(month_day):
    """
    Formats a date string to ensure that both the month and day are zero-padded to two digits.

    This function takes a date string in 'month/day' format and returns it with each component (month and day)
    zero-padded to two digits if necessary. This is commonly used to maintain consistency in date formats
    throughout an application, especially for storage and comparison purposes.
    Args:
        month_day (str): A string representing a date, expected to be in 'month/day' format where
                         both month and day can be one or two digits.

    Returns:
        str: The formatted date string where both month and day are zero-padded to two digits.

    Examples:
        >>> format_date("1/1")
        '01/01'
        >>> format_date("12/31")
        '12/31'
        >>> format_date("9/11")
        '09/11'
    """
    parts = month_day.split('/')
    month, day = parts
    return f"{int(month):02d}/{int(day):02d}"


import random
dic_delay = {range(0, 1): "Present", range(1, 6): "Late", range(6, 180): "Absent"}

class Attendance:
    def __init__(self, total_minutes, late_minutes, day):
        self.set_total_minutes(total_minutes)
        self.set_late_minutes(late_minutes)
        self.set_day(day)
        self.status = self.get_attendance_status()

    def get_attendance_status(self):
        for delay_range, status in dic_delay.items():
            if self.late_minutes in delay_range:
                return status
        return "Absent"

    def get_total_minutes(self):
        return self.total_minutes

    def set_total_minutes(self, value):
        self.total_minutes = value

    def get_late_minutes(self):
        return self.late_minutes

    def set_late_minutes(self, value):
        self.late_minutes = value
        self.status = self.get_attendance_status()

    def get_day(self):
        return self.day

    def set_day(self, value):
        self.day = format_date(value)

    def get_status(self):
        return self.status

class Assessment:
    used_ids = set()
    def __init__(self, assessment_type, grade):
        self.set_assessment_type(assessment_type)
        self.set_grade(grade)
        self.id = self.generate_id()

    def generate_id(self):
        while True:
            assessment_id = random.randint(0, 2**12)
            if assessment_id not in Assessment.used_ids:
                Assessment.used_ids.add(assessment_id)
                return assessment_id

    def get_id(self):
        return self.id

    def get_assessment_type(self):
        return self.assessment_type

    def set_assessment_type(self, value):
        self.assessment_type = value

    def get_grade(self):
        return self.grade

    def set_grade(self, value):
        self.grade = value


class Student:
    ass_types = ["TD", "TP", "Quizz", "Exam"]

    def __init__(self, name, gender, group):
        self.set_name(name)
        self.set_gender(gender)
        self.set_group(group)
        self.subject_grades = {}
        self.attendance = {}

    def get_name(self):
        return self.name

    def set_name(self, value):
        self.name = value

    def get_gender(self):
        return self.gender

    def set_gender(self, value):
        self.gender = value

    def get_group(self):
        return self.group

    def set_group(self, value):
        self.group = value

    # ------------------------------------------------------------------------------------------------------------------------------
    def add_subject_grades(self, subject_name, assessment_type, grade):
        if subject_name not in self.subject_grades:
            self.subject_grades[subject_name] = []
        self.subject_grades[subject_name].append(Assessment(assessment_type, grade))

    def add_attendance(self, subject_name, total_minutes, late_minutes, day):
        if subject_name not in self.attendance:
            self.attendance[subject_name] = []
        self.attendance[subject_name].append(Attendance(total_minutes, late_minutes, format_date(day)))

    # ------------------------------------------------------------------------------------------------------------------------------
    # GET GRADES & ATTENDANCE SUBJECT
    def get_grades_subject(self, subject_name):
        if subject_name not in self.subject_grades:
            print(f"{self.name} is not registered for {subject_name}.")
            return

        print(f"{subject_name} Grades:")
        for assessment_type in Student.ass_types:
            grades = [(a.get_id(), a.get_grade()) for a in self.subject_grades[subject_name] if
                      a.get_assessment_type() == assessment_type]
            if grades:
                print(f"  - {assessment_type}: {grades}")
    def get_attendance_subject(self, subject_name):
        if subject_name in self.attendance:
            attendance_records = self.attendance[subject_name]
            print(f"{self.name}'s {subject_name} attendance")
            for attendance in attendance_records:
                print(
                    f"  - {attendance.get_day():6}: {attendance.get_status():8} (Delay: {attendance.get_late_minutes()} minutes)")
        else:
            print(f"{self.name} is not registered for {subject_name}.")
    # ------------------------------------------------------------------------------------------------------------------------------
    # ASSESSMENT
    def modify_assessment_by_id(self, subject_name, assessment_id, new_grade):
        # Error handling for subject_name
        if subject_name not in self.subject_grades:
            print(f"{self.name} is not registered for {subject_name}.")
            return
        # Error handling for assessment_id
        assessment = None
        for a in self.subject_grades[subject_name]:
            if a.get_id() == assessment_id:
                assessment = a
                break
        if not assessment:
            print(f"No assessment with ID {assessment_id} found for {self.name} in {subject_name}.")
            return
        # Error handling for new_grade
        if new_grade < 0 or new_grade > 20:
            print("Invalid grade. It must be between 0 and 20.")
            return
        # If all parameters are valid, modify the assessment
        assessment.set_grade(new_grade)

    def remove_assessment_by_id(self, subject_name, assessment_id):
        if subject_name not in self.subject_grades:
            print(f"{self.name} is not registered for {subject_name}.")
            return

        initial_count = len(self.subject_grades[subject_name])
        self.subject_grades[subject_name] = [a for a in self.subject_grades[subject_name] if
                                             a.get_id() != assessment_id]

        if initial_count == len(self.subject_grades[subject_name]):
            print(f"No assessment with ID {assessment_id} found for {self.name} in {subject_name}.")
    # ------------------------------------------------------------------------------------------------------------------------------
    # GET GRADES & ATTENDANCE ALL SUBJECTS
    def get_subject_grades(self):
        if self.subject_grades=={}:
            print("no grades records found for ",self.name)
        for subject in self.subject_grades:
            print(Student.get_grades_subject(self, subject))
    def get_attendance(self):
        if self.attendance =={}:
            print("no attendance record found for  ", self.name)
        for att in self.attendance :
            print(Student.get_attendance_subject(self, att))
    # ------------------------------------------------------------------------------------------------------------------------------
    # ATTENDANCE
    def modify_attendance_by_day(self, subject_name, day, new_late_minutes):
        if subject_name not in self.attendance :
           print(self.name, "is not registered for ", subject_name)
        attendance =  None
        for att in self.attendance[subject_name]:
            l=att.get_day().split()
            l1=[i for i in range(10)]
            if not (l[0] in l1 and l[1] in l1 and l[2] =="/" and l[3] in l1 and l[4] in l1 ):
                print("invalid format of day ")
            if not ((l[0]== 0 or l[0] == 1 ) and (l[1] in l1 )):
                print("invalid month")
            if att.get_late_minutes() < 0 :
                print("late minutes cannot be negative ")
            if att.get_late_minutes() > att.get_total_minutes() :
                print("false ")
            if att.get_day() == day :
                attendance= att
        if not attendance :
            print("day not found ")
        attendance.set_late_minutes(new_late_minutes)
    def remove_attendance_by_day(self, subject_name, day):
        # self.attendance[subject_name].append(Attendance(total_minutes, late_minutes, format_date(day)))
        if subject_name not in self.attendance :
            print(self.name, "is not registered for ",subject_name)
        initial = len(self.attendance[subject_name])
        self.attendance[subject_name]=[a for a in self.attendance[subject_name] if a.get_day() != day  ]
        if initial==len(self.attendance[subject_name]):
            print("day not found" )



# Instantiate a Student
ahmed = Student("Ahmed", "Male", "B")

# Add attendance records for the subject 'LBD2' with dates in 'month/day' format
ahmed.add_attendance("LBD2", 120, 4, "1/10")
ahmed.add_attendance("LBD2", 90, 20, "1/1")
ahmed.add_attendance("LBD2", 120, 0, "12/10")

# Display initial attendance records to verify correct setup
ahmed.get_attendance_subject("LBD2")
ahmed.get_attendance_subject("LBD2")
ahmed.remove_attendance_by_day("LBD2", "12/10")
# Attempt to remove attendance with an incorrect day
ahmed.remove_attendance_by_day("LBD2", "2/29")
ahmed.get_attendance_subject("LBD2")


