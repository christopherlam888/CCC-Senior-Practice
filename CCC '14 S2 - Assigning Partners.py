studentsNumber = int(input())
partners = []
pairs = []
output = "good"
for i in range(2):
    partners.append(input().split(" "))
for i in range(studentsNumber):
    if partners[0][i] == partners[1][i]:
        output = "bad"
    else:
        pair = [partners[0][i], partners[1][i]]
        pair.sort()
        pairs.append(pair)
pairs.sort()
for i in range(0, len(pairs)-len(pairs)%2, 2):
    if pairs[i] != pairs[i+1]:
        output = "bad"
print(output)
