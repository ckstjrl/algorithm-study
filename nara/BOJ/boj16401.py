import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 1, 10**9
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in arr:
        cnt += i // mid
    if M <= cnt:
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1
print(ans)