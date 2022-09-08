def dice_up(b, r):
    for i in range(1, 7):
        if r == i:
            d = dice_pattern[i - 1]
            if d.index(b) == 3:
                return d[0], i
            else:
                return d[d.index(b) + 1], i


def dice_down(b, r):
    for i in range(1, 7):
        if r == i:
            d = dice_pattern[i - 1]
            if d.index(b) == 0:
                return d[3], i
            else:
                return d[d.index(b) - 1], i


def dice_right(b, r):
    return r, 7 - b


def dice_left(b, r):
    return 7 - r, b

dice_pattern = [[2, 4, 5, 3],
                [1, 3, 6, 4],
                [1, 5, 6, 2],
                [1, 2, 6, 5],
                [1, 4, 6, 3],
                [2, 3, 5, 4]]
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
d_idx = 0
now_r = 0
now_c = 0
score = 0
dice_r = 3
dice_b = 6
def bfs(deep, _r, _c, number):
    global can_go
    end_flag = True
    for i in range(4):
        nr = _r + dr[i]
        nc = _c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            # print(_r, _c,visited[nr][nc],board[nr][nc], number)
            if not visited[nr][nc] and board[nr][nc] == number:
                visited[nr][nc] = True
                bfs(deep + 1, nr, nc, number)
                can_go += 1
                end_flag = False
    if end_flag:
        return

for _ in range(k):
    if 0 <= now_r + dr[d_idx % 4] < n and 0 <= now_c + dc[d_idx % 4] < m:
        now_r += dr[d_idx % 4]
        now_c += dc[d_idx % 4]
    else:
        now_r -= dr[d_idx % 4]
        now_c -= dc[d_idx % 4]
        d_idx += 2
    num = board[now_r][now_c]
    can_go = 1
    visited = [[False] * m for _ in range(n)]
    visited[now_r][now_c] = True
    bfs(0, now_r, now_c, num)
    score += (can_go * num)
    if d_idx % 4 == 0:
        dice_b, dice_r = dice_right(dice_b, dice_r)
    elif d_idx % 4 == 1:
        dice_b, dice_r = dice_down(dice_b, dice_r)
    elif d_idx % 4 == 2:
        dice_b, dice_r = dice_left(dice_b, dice_r)
    elif d_idx % 4 == 3:
        dice_b, dice_r = dice_up(dice_b, dice_r)


    if dice_b > board[now_r][now_c]:
        d_idx += 1
    elif dice_b < board[now_r][now_c]:
        d_idx += 3
print(score)