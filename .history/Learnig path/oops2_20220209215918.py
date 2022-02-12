class Employee:
    # The things inside this class will be its property only and it will be shared by its children:
    leaves = 10
    pass

shahnawaz = Employee()
hamza = Employee()

shahnawaz.salary = 500000
shahnawaz.dept = "Development"
shahnawaz.id = 32

hamza.salary = 400000
hamza.dept = "Management"
hamza.id = 30

print(shahnawaz.leaves)

