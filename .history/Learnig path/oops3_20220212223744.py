class Employee:
    # The things inside this class will be its property only and it will be shared by its children:
    leaves = 10

    def Details(self):
        return f"salary is {self.salary} and department is {self.dept}"

    def __init__(self, asalary, adept):
        asalary = asalary
        adept = adept

    @classmethod
    def change_leaves(cls, newleaves):
        cls.leaves = newleaves

    @staticmethod
    def printgood(string):
        print("This is a string " + string)
        
        # A static method is also a method that is bound to the class and not the object of the class.
        # A static method can’t access or modify the class state.
        # It is present in a class because it makes sense for the method to be present in class.
        # It doesn't takes self as an argument ,it works idependently 


# shahnawaz = Employee()
# hamza = Employee()


# shahnawaz.salary = 500000
# shahnawaz.dept = "Development"
# shahnawaz.id = 32

# hamza.salary = 400000
# hamza.dept = "Management"
# hamza.id = 30


# We cant change the leaves of the Employee class by any instance / object

# shahnawaz.leaves = 10  this will change the leaves of the shahnawaz and not the employee class

# print(shahnawaz.leaves)
# print(Employee.__dict__)
# print(shahnawaz.Details())



harry = Employee(200000, "dev")

print(harry.Details)

Employee.printgood("Shahnawaz")


# Inheritance :

class Programmer(Employee):
    def printprog(self):
        return f"Programmer is : {self.salary}".format(self.dept)
        
    pass

shahnawaz = Employee(200000, "dev")
hamza = Programmer(300000 , "flutter dev")

print(shahnawaz.printprog())



