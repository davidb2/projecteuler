from fractions import Fraction
LO = 2
HI = 45
FRAC = Fraction(1, 2)
cache = {}


def ways(frac, curr_denom, acc):
    #print frac, float(frac), curr_denom
    #raw_input()
    print acc
    if frac == 0:
        return 1
    elif frac < 0:
        return 0
    elif (frac, curr_denom) not in cache:
        ans = 0
        for d in xrange(curr_denom+1, HI+1):
            ans += ways(frac - Fraction(1, d**2), d, acc+[d])
        cache[(frac, curr_denom)] = ans
    return cache[(frac, curr_denom)]

