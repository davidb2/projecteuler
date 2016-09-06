# all primitive pythagorean triplets can be formed using:
#   a = m^2 - n^2
#   b = 2mn
#   c = m^2 + n^2
# we can reduce the system of equations:
#    perimeter = a + b + c = m^2 - n^2 + 2mn + m^2 + n^2
# => perimeter = 2m^2 + 2mn
# => perimeter/2 = m^2 + mn     -- we see that the perimeter MUST be even
# => perimeter/2 - m^2 = mn
# => (perimeter/2 - m^2)/m = n 
# => perimeter/(2m) - m = n 

from fractions import gcd
LIMIT = 1500000
ones = 0
cache = [0 for i in range(LIMIT+1)]
for m in range(1, 1223, 2):
    for n in range(2, 1223+1, 2):
        if gcd(m, n) == 1:
            a = abs(m**2 - n**2)
            b = 2*m*n 
            c = m**2 + n**2
            length = a + b + c
            for multiple in range(1, LIMIT//length+1):
                temp_length = length * multiple
                cache[temp_length] += 1
                if cache[temp_length] == 1: ones += 1
                elif cache[temp_length] == 2: ones -= 1
print(ones)

# # Using: https://en.wikipedia.org/wiki/Pythagorean_triple#Parent.2Fchild_relationships

# from functools import reduce
# LIMIT = 1500000
# cache = [0 for i in range(LIMIT+1)]
# ones = 0
# def triples(a = 3, b = 4, c = 5):
#     global ones
#     l = a + b + c
#     if l > LIMIT: return 0
#     for i in range(1, LIMIT//l+1):
#         cache[l*i] += 1
#         if cache[l*i] == 1: ones += 1
#         if cache[l*i] == 2: ones -= 1
    
#     return reduce(lambda x, y: x + y, [
#         LIMIT//l,
#         triples(a - 2*b + 2*c,  2*a - b + 2*c,  2*a - 2*b + 3*c),
#         triples(a + 2*b + 2*c,  2*a + b + 2*c,  2*a + 2*b + 3*c),
#         triples(-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c)])
# print(triples(), 'triplets\nAnswer:', ones)