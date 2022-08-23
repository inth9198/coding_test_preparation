import sys
def GCD(x, y):
    while y:
        x, y = y, x % y
    return x

n = int(sys.stdin.readline())
tree = []
for _ in range(n):
    tree.append(int(sys.stdin.readline()))
gaps = []
lg = tree[1] - tree[0]
for i in range(n - 1):
    gap = (tree[i + 1] - tree[i])
    lg = GCD(lg, gap)

print((tree[-1] - tree[0]) // lg - n + 1)
