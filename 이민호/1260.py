from collections import deque
def dfs(start):
    if visited[start] == 1:
        return
    visited[start] = 1
    print(start, end=' ')
    for gp in graph[start]:
        dfs(gp)


def bfs(start):
    Q = deque()
    Q.append(start)
    while Q:
        now = Q.popleft()
        if visited[now] == 0:
            print(now, end=' ')
            visited[now] = 1
        for gp in graph[now]:
            if visited[gp] == 0:
                Q.append(gp)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n + 1):
    graph[i].sort()
visited = [0] * (n + 1)
dfs(v)
visited = [0] * (n + 1)
print()
bfs(v)