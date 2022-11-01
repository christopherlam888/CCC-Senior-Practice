#too long error

start = int(input())
end = int(input())
coolNumberCounter = 0
for i in range(start, end+1):
    square = False
    cube = False
    if i == 1:
        coolNumberCounter += 1
    for j in range(1, i):
        if i == (j*j):
            square = True
        if i == (j*j*j):
            cube = True
    if square == True and cube == True:
        coolNumberCounter += 1
print(coolNumberCounter)
