class Employee:
    def __new__(cls, *args):
        print("Object created")
        return super().__new__(cls)
    def __init__(self, name=None, emp_id=None, salary=None): #To not have missing parameters, put =None
        print("Initialization happens")
        self.name = name
        self.emp_id = emp_id
        self.__salary=salary #use double underscore to make it private, private properties cannot be inherited
    
    def get_id(self):
        return self.__salary #Implemented in the parent class in order to use the private salary


    def show_details(self):
        return "The employee details are:", self.emp_id, self.name, self.salary