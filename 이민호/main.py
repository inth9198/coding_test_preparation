import sys
n = int(input())
board = [list(map(int, input())) for _ in range(n)]
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
cir = []
def dfs(_r, _c):
    for i in range(4):
        if 0 <= _r + dr[i] < n and 0 <= _c + dc[i] < n:
            nr = _r + dr[i]
            nc = _c + dc[i]
            if board[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                cir[-1] += 1
                dfs(nr, nc)

visited = [[False] * n for _ in range(n)]
for r in range(n):
    for c in range(n):
        if board[r][c] == 1 and not visited[r][c]:
            visited[r][c] = True
            cir.append(1)
            dfs(r, c)
cir.sort()
print(len(cir))
for c in cir:
    print(c)
