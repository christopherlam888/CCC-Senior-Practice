values = list(input())
for i in range(1, len(values), 2):
    if values[i] == "I":
        values[i] = 1
    elif values[i] == "V":
        values[i] = 5
    elif values[i] == "X":
        values[i] = 10
    elif values[i] == "L":
        values[i] = 50
    elif values[i] == "C":
        values[i] = 100
    elif values[i] == "D":
        values[i] = 500
    elif values[i] == "M":
        values[i] = 1000
total = 0
for i in range(0, len(values), 2):
    if i+1 <= len(values)-3 and values[i+1] < values[i+3]:
        total -= int(values[i])*values[i+1]
    else:
        total += int(values[i])*values[i+1]
print(total)
