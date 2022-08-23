n, m = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(n)]
homes = []
chickens = []
for y in range(n):
    for x in range(n):
        if _map[y][x] == 1:
            homes.append([y, x])
        elif _map[y][x] == 2:
            chickens.append([y, x])
from itertools import combinations
how_chickens = list(combinations(chickens, m))
answer = 1e6
for s_chickens in how_chickens:
    all_distance = 0
    for home in homes:
        distance = 1e6
        for s_chicken in s_chickens:
            if abs(s_chicken[0] - home[0]) + abs(s_chicken[1] - home[1]) < distance:
                distance = abs(s_chicken[0] - home[0]) + abs(s_chicken[1] - home[1])
        all_distance += distance
    if all_distance < answer:
        answer = all_distance
print(answer)