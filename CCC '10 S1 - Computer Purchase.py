def max_index():
    index = 0
    for i in range(1, len(computerValues)):
        if computerValues[i] > computerValues[index]:
            index = i
        elif computerValues[i] == computerValues[index] and computerNames[i] < computerNames[index]:
            index = i
    return index


computersNumber = int(input())
if computersNumber > 0:
    computerNames = []
    computerValues = []
    for i in range(computersNumber):
        computerComponents = input().split(" ")
        computerNames.append(computerComponents[0])
        computerValues.append(2*int(computerComponents[1])+3*int(computerComponents[2])+int(computerComponents[3]))
    computerOne = max_index()
    print(computerNames[computerOne])
    computerValues.remove(computerValues[computerOne])
    computerNames.remove(computerNames[computerOne])
    if computersNumber == 2:
        print(computerNames[0])
    elif computersNumber > 2:
        computerTwo = max_index()
        print(computerNames[computerTwo])
