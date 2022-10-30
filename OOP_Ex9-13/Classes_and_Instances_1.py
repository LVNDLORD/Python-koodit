# (in vid) "data and functions that are associated with a specific class" - attributes and methods
# (in vid) "method" meaning a function associated with a class
# classes logically group our data and functions in a way its easy to reuse and build upon if needed

# class is a blueprint for creating instances
# each unique employee that we create using "Employee" class will be an instance of that class

class Employee:

    # init receiving instance a first argument automatically
    def __init__(self, e_first, e_last, e_pay):
        self.first = e_first
        self.last = e_last
        self.pay = e_pay
        self.email = e_first + '.' + e_last + '@company.com'

    def fullname(self):    # instance is passed automatically, so "self" should always be present
        return '{} {}'.format(self.first, self.last)


# passing the values we specify in the init method. __init__ automatically takes instance "emp_1" as "self",
# and "first, last, pay" as arguments to pass to attributes in a function
emp_1 = Employee('Corey', 'Schafer', 50_000)
emp_2 = Employee('Test', 'User', 60_000)

print(emp_1.email)


emp_1.fullname()       # same as "Employee.fullname(emp_1)". Instance and call the method
Employee.fullname(emp_1)  # Call a method using class name. But here need to path instance manually as an argument
# Method can be called from another class, as we specify the "Employee" class name



# print(emp_2.fullname())

print(Employee.fullname(emp_2))


