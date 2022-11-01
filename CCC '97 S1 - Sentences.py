def get_data(number, group):
    for i in range(number):
        group.append(input())


dataSetsNumber = int(input())
for j in range(dataSetsNumber):
    subjectsNumber = int(input())
    subjects = []
    predicatesNumber = int(input())
    predicates = []
    objectsNumber = int(input())
    objects = []
    get_data(subjectsNumber, subjects)
    get_data(predicatesNumber, predicates)
    get_data(objectsNumber, objects)
    sentences = []
    for k in range(subjectsNumber):
        for l in range(predicatesNumber):
            for m in range(objectsNumber):
                sentences.append("%s %s %s." % (subjects[k], predicates[l], objects[m]))
    for n in range(len(sentences)):
        print(sentences[n])
    if dataSetsNumber > 1:
        print("")
