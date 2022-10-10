import random

#plays as the file given
class PlayerFile:
    def __init__(self, filename):
        self.file = open(filename, "r")
        self.value = ""

    def NextChoice(self):
        self.value = self.file.readline().strip()

class PlayerRandom:
    def __init__(self):
        self.value = ""
    #random choice
    def NextChoice(self):
        self.value = random.choice(["C","P","R"])

def Play():
    p1.NextChoice()
    p2.NextChoice()

    # calculates the value of the play (0 for loss, 1 for tie, 2 for win)
    if (p1.value == p2.value):
        print("both tie with " + p1.value)
    elif (p1.value == "C"):
        if (p2.value == "P"):
            print("p1 wins : p1 C; p2 P")
        else:
            print("p2 wins : p1 C; p2 R")

    elif (p1.value == "P"):
        if (p2.value == "R"):
            print("p1 wins : p1 P; p2 R")
        else:
            print("p2 wins : p1 P; p2 C")

    elif (p1.value == "R"):
        if (p2.value == "C"):
            print("p1 wins : p1 R; p2 C")
        else:
            print("p2 wins : p1 R; p2 P")

p1 = PlayerRandom()
p2 = PlayerFile("joueur400.txt")

f = open("test.txt", "x")


p2.NextChoice()
p1.NextChoice()
print(p1.value)

#plays the game a certain amount of times equal to the number in the file
for i in range(int(p1.value)):
    Play()
    f.write(p1.value + " " + p2.value + "\n")