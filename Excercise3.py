# Ask the user for their marks, if marks 90 >= A grade, if 75, B grade, if grade 50, c grade else fail
b = int(input("Enter your marks:"))
if(b>=90):
    print(b,"You have A grade, Excellient!")
    print("Am proud of you")
elif(b>=75):
    print(b,"you have B grade, Nice Job!")
    print("Nice! keep it up!")
elif(b>=50):
    print(b,"you have C grade")
    print("Work hard, You can Do it!")
else:
    print("you are failed")
    print("don't lose hope you can do it!")