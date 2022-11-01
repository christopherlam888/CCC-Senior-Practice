year = int(input())
while True:
    fail = False
    year += 1
    yearString = str(year)
    for i in range(len(yearString)):
        for j in range(i+1, len(yearString)):
            if yearString[i] == yearString[j]:
                fail = True
    if fail != True:
        print(year)
        break