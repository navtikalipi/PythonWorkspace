class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


def get_marks(student):
    return student.marks


class Teacher:
    def __init__(self, name, students):
        self.name = name
        self.students = students   # HAS-A relationship

    def add_student(self, student):
        self.students.append(student)

    def process_students(self):

        print("Total students:", len(self.students))
        print()

        print("Division results:")
        distinction_count = 0
        for s in self.students:
            if s.marks > 70:
                division = "Distinction"
            elif s.marks >= 60:
                division = "1st Division"
            elif s.marks >= 50:
                division = "2nd Division"
            elif s.marks >= 40:
                division = "3rd Division"
            else:
                division = "Fail"

            if s.marks >= 75:
                distinction_count += 1

            print(s.name, s.marks, division)

        print()
        print("Students with marks >= 75:", distinction_count)

        print()
        print("Restricted students (marks below 20):")
        for s in self.students:
            if s.marks < 20:
                print(s.name, s.marks)

        print()
        print("Students sorted by marks (descending):")
        sorted_students = sorted(self.students, key=get_marks, reverse=True)
        for s in sorted_students:
            print(s.name, s.marks)


students = [
    Student("Aman", 82),
    Student("Rashid", 68),
    Student("Navtika", 95),
    Student("Kavita", 45),
    Student("Rohit", 18)
]

teacher = Teacher("Mr. Gupta", students)

teacher.add_student(Student("Neha", 76))

teacher.process_students()
