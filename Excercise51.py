class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
      print(f"The name of Employee: {self.id} is {self.name}")

class programmer(Employee):
   def showlanguage(Self):
      print("The default language is python")


e1 = Employee("Amna Ali", 400)
e1.showDetails()
e2 =programmer("Fatima Ali", 500)
e2.showDetails()
e2.showlanguage()