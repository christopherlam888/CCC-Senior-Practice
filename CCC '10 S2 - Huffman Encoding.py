charactersNumber = int(input())
characters = []
for i in range(charactersNumber):
    characters.append(input().split(" "))
code = input()
message = []
while len(code) > 0:
    for i in range(len(characters)):
        if characters[i][1] in code[0:len(characters[i][1])]:
            message.append(characters[i][0])
            code = code[len(characters[i][1]):len(code)]
print("".join(message))
