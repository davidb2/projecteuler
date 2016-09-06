class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def sign(a, b, c):
    return (a.x-c.x)*(b.y-c.y)-(b.x-c.x)*(a.y-c.y)
def point_included(pt, a, b, c):
    b1 = sign(pt, a, b) < 0
    b2 = sign(pt, b, c) < 0
    b3 = sign(pt, c, a) < 0
    return (b1 == b2) and (b2 == b3)

ans = 0
for line in open("../pe102.txt"):
    nums = list(map(int, line.split(",")))
    a = Point(nums[0], nums[1])
    b = Point(nums[2], nums[3])
    c = Point(nums[4], nums[5])
    pt = Point(0, 0) # origin
    ans += 1 if point_included(pt, a, b, c) else 0
print(ans)