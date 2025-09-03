from collections import deque
N = int(input())
arr = [[] for _ in range(N + 1)] 
for _ in range(N - 1):  # 노드 정보(양방향) 추가
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

P = [0] * (N + 1)  
visited = [False] * (N + 1)

def parents(start):
    q = deque([start])  # 초기값
    visited[start] = True 

    while q:
        a = q.popleft()
        for i in arr[a]:
            if not visited[i]:
                P[i] = a  # 부모 노드 기록
                visited[i] = True  # 방문 기록
                q.append(i)  # 자식 다음 큐에 추가

parents(1)

for i in range(2, N + 1):
    print(P[i])