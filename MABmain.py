import random

#plays as the file given
class PlayerFile:
    def __init__(self, filename):
        self.file = open(filename, "r")
        self.value = ""

    def NextChoice(self):
        self.value = self.file.readline().strip()

class PlayerMAB:
    def __init__(self, eps):
        # RPC
        self.ChoiceCount = [0, 0, 0]
        self.ChoiceSum = [0, 0, 0]
        self.value = ""
        self.eps = eps

    def NextChoice(self):
        tempselect = -1
        #if the randomness hits make a random choice
        if (random.random() < self.eps):
            tempselect = random.randint(0, 2)
        #if it doesnt find the best average and choose that one
        else:
            maxmean = -1
            tempselect = -1
            for i in range(3):
                divide = -1
                if(self.ChoiceCount[i] == 0):
                    divide = 1
                else:
                    divide = self.ChoiceCount[i]
                print(self.ChoiceCount[i])
                mean = self.ChoiceSum[i] / divide
                if (mean > maxmean):
                    maxmean = mean
                    tempselect = i
            self.ChoiceCount[tempselect] += 1
        # translates the position to a play
        if (tempselect == 0):
            self.value = "R"
        if (tempselect == 1):
            self.value = "P"
        if (tempselect == 2):
            self.value = "C"

    # updates the value of the score received
    def update(self, pos, val):
        if(pos == "R"):
            self.ChoiceSum[0] += val
        if (pos == "P"):
            self.ChoiceSum[1] += val
        if (pos == "C"):
            self.ChoiceSum[2] += val


def Play():
    p1.NextChoice()
    p2.NextChoice()
    updatevalue = -1
    # calculates the value of the play (0 for loss, 1 for tie, 2 for win)
    if (p1.value == p2.value):
        print("both tie with " + p1.value)
        updatevalue = 1
    elif (p1.value == "C"):
        if (p2.value == "P"):
            print("p1 wins : p1 C; p2 P")
            updatevalue = 2
        else:
            print("p2 wins : p1 C; p2 R")
            updatevalue = 0

    elif (p1.value == "P"):
        if (p2.value == "R"):
            print("p1 wins : p1 P; p2 R")
            updatevalue = 2
        else:
            print("p2 wins : p1 P; p2 C")
            updatevalue = 0

    elif (p1.value == "R"):
        if (p2.value == "C"):
            print("p1 wins : p1 R; p2 C")
            updatevalue = 2
        else:
            print("p2 wins : p1 R; p2 P")
            updatevalue = 0

    p1.update(p1.value, updatevalue)


p1 = PlayerMAB(0.1)
p2 = PlayerFile("joueur400.txt")

f = open("testMAB400_1.txt", "x")

p2.NextChoice()
p1.NextChoice()
print(p1.value)

#plays the game a certain amount of times equal to the number in the file
for i in range(int(p2.value)):
    Play()
    f.write(p1.value + " " + p2.value + "\n")