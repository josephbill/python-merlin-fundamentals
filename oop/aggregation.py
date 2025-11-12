# one object contains another - but both exist independently 
# one to many : one Department has many employees - 'has a'
class Department:
    def __init__(self,name):
        self.name = name 
        self.employees = []  # direct initialization
        
    def add_employee(self, employee):
        self.employees.append(employee)
        
        
class Employee:
    def __init__(self, name):
        self.name = name
        
e1 = Employee("Joseph")
e2 = Employee("Jane")

it_department = Department("IT")
it_department.add_employee(e1)
it_department.add_employee(e2)

print([emp.name for emp in it_department.employees])