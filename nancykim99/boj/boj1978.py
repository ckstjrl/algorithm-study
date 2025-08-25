N = int(input())

arr = list(map(int, input().split()))

num_cnt = 0
for i in range(N):
    cnt = 0
    if arr[i] == 0 or arr[i] == 1:
        continue
    for j in range(2, arr[i]):
        if (arr[i] % j) != 0:
            cnt += 1
    if cnt == (arr[i] -2):
        num_cnt += 1

print(num_cnt)