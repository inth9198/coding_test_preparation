import sys
from collections import deque
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
vir = deque()
for y in range(n):
    for x in range(n):
        if board[y][x] == 2:
            vir.append((y, x))
can_vir_list = combinations(vir, m)
min_time = 1e9
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
for vir_list in can_vir_list:
    banggi = False
    time_map = [[-1] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    q = deque()
    for vir in vir_list:
        time_map[vir[0]][vir[1]] = 0
        q.append(vir)
    while q:
        y, x = q.popleft()
        visited[y][x] = True
        for i in range(4):
            if 0 <= y + dy[i] < n and 0 <= x + dx[i] < n:
                ny = y + dy[i]
                nx = x + dx[i]
                if board[ny][nx] == 1:
                    continue
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    if (ny, nx) not in vir_list:
                        time_map[ny][nx] = time_map[y][x] + 1
                    q.append((ny, nx))
    in_max_time = 0
    for y in range(n):
        for x in range(n):
            if time_map[y][x] == -1 and board[y][x] == 0:
                banggi = True
                break
            if visited and board[y][x] != 2:
                in_max_time = max(in_max_time, time_map[y][x])
        if banggi:
            break
    if banggi:
        continue

    min_time = min(in_max_time,min_time)
if min_time == 1e9:
    print(-1)
else:
    print(min_time)
