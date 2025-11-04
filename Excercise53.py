class student:
    def __init__(self):
        self._name = "AK"

    def _funName(self):
# protected method
         return "AI Engineer AK"
    
class Subject(student):
    # Inherited class
          pass

obj = student()
obj1 = Subject()

# calling by object student class
print(obj._name)
print(obj._funName())
# calling by object of subject class

print(obj1._name)
print(obj1._funName())