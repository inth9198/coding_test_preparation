import sys
board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
blank = []
stack = []
for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            blank.append((r, c))
def check(_r, _c):
    for i in range(9):
        if i != _c and board[_r][i] == board[_r][_c]:
            return False
    for i in range(9):
        if i != _r and board[i][_c] == board[_r][_c]:
            return False
    for i in range(_r//3 * 3, _r//3 * 3 + 3):
        for j in range(_c // 3 * 3, _c // 3 * 3 + 3):
            if (i, j) == (_r, _c):
                continue
            if board[i][j] == board[_r][_c]:
                return False
    return True
ending = False
def dfs(deep_i):
    global ending
    if ending:
        return
    if deep_i == len(blank):
        for r in range(9):
            for c in range(9):
                print(board[r][c], end=' ')
            print()
        ending = True
        return
    for i in range(1, 10):
        r_i, c_i = blank[deep_i]
        board[r_i][c_i] = i
        if check(r_i, c_i):
            stack.append((r_i, c_i, i))
            dfs(deep_i + 1)
        else:
            board[r_i][c_i] = 0
    deep_i -= 1
    tmp_r, tmp_c, tmp_i = stack.pop()
    board[tmp_r][tmp_c] = 0
dfs(0)
