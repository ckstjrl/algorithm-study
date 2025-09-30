import sys
input = sys.stdin.readline

N = int(input())
arr = [list(input()) for _ in range(N)]

def check():
    max_cnt = 1
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if arr[i][j] == arr[i][j - 1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)
        cnt = 1
        for j in range(1, N):
            if arr[j][i] == arr[j - 1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(cnt, max_cnt)

    return max_cnt


result = 1
for i in range(N):
    for j in range(N - 1):
        if j + 1 < N and arr[i][j] != arr[i][j + 1]:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            result = max(result, check())
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        if i + 1 < N and arr[i][j] != arr[i + 1][j]:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            result = max(result, check())
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(result)