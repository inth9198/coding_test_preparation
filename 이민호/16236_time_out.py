n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
way = 1e9
target = (0, 0)
visited = []

def dfs(_prays, s_y, s_x, dgree, _baby): #너무 많이 돌거나 못 가면
    global way
    global target
    if not (0 <= s_x < n) or not (0 <= s_y < n):
        return
    # print((s_y, s_x),_prays)
    if (s_y, s_x) in _prays:
        if way > dgree:
            target = (s_y, s_x)
            way = dgree
        elif way == dgree:
            if target[0] > s_y:
                target = (s_y, s_x)
            elif target[0] == s_y:
                if target[1] > s_x:
                    target = (s_y, s_x)
        return
    if dgree > n * 2:
        return

    for i in range(4):
        #print(visited)
        if not (0 <= s_x + dx[i] < n) or not (0 <= s_y + dy[i] < n):
            continue
        if board[s_y + dy[i]][s_x + dx[i]] > _baby:
            continue
        if (s_y + dy[i], s_x + dx[i]) in visited:
            continue
        visited.append((s_y + dy[i], s_x + dx[i]))
        dfs(_prays, s_y + dy[i], s_x + dx[i], dgree + 1, _baby)
        visited.pop()
def shark(n):
    baby = 2
    time = 0
    stomach = 0
    global way
    global visited
    global target
    while True:
        prays = []
        for y in range(n):
            for x in range(n):
                if board[y][x] == 0:
                    continue
                elif board[y][x] == 9:
                    f_site = (y, x)
                elif board[y][x] < baby:
                    prays.append((y, x))
        #print(prays, len(prays))
        if len(prays) == 0:
            return time
        way = 1e9
        visited = []
        target = (-1, -1)
        board[f_site[0]][f_site[1]] = 0
        dfs(prays, f_site[0], f_site[1], 0, baby)
        if way == 1e9:
            return time
        time += way
        stomach += 1
        if stomach >= baby:
            baby += 1
            stomach = 0
        f_site = target
        #print(target)
        board[f_site[0]][f_site[1]] = 9
        #print(board, baby, time)
    return time

print(shark(n))
