mapping = []
for i in range(2):
    mapping.append(list(input()))
code = list(input())
message = []
for i in range(len(code)):
    if code[i] in mapping[1]:
        message.append(mapping[0][mapping[1].index(code[i])])
    else:
        message.append(".")
print("".join(message))
