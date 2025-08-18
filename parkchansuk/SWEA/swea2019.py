# 2019. 더블더블 / D1
N = int(input())

arr = [0]*(N+1)
for i in range(N+1):
    arr[i] = 2 ** i

print(' '.join(map(str, arr)))