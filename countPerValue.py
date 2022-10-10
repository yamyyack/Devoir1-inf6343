f = open("testExploreExploit400.txt", "r")

TotalRegret = 0
totalcount = [0,0,0]
for line in f.readlines():
    values = line.strip().split(" ")

    if (values[1] == "R"):
        totalcount[0] += 1
    elif (values[1] == "P"):
        totalcount[1] += 1
    elif (values[1] == "C"):
        totalcount[2] += 1

print(totalcount)