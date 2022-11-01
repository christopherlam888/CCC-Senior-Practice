components = []
while True:
    information = input()
    components.extend(information.split(" "))
    if "Waterloo" in information:
        break
lowestTemperatureIndex = 1
for i in range(3, len(components), 2):
    if int(components[i]) < int(components[lowestTemperatureIndex]):
        lowestTemperatureIndex = i
print(components[lowestTemperatureIndex-1])
