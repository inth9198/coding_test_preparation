from collections import deque
import copy
board = [deque([0] * 10) for _ in range(10)]
stack_lefts = []
stack_downs = []
def check_full():
    for _c in range(6, 10):
        flag = False
        for _r in range(4):
            if board[_r][_c] == 0:
                flag = True
                break
        if not flag:
            # print('holla')
            stack_lefts.append(_c)
            # print(stack_lefts, _c)
    for _r in range(6, 10):
        flag = False
        for _c in range(4):
            if board[_r][_c] == 0:
                flag = True
                break
        if not flag:
            # print('solla')
            stack_downs.append(_r)

def check_up():
    stack_left_ = 0
    for c in range(4, 6):
        for r in range(4):
            if board[r][c] == 1:
                stack_left_ += 1
                break
    stack_down_ = 0
    for r in range(4, 6):
        for c in range(4):
            if board[r][c] == 1:
                stack_down_ += 1
                break
    return stack_left_, stack_down_
n = int(input())
order = [list(map(int, input().split())) for _ in range(n)]
score = 0
for i in range(n):
    starts = []
    if order[i][0] == 1:
        #x가 행이래
        starts.append([order[i][1], order[i][2]])
    elif order[i][0] == 2:
        starts.append([order[i][1], order[i][2]])
        starts.append([order[i][1], order[i][2] + 1])
    elif order[i][0] == 3:
        starts.append([order[i][1], order[i][2]])
        starts.append([order[i][1] + 1, order[i][2]])
    #left 먼저
    left_starts = copy.deepcopy(starts)
    down_starts = copy.deepcopy(starts)
    while True:
        stop_flag = False
        for start in left_starts:
            start[1] += 1
            #여기서 아직 안떨어졌는데 멈춰버림
            if start[1] > 9:
                stop_flag = True
                continue
            if board[start[0]][start[1]] == 1:
                stop_flag = True
                continue
        if stop_flag:
            for left_start in left_starts:
                board[left_start[0]][left_start[1] - 1] = 1
            break
    while True:
        stop_flag = False
        for start in down_starts:
            start[0] += 1
            if start[0] > 9:
                stop_flag = True
                continue
            if board[start[0]][start[1]] == 1:
                stop_flag = True
                continue
        if stop_flag:
            for down_start in down_starts:
                board[down_start[0] - 1][down_start[1]] = 1
            break
    stack_lefts = []
    stack_downs = []
    check_full()
    # print(stack_lefts,stack_downs)

    stack_lefts.reverse()
    stack_downs.reverse()
    score += len(stack_lefts)
    double = 0
    for stack_left in stack_lefts:
        for tmp_r in range(4):
            board[tmp_r][stack_left + double] = 0
        for tmp_c in range(stack_left + double, 3, -1):
            for tmp_r in range(4):
                board[tmp_r][tmp_c] = board[tmp_r][tmp_c - 1]
        double += 1
    score += len(stack_downs)
    double = 0
    for stack_down in stack_downs:
        for tmp_c in range(4):
            board[stack_down + double][tmp_c] = 0
        for tmp_r in range(stack_down + double, 3, -1):
            for tmp_c in range(4):
                board[tmp_r][tmp_c] = board[tmp_r - 1][tmp_c]
        double += 1


    left_up, down_up = check_up()
    for _ in range(left_up):
        for tmp_c in range(9, 3, -1):
            for tmp_r in range(4):
                board[tmp_r][tmp_c] = board[tmp_r][tmp_c - 1]
    for _ in range(down_up):
        for tmp_r in range(9, 3, -1):
            for tmp_c in range(4):
                board[tmp_r][tmp_c] = board[tmp_r - 1][tmp_c]
tile = 0
for r in range(6, 10):
    for c in range(4):
        if board[r][c] == 1:
            tile += 1
for c in range(6, 10):
    for r in range(4):
        if board[r][c] == 1:
            tile += 1
print(score)
print(tile)
# 1. revers는 반환 값이 없다
# 2. 이것 저것 꼼꼼하지못함
