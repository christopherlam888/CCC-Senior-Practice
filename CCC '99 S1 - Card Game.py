def check_following_cards(deck, start, end):
    point = True
    for i in range(start, end):
        if deck[i] == "ace" or deck[i] == "king" or deck[i] == "queen" or deck[i] == "jack":
            point = False
    return point


def assign_point(j, point):
    if j % 2 == 0:
        print("Player A scores %d point(s)." % point)
        return "A"
    else:
        print("Player B scores %d point(s)." % point)


deck = []
for j in range(52):
    deck.append(input())
aScore = 0
bScore = 0
for j in range(len(deck)):
    if deck[j] == "ace" and j < 48 and check_following_cards(deck, j+1, j+5):
        if assign_point(j, 4) == "A":
            aScore += 4
        else:
            bScore += 4
    elif deck[j] == "king" and j < 49 and check_following_cards(deck, j+1, j+4):
        if assign_point(j, 3) == "A":
            aScore += 3
        else:
            bScore += 3
    elif deck[j] == "queen" and j < 50 and check_following_cards(deck, j+1, j+3):
        if assign_point(j, 2) == "A":
            aScore += 2
        else:
            bScore += 2
    elif deck[j] == "jack" and j < 51 and check_following_cards(deck, j+1, j+2):
        if assign_point(j, 1) == "A":
            aScore += 1
        else:
            bScore += 1
print("Player A: %d point(s)." % aScore)
print("Player B: %d point(s)." % bScore)
