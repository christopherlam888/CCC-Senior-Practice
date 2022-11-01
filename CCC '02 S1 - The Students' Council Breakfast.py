pinkValue = int(input())
greenValue = int(input())
redValue = int(input())
orangeValue = int(input())
totalValue = int(input())
combinations = []
for p in range(int(totalValue/pinkValue)+1):
    for g in range(int(totalValue / greenValue)+1):
        for r in range(int(totalValue / redValue)+1):
            for o in range(int(totalValue / orangeValue)+1):
                if pinkValue*p + greenValue*g + redValue*r + orangeValue*o == totalValue:
                    combinations.append([p, g, r, o])
for i in range(len(combinations)):
    print("# of PINK is %d # of GREEN is %d # of RED is %d # of ORANGE is %d" % (combinations[i][0], combinations[i][1], combinations[i][2], combinations[i][3]))
print("Total combinations is %d." % len(combinations))
minTickets = combinations[0][0] + combinations[0][1] + combinations[0][2] + combinations[0][3]
print("Minimum number of tickets to print is %d." % minTickets)
