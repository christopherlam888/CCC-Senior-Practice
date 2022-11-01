#TLE
radii = []
inputting = True
while inputting:
    radius = int(input())
    if radius == 0:
        inputting = False
    else:
        radii.append(radius)
for i in range(len(radii)):
    counter = 1
    for x in range(0, radii[i]+1):
        for y in range(1, radii[i]+1):
            if x*x + y*y <= radii[i]*radii[i]:
                counter += 4
    print(counter)

