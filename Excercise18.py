
students = { 
    "Ali": 80,
    "Mariyum": 45,
    "Ahmad": 90,
    "Fatima": 30,
    "Sana": 55,
    "Rida": 20,
    "Kamil": 10,
    "Farzana": 5,
    "Amna": 15,
    "Rabia": 0
}

passed = []
failed = []

for name, marks in students.items():
    if marks >= 50:
        passed.append(name)
    else:
        failed.append(name)

print("Passed Students:", passed)
print(" Failed Students:", failed)
