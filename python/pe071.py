UPPER_LIMIT = 3/7   # 0.428571
min_delta = [1, (0, 1)]
for denominator in range(8, 1000000+1):
    numerator = (denominator*3)//7
    frac = numerator / denominator
    delta = UPPER_LIMIT - frac
    if delta < min_delta[0] and frac != UPPER_LIMIT:
        min_delta[0], min_delta[1] = delta, (numerator, denominator)
print('Fraction:', str(min_delta[1][0])+'/'+str(min_delta[1][1]), '\nAnswer:', min_delta[1][0])