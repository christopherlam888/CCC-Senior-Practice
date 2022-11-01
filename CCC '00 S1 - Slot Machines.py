total = int(input())
machines = []
for i in range(3):
    machines.append(int(input()))
plays = 0
playing = True
while playing:
    for i in range(len(machines)):
        total -= 1
        machines[i] += 1
        plays += 1
        if i == 0 and machines[i] == 35:
            total += 30
            machines[i] = 0
        elif i == 1 and machines[i] == 100:
            total += 60
            machines[i] = 0
        elif i == 2 and machines[i] == 10:
            total += 9
            machines[i] = 0
        if total == 0:
            print("Martha plays %d times before going broke." % plays)
            playing = False
