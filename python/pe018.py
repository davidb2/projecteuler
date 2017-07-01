def max_path(triangle):
    for level in xrange(1, len(triangle)):
        triangle[level][0] += triangle[level - 1][0]
        for i in xrange(1, level):
            triangle[level][i] += max(
                triangle[level - 1][i - 1],
                triangle[level - 1][i]
            )
        triangle[level][~0] += triangle[level - 1][~0]
    return max(triangle[~0])

def trianglize(lines):
    return [map(int, line.split()) for line in lines]

with open('../pe018.txt', 'r') as f:
    triangle = trianglize(f.readlines())
print max_path(triangle)