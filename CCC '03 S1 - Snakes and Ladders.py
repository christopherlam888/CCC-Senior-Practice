done = False
position = 1
while not done:
    roll = int(input())
    if roll == 0:
        print("You Quit!")
        done = True
    elif position+roll <= 100:
        position += roll
        if position == 100:
            print("You are now on square %d" % position)
            print("You Win!")
            done = True
        elif position == 9:
            position = 34
        elif position == 40:
            position = 64
        elif position == 67:
            position = 86
        elif position == 54:
            position = 19
        elif position == 90:
            position = 98
        elif position == 99:
            position = 77
    if not done:
        print("You are now on square %d" % position)
