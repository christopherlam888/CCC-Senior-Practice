def fit(itemSize, boxSize):
    if itemSize[0] > boxSize[1] or itemSize[1] > boxSize[2] or itemSize[2] > boxSize[3]:
        return False
    else:
        return True


boxSizesNumber = int(input())
boxSizes = []
for i in range(boxSizesNumber):
    dimensions = input().split(" ")
    boxVolume = 1
    for j in range(len(dimensions)):
        dimensions[j] = int(dimensions[j])
        boxVolume *= dimensions[j]
    dimensions.sort()
    boxSize = [boxVolume]
    boxSize.extend(dimensions)
    boxSizes.append(boxSize)
boxSizes.sort()
itemsNumber = int(input())
itemSizes = []
for i in range(itemsNumber):
    itemSize = input().split(" ")
    for j in range(len(itemSize)):
        itemSize[j] = int(itemSize[j])
    itemSize.sort()
    itemSizes.append(itemSize)
outputs = []
for i in range(itemsNumber):
    done = False
    j = 0
    while not done and j < boxSizesNumber:
        if fit(itemSizes[i], boxSizes[j]):
            outputs.append(boxSizes[j][0])
            done = True
        else:
            j += 1
    if not done:
        outputs.append("Item does not fit.")
for i in range(itemsNumber):
    print(outputs[i])
