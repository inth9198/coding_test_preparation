import copy
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
board = [[[] for _ in range(4)] for _ in range(4)]
for r in range(4):
    line = list(map(int, input().split()))
    for c in range(4):
        board[r][c] = [line[c*2], line[c*2+1] - 1]
score = board[0][0][0]
board[0][0][0] = 0 #죽음을 의미
top_score = 0
def dfs(s_r, s_c, s_d, _board):
    global score
    global top_score
    copy_board = copy.deepcopy(_board)
    for i in range(1, 17):
        stop_sign = False
        for r in range(4):
            if stop_sign:
                break
            for c in range(4):
                if stop_sign:
                    break
                elif copy_board[r][c][0] == 0:
                    continue
                elif copy_board[r][c][0] == i:
                    for a in range(8):
                        tmp_i = (a + copy_board[r][c][1]) % 8
                        tmp_r = r + dr[tmp_i]
                        tmp_c = c + dc[tmp_i]
                        if 0 <= tmp_r < 4 and 0 <= tmp_c < 4:
                            if not (tmp_r == s_r and tmp_c == s_c):
                                copy_board[r][c][1] = tmp_i
                                tmp = copy_board[r][c]
                                copy_board[r][c] = copy_board[tmp_r][tmp_c]
                                copy_board[tmp_r][tmp_c] = tmp
                                break
                    stop_sign = True
                    break
    re_flag = True
    for i in range(1, 4):
        nr = s_r + (dr[s_d]) * i
        nc = s_c + (dc[s_d]) * i
        if 0 <= nr < 4 and 0 <= nc < 4:
            if copy_board[nr][nc][0] != 0:
                re_flag = False
                add_score = copy_board[nr][nc][0]
                score += add_score
                nd = copy_board[nr][nc][1]
                copy_board[nr][nc][0] = 0
                dfs(nr, nc, nd, copy_board)
                score -= add_score
                copy_board[nr][nc][0] = add_score
    if re_flag:
        if top_score < score:
            top_score = score
        return
d = board[0][0][1]
dfs(0, 0, d, board)
print(top_score)

