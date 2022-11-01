birthdaysNumber = int(input())
eligible = []
for i in range(birthdaysNumber):
    birthday = input()
    components = birthday.split(" ")
    if int(components[0]) < 2007-18:
        eligible.append("Yes")
    elif int(components[0]) > 2007-18:
        eligible.append("No")
    elif int(components[1]) < 2:
        eligible.append("Yes")
    elif int(components[1]) > 2:
        eligible.append("No")
    elif int(components[2]) <= 27:
        eligible.append("Yes")
    elif int(components[2]) > 27:
        eligible.append("No")
for i in range(len(eligible)):
    print(eligible[i])
