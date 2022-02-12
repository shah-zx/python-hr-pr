class Employee:
    # The things inside this class will be its property only and it will be shared by its children:
    leaves = 10
    
    def Details(self):
        return f"salary is {self.salary} and department is {self.dept}"
    def __init__(self , asalary , adept , aid):
        asalary = asalary
        adept = adept
        aid = aid
        

shahnawaz = Employee()
hamza = Employee()




shahnawaz.salary = 500000
shahnawaz.dept = "Development"
shahnawaz.id = 32

hamza.salary = 400000
hamza.dept = "Management"
hamza.id = 30


# We cant change the leaves of the Employee class by any instance / object 

# shahnawaz.leaves = 10  this will change the leaves of the shahnawaz and not the employee class

# print(shahnawaz.leaves)

# print(Employee.__dict__)

print(shahnawaz.Details())

