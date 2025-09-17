import sys
from time import sleep
import time

def printlyrics():
    print("\n\n")
    lines = [
        ("You know, Yoou know", 0.15),
        ("You know where you are with", 0.13),
        ("You know where you are with", 0.13),
        ("Floor collapsing", 0.1),
        ("Floating, bouncing back", 0.15),
        ("And one day", 0.2),
        ("Am gonna Grow Wings", 0.15),
        ("A chemical Reaction", 0.17),
        ("Historical and Useless", 0.17),
         ("Let down and hanging around", 0.15),
        ("Crushed like a bug in the ground", 0.15),
        ("Let down and hanging around", 0.15),
    ]
    delays = [0.2, 1.5, 1.1, 0.5, 0.5, 1.0, 1.0, 5.0, 2.0, 1.5, 1.5, 2.0]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            sleep(char_delay)
        print()  # new line after the whole line
        time.sleep(delays[i])

printlyrics()
