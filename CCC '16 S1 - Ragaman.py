s1 = list(input())
s1.sort()
s2 = list(input())
s2.sort()
anagram = True
for i in range(len(s2)):
    if s2[i] != "*":
        if s2[i] in s1:
            s1.remove(s2[i])
        else:
            anagram = False
if not anagram:
    print('N')
else:
    print('A')
