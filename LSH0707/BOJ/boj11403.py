N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = [[0] * N for _ in range(N)]
edge = [[] for _ in range(N)]  # 부모 자식 리스트
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            edge[i].append(j)

def dfs(idx):  # dfs로 한 정점에서 도착할 수 있는 모든 경로 1로 바꾸기
    stack = []
    for i in edge[idx]:
        ans[idx][i] = 1
        stack.append(i)
    while stack:
        a = stack.pop()
        for i in edge[a]:
            if ans[a][i] == 0 or ans[idx][i] == 0:
                ans[a][i] = 1
                ans[idx][i] = 1
                stack.append(i)

for i in range(N):  # 모든 정점에 대해 dfs
    dfs(i)
    print(*ans[i])