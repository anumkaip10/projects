class person:
    name = "AK"
    accupation = "AI Engineer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.accupation}")
a = person()
b = person()
a.name = "Anum"
a.accupation = "AI engineer"
b.name = "Amna"
b.accupation = "HR"
print(a.name, a.accupation)
print(b.name, b.accupation)
a.info()
b.info()