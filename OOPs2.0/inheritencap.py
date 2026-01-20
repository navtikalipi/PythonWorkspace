class Employee:
    def __init__(self, name, id, salary):
        self.__id=id
        self.__name=name
        self.__salary=salary

    def get_id(self):
        return "The id is", self.__id
    
    def show_details(self):
        print(self.__id, self.__name, self.__salary)
    
class Manager(Employee):
    def __init__(self, name, id, salary, no_of_teams):
        super().__init__(name, id, salary)
        self.__no_of_teams=no_of_teams

    def show_details(self): #same name as parent class method: method overriding
        super().show_details()
        print(self.__no_of_teams)

emp=Employee(1001,'xyz',52779)
emp.show_details()
mgr=Manager(101,'abc',26819,7)
mgr.show_details()