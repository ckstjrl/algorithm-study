N, M = map(int, input().split())
nums = list(map(int, input().split()))

ans = []

sum = [0] * (N + 1)
for i in range(N):
    sum[i + 1] = sum[i] + nums[i]

for _ in range(M):
    i, j = map(int, input().split())
    res = sum[j] - sum[i - 1]
    print(res)
