def to_number(character):
    if character == "A" or character == "B" or character == "C":
        return "2"
    elif character == "D" or character == "E" or character == "F":
        return "3"
    elif character == "G" or character == "H" or character == "I":
        return "4"
    elif character == "J" or character == "K" or character == "L":
        return "5"
    elif character == "M" or character == "N" or character == "O":
        return "6"
    elif character == "P" or character == "Q" or character == "R" or character == "S":
        return "7"
    elif character == "T" or character == "U" or character == "V":
        return "8"
    elif character == "W" or character == "X" or character == "Y" or character == "Z":
        return "9"
    elif character == "0" or character == "1" or character == "2" or character == "3" or character == "4" or character == "5" or character == "6" or character == "7" or character == "8" or character == "9":
        return character
    else:
        return ""


testCasesNumber = int(input())
for i in range(testCasesNumber):
    givenNumber = input()
    newNumberParts = []
    j = 0
    while len(newNumberParts) != 10:
        if to_number(givenNumber[j]) != "":
            newNumberParts.append(to_number(givenNumber[j]))
        j += 1
    newNumberParts.insert(3, "-")
    newNumberParts.insert(7, "-")
    newNumber = "".join(newNumberParts)
    print(newNumber)
