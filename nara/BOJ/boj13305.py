import sys
input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))
res = 0

c = cost[0]
for i in range(N - 1):
    if c > cost[i]:
        c = cost[i]
    res += c * dist[i]

print(res)