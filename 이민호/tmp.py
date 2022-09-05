dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
board = [[[] for _ in range(4)] for _ in range(4)]
fishes = []
for r in range(4):
    line = list(map(int, input().split()))
    for c in range(4):
        board[r][c] = (line[c*2] - 1, line[c*2+1] - 1)
        fishes.append([line[c*2] - 1, line[c*2+1] - 1, r, c])
fishes.sort(key=lambda x: x[0])
fishes[board[0][0][0]] = [0, 0, 0, 0]
score = board[0][0][0]
board[0][0] = (77, 77)

#죽을때 물고기즈 []로 만들고 가기
#보드에 0
#바꿀때는 불고기 끼리 꼬리 바꾸기
def go_fish_go():
    for fish in fishes:
        if len(fish) == 0:
            continue
        for i in range(8):
            new_i = (fish[1] + i) % 8
            if 0 <= fish[2] + dr[new_i] < 4 and 0 <= fish[3] + dc[new_i] < 4:
                if board[fish[2] + dr[new_i]][fish[3] + dc[new_i]][0] != 77:
                    new_r = fish[2] + dr[new_i]
                    new_c = fish[3] + dc[new_i]
                    fish[1] = new_i
                    #물고기 바꾸기 실행
                    if board[new_r][new_c][0] == 0:
                        board[new_r][new_c] = (fish[0], new_i)
                        board[fish[2]][fish[2]] = (0, 0)
                        fish[2] = new_r
                        fish[3] = new_c
                    else:
                        board[new_r][new_c] = (fish[0], new_i)
                        board[fish[2]][fish[3]] = (fishes[board[new_r][new_c][0]][0], fishes[board[new_r][new_c][0]][1])
                        tmp_r = fishes[board[new_r][new_c][0]][2]
                        tmp_c = fishes[board[new_r][new_c][0]][3]
                        fishes[board[new_r][new_c][0]][2] = fish[2]
                        fishes[board[new_r][new_c][0]][3] = fish[3]
                        fish[2] = tmp_r
                        fish[3] = tmp_c
print(board)
go_fish_go()
print(board)

