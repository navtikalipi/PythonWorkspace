class Employee:
    def __init__(self, name=None, emp_id=None, salary=None): #To not have missing parameters, put =None
        self.name = name
        self.emp_id = emp_id
        self.salary=salary

    def show_details(self):
        return "The employee details are:", self.emp_id, self.name, self.salary
        

# emp= Employee()
# print(type(emp))
# print(emp.id)

emp1=Employee("Rashid",101, 7889999)
#print(emp1.show_details())
emp2=Employee("Navtika",102,1200000)
#print(emp2.show_details())
emp3=Employee("Aman",103,5728017)
#print(emp3.show_details())

# emps =[emp1, emp2, emp3]

# emp3=Employee(102,"kavita",1788888)

# flag=False
# for item in emps:
#     if (item.emp_id==emp3.emp_id):
#         print("Already exists")
#         flag=True
#         break

# if not flag:
#     emps.append(emp3)

# for item in emps:
#     print(item.show_details())

#convert into set use add(), it is unordered and change the brackets

#Convert into dictionary
emps = {}

emps[emp1.emp_id] = emp1
emps[emp2.emp_id] = emp2
emps[emp3.emp_id] = emp3 

for item in emps.values():
    print(item.show_details())


emp4 = Employee("kavita", 102, 1788888)

flag = False

for key in emps:
    if key == emp4.emp_id:
        print(key, "already exists")
        flag = True
        break

if not flag:
    emps[emp4.emp_id] = emp4

