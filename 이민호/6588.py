import sys
from collections import deque
input = sys.stdin.readline
is_prime = [True] * 1000001
is_prime[0] = False
is_prime[1] = False
prime_list = deque()
for i in range(1000001):
    if is_prime[i]:
        prime_list.append(i)
        for j in range(i + i, 1000001, i):
            is_prime[j] = False
while True:
    n = int(input())
    if n == 0:
        break
    for prime in prime_list:
        if is_prime[n-prime]:
            print(n, '=', prime, '+', n-prime)
            break