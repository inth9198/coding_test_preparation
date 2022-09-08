import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
long_way = 0
dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]
visited = [False] * 26
visited[ord(board[0][0]) - ord('A')] = True
def dfs(_r, _c, deep):
    global long_way
    flag = True
    for i in range(4):
        nr = _r + dr[i]
        nc = _c + dc[i]
        if 0 <= nr < r and 0 <= nc < c:
            n_o = ord(board[nr][nc]) - ord('A')
            if not visited[n_o]:
                visited[n_o] = True
                dfs(nr, nc, deep + 1)
                visited[n_o] = False
                flag = False
    if flag:
        long_way = max(deep, long_way)
dfs(0, 0, 1)
print(long_way)