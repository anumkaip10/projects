with open('myfile12.txt', 'r') as f:
    lines = f.readlines()

if not lines:
    print("File is empty or missing!")
else:
    for i, line in enumerate(lines, start=1):
        parts = line.strip().split(',')
        if len(parts) == 3:
            m1, m2, m3 = parts
            print(f"marks of student {i} in Maths is: {m1}")
            print(f"marks of student {i} in English is: {m2}")
            print(f"marks of student {i} in Science is: {m3}")
        else:
            print(f" Line {i} format is wrong: {line}")
