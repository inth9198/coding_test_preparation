import math
import sys
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True
prime_number = []

n = int(sys.stdin.readline())

for i in range(2, n+1):
    if is_prime_number(i):
        prime_number.append(i)

ret = 0
sum_p = [0] * (len(prime_number) + 1)
for i in range(1, len(prime_number) + 1):
    sum_p[i] = sum_p[i-1] + prime_number[i-1]
start = 0
end = 1

while start != len(prime_number):
    if sum_p[end] - sum_p[start] == n:
        ret += 1
        start += 1
    elif sum_p[end] - sum_p[start] > n:# 좁아져야함
        start += 1
    else:
        if end != len(prime_number):# 넓어져야함
            end += 1
        else:
            start += 1
[2,3,5,7]
[2,5,10,15,22]
print(ret)