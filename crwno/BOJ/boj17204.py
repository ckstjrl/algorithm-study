N, K = map(int, input().split())
point = []
for _ in range(N):
    j = int(input())
    point.append(j)

visited = [False] * N
cnt = 0
start = 0
while True:
    if not visited[start]:
        visited[start] = True
        cnt += 1
        n_start = point[start]
        start = n_start
    else:
        cnt = -1
        break
    if start == K:
        break

print(cnt)