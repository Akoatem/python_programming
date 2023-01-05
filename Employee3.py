
class Employee3:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + '.' + last + '@gmail.com'

    @property             # this keep updating with manually doing it
    def email(self):      # use of property decorator to update details
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return 'Hi,{} {}, your salery is: ${}'.format(self.first, self.last, self.pay)

    @fullname.setter     # create a class fullname to setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter  # create a class fullname to deleter which delete the attribute
    def fullname(self):
        print("Delete name!")
        self.first = None
        self.last = None


emp1 = Employee3('benson', 'sam',4000)

emp1.first = 'Peter'

emp1.fullname = 'akoatem sampson'  # here we create a method setter
emp1.fullname = 'elizabeth kadewere'

del  emp1.fullname  # This delete the attribute

print(emp1.first)
print(emp1.email)       # accessing it like an attribute
print(emp1.fullname)    # removing the parathensis and access it like an attribute
