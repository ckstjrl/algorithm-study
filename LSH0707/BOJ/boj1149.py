import sys
input = sys.stdin.readline
N = int(input())
arr = [0] * N
for i in range(N):
    a, b, c = map(int, input().split())
    arr[i] = (a, b, c)
cost = [[0]*3 for _ in range(N)]  # (x, y, z) -> 각 인덱스에서 RGB를 골랐을 경우의 최솟값
cost[0][0], cost[0][1], cost[0][2] = arr[0][0], arr[0][1], arr[0][2]
for i in range(1, N):  # dp
    cost[i][0] = arr[i][0] + min(cost[i - 1][1], cost[i - 1][2])
    cost[i][1] = arr[i][1] + min(cost[i - 1][0], cost[i - 1][2])
    cost[i][2] = arr[i][2] + min(cost[i - 1][1], cost[i - 1][0])
print(min(cost[N-1]))
