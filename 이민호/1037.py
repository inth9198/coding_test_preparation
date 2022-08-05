yack = int(input())
y_list = list(map(int, input().split()))
y_list.sort()
print(y_list[0] * y_list[-1])
