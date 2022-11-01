villagesNumber = int(input())
villages = []
midpoints = []
neighbourhoods = []
for i in range(villagesNumber):
    villages.append(float(input()))
villages.sort()
for i in range(len(villages)-1):
    midpoints.append((villages[i]+villages[i+1])/2)
for i in range(len(midpoints)-1):
    neighbourhoods.append(midpoints[i+1]-midpoints[i])
neighbourhoods.sort()
print(neighbourhoods[0])
