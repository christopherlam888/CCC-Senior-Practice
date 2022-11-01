def find_expressed(allele1, allele2):
    if allele1.isupper():
        return allele1
    elif allele2.isupper():
        return allele2
    else:
        return allele1


def populate_possibilities(possibilities, start, end):
    for i in range(start, end):
        for j in range(start, end):
            possibilities.append(find_expressed(mother[i], father[j]))


def check_allele(child, possibilities, index):
    if child[index] in possibilities:
        return True
    else:
        return False


mother = input()
father = input()
aPossibilities = []
bPossibilities = []
cPossibilities = []
dPossibilities = []
ePossibilities = []
populate_possibilities(aPossibilities, 0, 2)
populate_possibilities(bPossibilities, 2, 4)
populate_possibilities(cPossibilities, 4, 6)
populate_possibilities(dPossibilities, 6, 8)
populate_possibilities(ePossibilities, 8, 10)
childrenNumber = int(input())
for i in range(childrenNumber):
    child = input()
    a = check_allele(child, aPossibilities, 0)
    b = check_allele(child, bPossibilities, 1)
    c = check_allele(child, cPossibilities, 2)
    d = check_allele(child, dPossibilities, 3)
    e = check_allele(child, ePossibilities, 4)
    if (a == True) and (b == True) and (c == True) and (d == True) and (e == True):
        print("Possible baby.")
    else:
        print("Not their baby!")
