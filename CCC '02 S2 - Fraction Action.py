def find_fraction(numerator, denominator):
    newNumerator = numerator % denominator
    for i in range(newNumerator, 1, -1):
        if newNumerator % i == 0 and denominator % i == 0:
            newNumerator /= i
            denominator /= i
    return "%d/%d" % (int(newNumerator), int(denominator))


numerator = int(input())
denominator = int(input())
if numerator % denominator == 0:
    print(int(numerator/denominator))
elif numerator//denominator > 0:
    whole = numerator//denominator
    print("%d %s" % (whole, find_fraction(numerator, denominator)))
else:
    print(find_fraction(numerator, denominator))
