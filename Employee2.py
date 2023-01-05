class Employee2:
    num_of_emp = 0
    raise_amt = 1.04

    def __int__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #self.email = email
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):  # create another method and call it from the print
        return '{} {} {}'.format(self.first, self.last, self.email)

    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amt)

    @classmethod  # this method is call decorator
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod  # create alternative contructore
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # static method dont take any instance parameters
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee2()
emp_2 = Employee2()

emp_str1 = 'Ako-Atem-3000'
emp_str2 = 'Ben-Suh-4857'
emp_str3 = 'Waley-Grey-7473'

# first, last, pay = emp_str1.split('-')
# new_emp_1 = Employee(first, last, pay)
#new_emp_1 = Employee.from_str(emp_str1)  #the use of class method as altinative contructor

#print(new_emp_1.email)
#print(new_emp_1.pay)

Employee2.set_raise_amt(1.05)  # to change the raise amount
emp_1.set_raise_amt(1.90)  # you can still increase it from class variable

print(Employee2.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

import datetime

my_date = datetime.date(2001, 7, 10)
print(Employee2.is_workday(my_date))

# (emp_1.fullname())  #this is print for both emp1 and emp2
# print(emp_2.fullname())
# you can call the method by passing the class
# emp_1.fullname()
# print(Employee.fullname(emp_1))

# emp_2.fullname()
# print(Employee.fullname(emp_2))
