questionsNumber = int(input())
answers = []
for i in range(questionsNumber):
    answers.append(input())
key = []
for i in range(questionsNumber):
    key.append(input())
score = 0
for i in range(questionsNumber):
    if answers[i] == key[i]:
        score += 1
print(score)
