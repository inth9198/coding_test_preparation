import sys
n = int(sys.stdin.readline())
nl = []

def is_ok():
    nln = len(nl)
    for i in range(1, nln//2 + 1):
        flag = False
        for j in range(i):
            if nl[nln - i + j] == nl[nln - i - i + j]:
                flag = True
            else:
                flag = False
                break
        if flag: #안좋은 수열
            return False
    return True
fl = False
def dfs():
    global fl
    if not is_ok():
        return
    if fl:
        return
    if len(nl) == n:
        if is_ok():
            fl = True
            for i in range(n):
                print(nl[i], end='')
            print('')
        return
    for i in range(1, 4):
        nl.append(i)
        dfs()
        nl.pop()

dfs()
