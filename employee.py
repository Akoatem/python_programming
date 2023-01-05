
class Employee:
    def __int__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):  # create another method and call it from the print
        return '{} {} {}'.format(self.first, self.last, self.email)
    # this can be return value for both emp1 and emp2


emp_1 = Employee("ako", "atem", 2300)
emp_2 = Employee("akoen", "batem", 2700)

# (emp_1.fullname())  #this is print for both emp1 and emp2
# print(emp_2.fullname())
# you can call the method by passing the class
emp_1.fullname()
print(Employee.fullname(emp_1))

emp_2.fullname()
print(Employee.fullname(emp_2))

# print('{} {} {}'.format(emp_1.first, emp_1.last, emp_1.email))
# print('{} {} {}'.format(emp_2.first, emp_2.last, emp_2.email))
# crate instance variables
# the init method will be passed automatically

# print(emp_1.email)
# print(emp_2.email)


# this is the manula way of doing it
""" 
 emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

#attributes for instamce variables
emp_1.first = "Ako"
emp_1.last = "Sampson"
emp_1.email = "ako.sampson@gmail.com"
emp_1.pay = 10000

emp_2.first = "Beson"
emp_2.last = "David"
emp_2.email = "beson.david@gmail.com"
emp_2.pay = 10000

print(emp_1.email)
print(emp_2.email)"""