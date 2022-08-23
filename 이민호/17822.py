import sys
from collections import deque
n, m, t = map(int, sys.stdin.readline().split())
circle = [deque(list(map(int, sys.stdin.readline().split()))) for _ in range(n)]
go_turn = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]
# 2 -> 2, 4 -> 1, 3
dn = [0, -1, 1, 0]
dm = [-1, 0, 0, -1]

for i in range(t):
    fist_x = go_turn[i][0] - 1
    x_i = go_turn[i][0]
    for j in range(n):
        if fist_x == j % x_i:
            #시계방향
            if go_turn[i][1] == 0:
                circle[i].rotate(go_turn[i][2])
            elif go_turn[i][1] == 1:
                circle[i].rotate(go_turn[i][2] * (-1))