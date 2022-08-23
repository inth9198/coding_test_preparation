import sys
import math
_min, _max = map(int, sys.stdin.readline().split())
re = 0
graph = [False]*(_max - _min + 1)
for i in range(2, math.ceil(math.sqrt(_max) + 1)):
    start = math.ceil(_min/(i*i))
    while start * (i * i) <= _max:
        if not graph[start * (i * i) - _min]:
            graph[start * (i * i) - _min] = True
            re += 1
        start += 1

print(_max - _min - re + 1)
