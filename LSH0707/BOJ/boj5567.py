import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
friend = [[] for _ in range(n+1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)
for i in friend[1]:  # 1번의 친구 방문
    visited[i] = 1
    for x in friend[i]:  # 1번의 친구의 친구 방문
        visited[x] = 1
visited[1] = 0  # 1번 제외
print(sum(visited))