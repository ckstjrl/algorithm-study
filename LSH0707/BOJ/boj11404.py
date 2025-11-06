import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
bus = [[float('inf')]*n for _ in range(n)]  # 초기 (i -> j) 비용 설정
for _ in range(m):
    a, b, c = map(int, input().split())
    if bus[a-1][b-1] > c:
        bus[a-1][b-1] = c
for i in range(n):  # 자기 자신으로 가는 노선 x
    bus[i][i] = 0
for x in range(n):  # 모든 (i -> j) 와 (i -> x -> j) 비교해서 최소 비용 갱신
    for i in range(n):
        for j in range(n):
            bus[i][j] = min(bus[i][j], bus[i][x] + bus[x][j])
for i in range(n):
    for j in range(n):
        if bus[i][j] == float('inf'):  # 없는 경로는 0으로 처리
            bus[i][j] = 0
for i in range(n):
    print(*bus[i])
