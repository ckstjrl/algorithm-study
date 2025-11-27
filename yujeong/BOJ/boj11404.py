# 11404. 플로이드

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())    # 도시의 개수
M = int(input())    # 버스의 개수

graph = [[] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split()) # 출발 도시, 도착 도시, 비용
    graph[a].append((b, c))

# s번 도시에서 시작해 다익스트라로 탐색하며 각 도시까지 도달하기 위한 최소 비용 찾기
def search(s):
    visited = [1e9] * (N+1)     # 임의의 큰 값으로 비용들 초기화 
    visited[s] = 0
    q = [(0, s)]
    while q:
        dist, nxt = heappop(q)
        if dist > visited[nxt]:     # 더 작은 비용으로 도달가능하면 패스
            continue
        for n, d in graph[nxt]:     # 다음 연결된 도시에 대해
            if visited[n] > visited[nxt] + d:   # 더 최소비용으로 도달 가능하면
                visited[n] = visited[nxt] + d   # 비용 갱신
                heappush(q, (visited[n], n))
    # 도달 불가능하면 (아직 초기값으로 남음) 0으로 바꿔주기
    result_lst = [0 if x == 1e9 else x for x in visited[1:]]
    return result_lst   # 비용 리스트 리턴

for x in range(1, N+1):
    result = search(x)  # 1번부터 시작해 각 도시별로 다익스트라 탐색
    print(*result)      # 비용 리스트 출력