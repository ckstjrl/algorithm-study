N, K = map(int, input().split())

visited = [-1] * 100001

front, rear = -1, -1
q = [0]* 100001
rear += 1
q[rear] = N
visited[N] = 0

while front != rear:
    front += 1
    N = q[front]
    if N == K:
        break
    for i in [N+1,N-1,N*2]:
        if 0 < i < 100001 and visited[i] < 0:
            visited[i] = visited[N]+1
            rear+=1
            q[rear] = i    
    
print(visited[K])
