def find_vowel(line):
    lineList = list(line)
    counter = len(lineList)-1
    while counter >= 0:
        if lineList[counter] == "a" or lineList[counter] == "e" or lineList[counter] == "i" or lineList[counter] == "o" or lineList[counter] == "u":
            return counter
        elif lineList[counter] == " ":
            counter = -1
        else:
            counter -= 1
    return len(line) - len(line.split(" ")[-1])


def last_syllable(line):
    return line[find_vowel(line):]


versesNumber = int(input())
rhymes = []
for i in range(versesNumber):
    lastSyllables = []
    for j in range(4):
        lastSyllables.append(last_syllable(input().lower()))
    if lastSyllables[0] == lastSyllables[1] == lastSyllables[2] == lastSyllables[3]:
        rhymes.append("perfect")
    elif lastSyllables[0] == lastSyllables[1] and lastSyllables[2] == lastSyllables[3]:
        rhymes.append("even")
    elif lastSyllables[0] == lastSyllables[2] and lastSyllables[1] == lastSyllables[3]:
        rhymes.append("cross")
    elif lastSyllables[0] == lastSyllables[3] and lastSyllables[1] == lastSyllables[2]:
        rhymes.append("shell")
    else:
        rhymes.append("free")
for i in range(len(rhymes)):
    print(rhymes[i])
