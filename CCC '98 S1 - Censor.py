n = int(input())
for i in range(n):
    line = input()
    words = line.split(" ")
    for j in range(len(words)):
        if len(words[j])==4:
            words[j] = "****"
    newLine = " ".join(words)
    print(newLine)
