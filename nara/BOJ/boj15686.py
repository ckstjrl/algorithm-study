import sys
input = sys.stdin.readline

N, M = map(int, input().split())
houses = []
chickens = []
for i in range(N):
    graph = list(map(int, input().split()))
    for j in range(N):
        if graph[j] == 1:
            houses.append([i, j])
        elif graph[j] == 2:
            chickens.append([i, j])

result = float('inf')
choose = []
def dfs(depth, idx):
    global result
    if depth == M:
        total_dist = 0
        for house in houses:
            tmp = 100
            for chicken in choose:
                dist = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
                tmp = min(dist, tmp)
            total_dist += tmp
        result = min(result, total_dist)
        return
    for i in range(idx, len(chickens)):
        choose.append(chickens[i])
        dfs(depth+1, i+1)
        choose.pop()

dfs(0, 0)
print(result)