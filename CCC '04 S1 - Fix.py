collectionsNumber = int(input())
answers = []
for i in range(collectionsNumber):
    collection = []
    for j in range(3):
        collection.append(input())
    answers.append("Yes")
    for j in range(len(collection)):
        for k in range(len(collection)):
            if len(collection[j]) < len(collection[k]):
                if collection[j] in collection[k][len(collection[j])] or collection[j] in collection[k][(len(collection[k])-len(collection[j])): len(collection[k])]:
                    answers[i] = "No"
            if len(collection[j]) == len(collection[k]) and j != k:
                if collection[j] == collection[k]:
                    answers[i] = "No"
for i in range(len(answers)):
    print(answers[i])
