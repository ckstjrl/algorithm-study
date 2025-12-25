N, K = map(int, input().split())  # N사람수, M타겟
arr = [0] * N  # i -> arr[i] 지목
for i in range(N):
    a = int(input())
    arr[i] = a
visited = [0] * N
ans = 0
stack = []
stack.append(0)  # 0번 게임 시작
visited[0] = 1
while stack:  # BFS
    next = stack.pop()
    if visited[arr[next]] == 0:  # 방문기록없으면 횟수+1, append
        ans = ans + 1
        if arr[next] == K:  # K걸리면 방문기록하고 break
            visited[arr[next]] = 1
            break
        else:  # K안걸리면 DFS 계속 진행
            stack.append(arr[next])
            visited[arr[next]] = 1
if visited[K] == 1:  # K방문기록 있으면 횟수 출력
    print(ans)
else:
    print(-1)