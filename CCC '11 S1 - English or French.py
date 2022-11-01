linesNumber = int(input())
lines = []
tCounter = 0
sCounter = 0
for i in range(linesNumber):
    lines = input()
    for j in range(len(lines)):
        if lines[j] == "T" or lines[j] == "t":
            tCounter += 1
        if lines[j] == "S" or lines[j] == "s":
            sCounter += 1
if tCounter > sCounter:
    print("English")
else:
    print("French")
