# pe99
# we need to compare a^b to x^y
# we need to compare log(a^b) to log(x^y) 
# we need to compare b * log(a) to y * log(x)
from math import log
f = open('../pe099.txt')
a = list(map(lambda x: (x.split(',')), f.read().split('\n')))
b = list(range(len(a)))
z = max(list(map(lambda x: (int(x[0][1])*log(int(x[0][0])),x[1]), zip(a, b))))
print(z)
# it turns out that the line number starts at 1, so add one to the printed result