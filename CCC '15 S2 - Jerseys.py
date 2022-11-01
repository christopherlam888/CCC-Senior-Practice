#TLE on cases 4 and 5
jerseysNumber, athletesNumber = int(input()), int(input())
jerseys = []
for i in range(1, jerseysNumber+1):
    size = input()
    jerseys.append([i, size])
requests = []
for i in range(athletesNumber):
    info = input().split(" ")
    requests.append([int(info[1]), info[0]])
sizes = {"S": 1, "M": 2, "L": 3}
jerseys.sort()
requests.sort()
counter = 0
for i in range(jerseysNumber):
    j = 0
    found = False
    while j < athletesNumber and not found:
        if jerseys[i] == requests[j] or (sizes[jerseys[i][1]] > sizes[requests[j][1]] and jerseys[i][0] == requests[j][0]):
            counter += 1
            found = True
        else:
            j += 1
print(counter)
