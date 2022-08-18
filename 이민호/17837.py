import sys

n, k = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
horses = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
board_horses = [[[] for _ in range(n)] for _ in range(n)]
for i, horse in enumerate(horses):
    r, c = horse[0] - 1, horse[1] - 1
    board_horses[r][c].append(i)
    if len(board_horses[r][c]) >= 4:
        print(0)
        exit()
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
time = 0
while True:
    time += 1
    if time > 1000:
        print(-1)
        break
    for i, horse in enumerate(horses):
        r, c = horse[0] - 1, horse[1] - 1

        for j, h_s in enumerate(board_horses[r][c]):
            if h_s == i:
                get_idx = j
        #이거 옯기고 말들도 수정해야 함
        d = horse[2] - 1
        nr = r + dr[d]
        nc = c + dc[d]
        blue = False
        if 0 <= nr < n and 0 <= nc < n:
            if board[nr][nc] == 0 or board[nr][nc] == 1:
                have_to_move = board_horses[r][c][get_idx:]
                board_horses[r][c] = board_horses[r][c][:get_idx]
                if board[nr][nc] == 1:
                    have_to_move.reverse()
                for htm in have_to_move:
                    board_horses[nr][nc].append(htm)
                    if len(board_horses[nr][nc]) >= 4:
                        print(time)
                        exit()
                    horses[htm][0] = nr + 1
                    horses[htm][1] = nc + 1
            else:
                blue = True
        else:
            blue = True
        if blue:
            d = horse[2] - 1
            if d == 0 or d == 2:
                horse[2] += 1
            else:
                horse[2] -= 1
            d = horse[2] - 1
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                if board[nr][nc] == 0 or board[nr][nc] == 1:
                    have_to_move = board_horses[r][c][get_idx:]
                    board_horses[r][c] = board_horses[r][c][:get_idx]
                    if board[nr][nc] == 1:
                        have_to_move.reverse()
                    for htm in have_to_move:
                        board_horses[nr][nc].append(htm)
                        if len(board_horses[nr][nc]) >= 4:
                            print(time)
                            exit()
                        horses[htm][0] = nr + 1
                        horses[htm][1] = nc + 1