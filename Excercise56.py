class Employee:
    companyname = "Apple"
    noofemployees = 0
    def __init__(self, name):
        self.name = name
        self.raise_amount = 0.02
        Employee.noofemployees += 1
        
    def showDetails(self):
      print(f"The name of the Employee is {self.name} and the raise amount in {self.noofemployees} sized {self.companyname} is{self.raise_amount}")

emp1 = Employee("Anum")
emp1.raise_amount = 0.3
emp1.companyname = "apple PAKISTAN"
emp1.showDetails()
emp1.companyname ="Google"
print(Employee.companyname)
emp2 = Employee("Amna")
emp2.companyname ="Nestle"
emp2.showDetails()
# Employee.showDetails(emp1)