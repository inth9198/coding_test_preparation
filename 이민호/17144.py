import sys
from collections import deque
r, c, t = map(int, sys.stdin.readline().split())
word = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

for i in range(r):
    if word[i][0] == -1:
        mc_y = i
        break
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
for _ in range(t):
    word_add = [[0] * c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if word[y][x] != 0 and word[y][x] != -1:
                can_go = 0
                for i in range(4):
                    if 0 <= y + dy[i] < r and 0 <= x + dx[i] < c and word[y + dy[i]][x + dx[i]] != -1:
                        word_add[y + dy[i]][x + dx[i]] += word[y][x] // 5
                        can_go += 1
                word[y][x] -= can_go * (word[y][x] // 5)

    for y in range(r):
        for x in range(c):
            word[y][x] += word_add[y][x]
    ro_man = deque()


    for i in range(1, c):
        ro_man.append(word[mc_y][i])
    for i in range(mc_y - 1, -1, -1):
        ro_man.append(word[i][c - 1])
    for i in range(c - 2, -1, -1):
        ro_man.append(word[0][i])
    for i in range(1, mc_y):
        ro_man.append(word[i][0])
    ro_man.rotate(1)
    ro_man[0] = 0
    for i in range(1, c):
        word[mc_y][i] = ro_man.popleft()
    for i in range(mc_y - 1, -1, -1):
        word[i][c - 1] = ro_man.popleft()
    for i in range(c - 2, -1, -1):
        word[0][i] = ro_man.popleft()
    for i in range(1, mc_y):
        word[i][0] = ro_man.popleft()


    for i in range(1, c):
        ro_man.append(word[mc_y + 1][i])
    for i in range(mc_y + 2, r):
        ro_man.append(word[i][c - 1])
    for i in range(c - 2, -1, -1):
        ro_man.append(word[r - 1][i])
    for i in range(r - 2, mc_y + 1, -1):
        ro_man.append(word[i][0])
    ro_man.rotate(1)
    ro_man[0] = 0
    for i in range(1, c):
        word[mc_y + 1][i] = ro_man.popleft()
    for i in range(mc_y + 2, r):
        word[i][c - 1] = ro_man.popleft()
    for i in range(c - 2, -1, -1):
        word[r - 1][i] = ro_man.popleft()
    for i in range(r - 2, mc_y + 1, -1):
        word[i][0] = ro_man.popleft()

re = 0
for i in range(r):
    re += sum(word[i])
print(re + 2)
