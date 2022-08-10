wfrom itertools import combinations
import sys
n = int(sys.stdin.readline())
stack = [int(sys.stdin.readline()) for _ in range(n)]
stack = sorted(stack, reverse=True)
_max = -1
for i in range(len(stack) - 2):
    if stack[i] < stack[i+1] + stack[i+2]:
        _max = max(sum([stack[i], stack[i+1], stack[i+2]]), _max)
print(_max)
