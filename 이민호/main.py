#19238
from collections import deque
n, m, s = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s_r, s_c = map(int, input().split())
client = [list(map(int, input().split())) for _ in range(m)]

dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]
s_r -= 1
s_c -= 1
for ci in client:
    for i in range(4):
        ci[i] -= 1
def bfs(sr, sc):
    visited = [[False] * n for _ in range(n)]
    visited_dir = [[-1] * n for _ in range(n)]
    visited_dir[sr][sc] = 0
    Q = deque()
    Q.append((sr, sc))
    while Q:
        now_r, now_c = Q.popleft()
        for i in range(4):
            if 0 <= now_r + dr[i] < n and 0 <= now_c + dc[i] < n:
                nr = now_r + dr[i]
                nc = now_c + dc[i]
                if not visited[nr][nc] and board[nr][nc] == 0:
                    visited[nr][nc] = True
                    visited_dir[nr][nc] = visited_dir[now_r][now_c] + 1
                    Q.append((nr, nc))
    return visited_dir

def bfs_go( now_r, now_c, dest_r, dest_c):
    visited = [[False] * n for _ in range(n)]
    visited_dir = [[-1] * n for _ in range(n)]
    visited_dir[now_r][now_c] = 0
    if dest_r == now_r and dest_c == now_c:
        return visited_dir[now_r][now_c]
    Q = deque()
    Q.append((now_r, now_c))
    while Q:
        now_r, now_c = Q.popleft()
        for i in range(4):
            if 0 <= now_r + dr[i] < n and 0 <= now_c + dc[i] < n:
                nr = now_r + dr[i]
                nc = now_c + dc[i]
                if not visited[nr][nc] and board[nr][nc] == 0:
                    visited[nr][nc] = True
                    visited_dir[nr][nc] = visited_dir[now_r][now_c] + 1
                    if dest_r == nr and dest_c == nc:
                        return visited_dir[nr][nc]
                    Q.append((nr, nc))
    return -1
flag = False
for _ in range(m):
    b_map = bfs(s_r, s_c)
    s_dir = 100
    s_dir_rc = (20, 20)
    s_i = -1
    for i in range(len(client)):
        if b_map[client[i][0]][client[i][1]] == -1:
            continue
        if s_dir > b_map[client[i][0]][client[i][1]]:
            s_dir_rc = (client[i][0], client[i][1], client[i][2], client[i][3])
            s_dir = b_map[client[i][0]][client[i][1]]
            s_i = i
        elif s_dir == b_map[client[i][0]][client[i][1]]:
            if s_dir_rc[1] > client[i][0]:
                s_dir_rc = (client[i][0], client[i][1], client[i][2], client[i][3])
                s_dir = b_map[client[i][0]][client[i][1]]
                s_i = i
    del client[s_i]
    s_r, s_c = s_dir_rc[0], s_dir_rc[1]
    s -= s_dir
    if s <= 0 or s_dir == 100:
        print(-1)
        flag = True
        break
    visited_d = [[False] * n for _ in range(n)]
    re = bfs_go(s_r, s_c, s_dir_rc[2], s_dir_rc[3])
    s -= re
    if s < 0 or re == -1:
        print(-1)
        flag = True
        break
    s += (re * 2)
    s_r, s_c = s_dir_rc[2], s_dir_rc[3]
if not flag:
    print(s)
# 6 1 2
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 3 4
# 3 4 2 5