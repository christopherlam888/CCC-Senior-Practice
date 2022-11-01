#wrong answer for two cases???
inputsNumber = int(input())
values = []
index = 0
for i in range(inputsNumber):
    value = int(input())
    if value == 0:
        values.remove(values[index-1])
        index -= 1
    else:
        values.append(value)
        index += 1
sum = 0
for i in range(len(values)):
    sum += values[i]
print(sum)
