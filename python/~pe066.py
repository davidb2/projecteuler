from math import sqrt

# bruteforce:
def f(D):
    x = 1
    while True:
        x2 = x*x
        y2 = float(x2-1)/float(D)
        y = int(sqrt(y2))
        if int(y*y) == y2 and y > 0:
            return x
        x += 1