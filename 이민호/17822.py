import sys
from collections import deque
n, m, t = map(int, sys.stdin.readline().split())
circle = [deque(list(map(int, sys.stdin.readline().split()))) for _ in range(n)]
go_turn = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]
# 2 -> 2, 4 -> 1, 3
dn = [0, -1, 1, 0]
dm = [-1, 0, 0, 1]

for i in range(t):
    fist_x = go_turn[i][0] - 1
    x_i = go_turn[i][0]
    for j in range(n):
        if fist_x == j % x_i:
            #시계방향
            if go_turn[i][1] == 0:
                circle[j].rotate(go_turn[i][2])
            elif go_turn[i][1] == 1:
                circle[j].rotate(go_turn[i][2] * (-1))
    black_list = []
    white_list = []
    flag = False
    all_sum = 0
    for n_i in range(n):
        for m_i in range(m):
            if circle[n_i][m_i] != 0:
                all_sum += circle[n_i][m_i]
                white_list.append((n_i, m_i))
            for d in range(4):
                if 0 <= n_i + dn[d] < n:
                    nm = m_i + dm[d]
                    if nm == m:
                        nm = 0
                    if circle[n_i][m_i] == 0:
                        continue
                    if circle[n_i][m_i] == circle[n_i + dn[d]][nm]:
                        black_list.append((n_i, m_i))
                        black_list.append((n_i + dn[d], nm))
                        flag = True
    black_list = list(set(black_list))
    for black in black_list:
        circle[black[0]][black[1]] = 0
    if not flag:
        for white in white_list:
            if circle[white[0]][white[1]] > all_sum/len(white_list):
                circle[white[0]][white[1]] -= 1
            elif circle[white[0]][white[1]] < all_sum/len(white_list):
                circle[white[0]][white[1]] += 1
all_sum = 0
for n_i in range(n):
    for m_i in range(m):
        if circle[n_i][m_i] != 0:
            all_sum += circle[n_i][m_i]
print(all_sum)