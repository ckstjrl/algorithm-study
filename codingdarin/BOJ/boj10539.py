# BOJ 10539 수빈이와 수열 (B2 / D1)
n = int(input())
arr = list(map(int, input().split()))

old = 0
for i in range(n):
    now = arr[i]*(i+1) - old
    print(now, end=' ')
    old += now
    