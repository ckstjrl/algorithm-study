# 1916. 최소비용 구하기

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())    # 도시 개수
M = int(input())    # 버스 개수

# 버스 노선 인접 리스트로 만들기
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, v = map(int, input().split())
    graph[a].append((b, v))

# 출발점 도시번호, 도착점 도시번호 
start, end = map(int, input().split())

# 다익스트라로 출발점에서부터 최소비용 도달가능한 도시들 탐색 
def search(s):
    q = [(0, s)]
    visited = [1e9] * (N+1)
    visited[s] = 0
    while q:
        cost, nxt = heappop(q)
        if nxt == end:  # 도착점 도착하면 비용 리턴 
            return visited[end]
        if cost > visited[nxt]:
            continue
        for n, d in graph[nxt]:
            if visited[n] > visited[nxt] + d:
                visited[n] = visited[nxt] + d
                heappush(q, (visited[n], n))
    return visited[end]

ans = search(start)
print(ans)