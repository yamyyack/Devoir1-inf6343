f = open("testExploreExploitRecency600.txt", "r")

TotalRegret = 0
for line in f.readlines():
    values = line.strip().split(" ")

    if (values[0] == values[1]):
        TotalRegret +=1
    elif (values[0] == "R" and values[1] == "P"):
        TotalRegret += 2

    elif (values[0] == "P" and values[1] == "C"):
        TotalRegret += 2

    elif (values[0] == "C" and values[1] == "R"):
        TotalRegret += 2

print(TotalRegret)

#478