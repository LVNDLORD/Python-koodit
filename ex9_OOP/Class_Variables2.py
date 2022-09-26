# class vars are vars that are shared among all instances of a class. Class var should be the same for each instance
# while instance variables can be unique for each instance like name, email, pay.
class Employee:

    num_of_employees = 0
    raise_amount = 1.04  # raise 4 percent. Class variable

    def __init__(self, e_first, e_last, e_pay):
        self.first = e_first
        self.last = e_last
        self.pay = e_pay
        self.email = e_first + '.' + e_last + '@company.com'

        Employee.num_of_employees += 1  # Using Employee instead of self, because constant class value can be overridden
        # per instance if needed to. So total num of employees will be the same for all the instances. By using self,
        # we can make this num different for various instances, but no point in that.

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)  # when we access class vars, we need to access via
                                                    # class name "Employee.raise_amount" - 1.04,
                                                    # or via instance of a class "self.raise_amount" - 1.04
        # can give different results based on "Employee.raise_amount" or "self.raise_amount", as to instance may
        # be assigned different attribute !!!
# using self.raise_amount also will allow any subclass, to override that constant if they wanted to

emp_1 = Employee('Corey', 'Schafer', 50_000)
emp_2 = Employee('Test', 'User', 60_000)

# When we try to access an attribute on an instance "emp_1.raise_amount", it will first check if an instance contains
# that attribute. If it doesn't, it will see if the class, or any class it inherits from contains that attribute
#  So when we access "raise_amount" from "emp_1/2.raise_amount", they don't have itself.
#  They (instances) access the class's "raise_amount" attribute

# print(emp_1.__dict__)   # returning a dictionary of emp_1. No "raise_amount"
# print(Employee.__dict__)  # returning a dict of emp_1. "raise_amount" present. Value that our instances see and access
# print(Employee.raise_amount)     # 1.04
# print(emp_1.raise_amount)     # 1.04
# print(emp_2.raise_amount)     # 1.04

# emp_1.raise_amount = 1.05  # ! This assignment created a raise_amount attribute within emp_1
#                             # it finds it within own namespace and returns that value BEFORE SEARCHING THE CLASS !
# print(emp_1.raise_amount) # 1.05. When raise applied, it's using emp_1 raise amount (1.05) instead of class raise amount (1.04)
# print(emp_1.__dict__)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

print(Employee.num_of_employees) # 2 It was incremented twice when we instantiated both of our employees on lines 29-30
