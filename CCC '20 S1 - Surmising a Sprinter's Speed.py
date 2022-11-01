observationsNumber = int(input())
observations = []
for i in range(observationsNumber):
    observations.append(input().split(" "))
for i in range(len(observations)):
    observations[i][0] = int(observations[i][0])
observations.sort()
speeds = []
for i in range(len(observations)-1):
    speeds.append(abs((float(observations[i][1])-float(observations[i+1][1]))/(float(observations[i][0])-float(observations[i+1][0]))))
print(max(speeds))
