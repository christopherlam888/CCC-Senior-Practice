def calculate_points(string):
    points = 0
    if string == "":
        points += 3
    else:
        cards = string.split(" ")
        for i in range(len(cards)):
            if cards[i] == "A":
                points += 4
            elif cards[i] == "K":
                points += 3
            elif cards[i] == "Q":
                points += 2
            elif cards[i] == "J":
                points += 1
        if len(cards) == 1:
            points += 2
        elif len(cards) == 2:
            points +=1
    return points


hand1 = input().split("S")
temp = " ".join(list(hand1[1]))
spades = ["Spades", temp, calculate_points(temp)]
hand2 = hand1[0].split("H")
temp = " ".join(list(hand2[1]))
hearts = ["Hearts", temp, calculate_points(temp)]
hand3 = hand2[0].split("D")
temp = " ".join(list(hand3[1]))
diamonds = ["Diamonds", temp, calculate_points(temp)]
hand4 = hand3[0].split("C")
temp = " ".join(list(hand4[1]))
clubs = ["Clubs", temp, calculate_points(temp)]
table = [["Cards Dealt", "", "Points"], clubs, diamonds, hearts, spades]
total = 0
for i in range(1, len(table)):
    total += table[i][2]
table.append(["", "", "Total %d" % total])
for line in table:
    print('{:<12} {:<12} {:>10}'.format(*line))#format strings with left or right alignment and column width in chars
