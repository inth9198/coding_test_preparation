import sys
from collections import deque
r, c, m = map(int, sys.stdin.readline().split())
sharks = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
word = [[[0, 0, 0] for __ in range(c)] for _ in range(r)]
for shark in sharks:
    word[shark[0] - 1][shark[1] - 1] = [shark[2],shark[3],shark[4]]
kings_laid = 0
dx = [0,0,1,-1]
dy = [-1,1,0,0]
for king in range(c):
    for y in range(r):
        if word[y][king][2] != 0:
            kings_laid += word[y][king][2]
            word[y][king] = [0, 0, 0]
            break
    new_word = [[[0, 0, 0] for __ in range(c)] for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if word[y][x][2] != 0:
                nx = x + dx[word[y][x][1]-1] * word[y][x][0]
                ny = y + dy[word[y][x][1]-1] * word[y][x][0]
                rev = 1

                while not(0 <= nx < c):
                    if nx >= c:
                        nx = c - 1 - (nx - (c-1))
                    elif 0 > nx:
                        nx *= -1
                    rev *= -1
                while not (0 <= ny < r):
                    if ny >= r:
                        ny = r - (ny - r) - 2
                    elif 0 > ny:
                        ny *= -1
                    rev *= -1

                # print(nx,c)
                ndd = word[y][x][1]
                if rev == -1:
                    if ndd == 1 or ndd == 3:
                        ndd += 1
                    else:
                        ndd -= 1
                if new_word[ny][nx][2] < word[y][x][2]:
                    new_word[ny][nx] = [word[y][x][0], ndd, word[y][x][2]]
    word = new_word
print(kings_laid)

# [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [8, 3, 3], [2, 1, 2]],
#  [[0, 0, 0], [0, 0, 0], [5, 1, 9], [2, 3, 5], [0, 0, 0], [8, 3, 1]],
#  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
#  [[0, 0, 0], [0, 0, 0], [1, 2, 7], [0, 0, 0], [0, 1, 4], [0, 0, 0]]] 8
#
# [[[0, 0, 0], [0, 0, 0], [8, 3, 3], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
#  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [8, 3, 1], [0, 0, 0], [2, 3, 5]],
#  [[0, 0, 0], [0, 0, 0], [5, 1, 9], [0, 0, 0], [0, 0, 0], [2, 2, 2]],
#  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 1, 4], [0, 0, 0]]] 8
#
# [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
#  [[0, 0, 0], [8, 3, 1], [2, 3, 5], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
#  [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [2, 1, 2]],
#  [[0, 0, 0], [0, 0, 0], [5, 2, 9], [0, 0, 0], [0, 1, 4], [0, 0, 0]]] 11
#
