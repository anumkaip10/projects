class Employee:
    def __init__(self):
        self.__name = "AK"


a = Employee()
# print(a.__name) cannot be accessed directly
print(a._Employee__name) 
# can be accessed directly
print(a.__dir__())