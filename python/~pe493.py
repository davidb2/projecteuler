# def ans()

# div = 70!/50!

# P(0) = 0
# P(1) = 0
# P(2) = ((7 pick 2) * (10!)^2) / div
# P(3) = 

from random import randint
COLORS = 7
PICKS = 20
def sim():
    balls_selected = set()
    balls = [x // COLORS for x in range(COLORS * 10)]
    for _ in range(PICKS):
        i = randint(0, len(balls)-1)
        balls_selected.add(balls[i])
        del balls[i]
    return float(len(balls_selected))

dis = 0.0  
count = 0.0
MOD = 100000
while True:
    dis += sim()
    count += 1.0
    if int(count) % MOD == 0:
        print(dis/count)