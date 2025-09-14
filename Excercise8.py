# Write a program to check if a character entered is a vowel or a consonant.
a = str(input("Enter character: ")).lower()
if a in ["a" ,  "e" , "i" , "o" , "u"]:
    print("Your Character is a Vowel!")
else:
    print(" Your character is Cononant!")