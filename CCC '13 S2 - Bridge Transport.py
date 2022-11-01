maxWeight = int(input())
carsNumber = int(input())
weights = []
for i in range(carsNumber):
    weights.append(int(input()))
if sum(weights[0:4]) <= maxWeight:
    cars = 4
    broken = False
    counter = 1
    while not broken and counter < carsNumber-3:
        if sum(weights[counter:counter+4]) <= maxWeight:
            cars += 1
            counter += 1
        else:
            broken = True
else:
    cars = 0
    for i in range(1, 4):
        if sum(weights[0:i]) <= maxWeight:
            cars += 1
print(cars)
