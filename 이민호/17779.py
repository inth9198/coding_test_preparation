import sys
n = int(sys.stdin.readline())
word = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

can = []
for d1 in range(1, n + 1):
    for d2 in range(1, n + 1):
        for y in range(d1, n + 1):
            for x in range(1, n-d1-d2+1):
                if 1 <= x < x + d1 + d2 <= n and 1 <= y-d1 < y < y + d2 <= n:
                    can.append((d1, d2, x, y))
gap = 1e9
for d1d2xy in can:
    _one = 0
    _two = 0
    _three = 0
    _four = 0
    _five = 0
    demo = [[False] * n for _ in range(n)]
    d1, d2, x, y = d1d2xy
    for i in range(d1+1):
        demo[x+i-1][y-i-1] = True
    for i in range(d2+1):
        demo[x + i - 1][y + i - 1] = True
    for i in range(d2+1):
        demo[x+d1+i - 1][y-d1+i - 1] = True
    for i in range(d1+1):
        demo[x + d2 + i - 1][y + d2 - i - 1] = True
    line = []
    for _x in range(x, d1 + d2 + x + 1):
        flag = False
        for _y in range(1, n + 1):
            if demo[_x - 1][_y - 1]:
                line.append((_x, _y))
                if not flag and True in demo[_x - 1][_y:n]:
                    flag = True
                elif flag:
                    flag = False
            elif flag :
                line.append((_x, _y))

    for r in range(1, n+1):
        for c in range(1, n+1):
            if (r, c) in line:
                _five += word[r - 1][c - 1]
            elif 1 <= r < x + d1 and 1 <= c <= y:
                _one += word[r-1][c-1]
            elif 1 <= r <= x + d2 and y < c <= n:
                _two += word[r-1][c-1]
            elif x+d1 <= r <= n and 1 <= c < y-d1+d2:
                _three += word[r-1][c-1]
            elif x+d2 < r <= n and y-d1+d2 <= c <= n:
                _four += word[r-1][c-1]
            else:
                _five += word[r-1][c-1]

    w = [_one, _two, _three, _four, _five]

    gap = min(gap, (max(w) - min(w)))
print(gap)