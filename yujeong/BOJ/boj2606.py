# 2606. 바이러스

def bfs():
    q = []
    q.append(0)

    while q:
        pos = q.pop(0)
        for e in edges:     # 연결되어 있는 컴퓨터들에 대해 탐색
            if e[0] == pos and not visited[e[1]]:   # 감염되지 않은 컴퓨터면
                q.append(e[1])          # 큐에 추가
                visited[e[1]] = True    # 연결된 컴퓨터도 감염된 컴퓨터

N = int(input())
k = int(input())
edges = []              # 연결된 쌍을 담을 리스트
visited = [False] * N   # 바이러스에 걸렸는지 여부를 체크할 리스트
visited[0] = True       # 1번 컴퓨터가 바이러스에 걸린 것에서 시작

for _ in range(k):
    x, y = map(int, input().split())
    # 연결 쌍방향을 모두 edges에 추가 
    edges.append((x-1, y-1))
    edges.append((y-1, x-1))

bfs()

print(sum(visited)-1)