# 홀수는 홀수+짝수로밖에 이루어질 수 없고, 짝수인 소수는 2밖에 없기 때문에
# 홀수가 두 소수의 합이 되려면 2 + 홀수소수 인 경우밖에 없다.
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
check_list = [True] * 2000001

prime_list = deque()
check_list[0] = False
check_list[1] = False
for i in range(2, 2000001):
    if check_list[i]:
        prime_list.append(i)
        for k in range(i+i, 2000001, i):
            check_list[k] = False

for _ in range(t):
    a, b = map(int, input().split())
    s = a + b
    if s < 4:
        print("NO")
    elif s % 2 == 0:
        print('YES')
    else:
        s -= 2  # 홀수가 두 소수의 합이 되려면 2 + 홀수 소수 인 경우 밖에 없다.
        if s > 2000000:
            flag = True
            for prime in prime_list:
                if prime >= s:
                    break
                elif s % prime == 0:
                    print("NO")
                    flag = False
                    break
            if flag:
                print('YES')
        else:
            if check_list[s]:
                print('YES')
            else:
                print("NO")