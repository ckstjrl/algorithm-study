'''boj11404 - 플로이드
n(2 ≤ n ≤ 100)개의 도시가 있다. 
그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1 ≤ m ≤ 100,000)개의 버스가 있다. 
각 버스는 한 번 사용할 때 필요한 비용이 있다.

모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 도시의 개수 n이 주어지고 둘째 줄에는 버스의 개수 m이 주어진다. 
그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 
먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 
버스의 정보는 버스의 시작 도시 a, 도착 도시 b, 한 번 타는데 필요한 비용 c로 이루어져 있다. 
시작 도시와 도착 도시가 같은 경우는 없다. 비용은 100,000보다 작거나 같은 자연수이다.

시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
'''

# 플로이드-워셜 알고리즘을 사용하는 모든 쌍 최단 경로 문제

'''
모든 정점 쌍 사이의 최단 경로를 한 번에 구하는 알고리즘 
다익스트라가 "한 점에서 다른 모든 점"으로 가는 최단 경로를 구한다면, 
플로이드-워셜은 "모든 점에서 모든 점"으로 가는 최단 경로를 구함

중간에 k를 거쳐가면 더 빠를까?를 모든 경우에 대해 확인

A에서 B로 가는 방법:
1. 직접 가기: A → B
2. K를 거쳐가기: A → K → B

더 짧은 경로를 선택

# 1. 초기화
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0  # 자기 자신은 0

# 2. 간선 정보 입력
dist[a][b] = cost

# 3. 플로이드-워셜 (핵심!)
for k in range(n):          # 경유지
    for i in range(n):      # 출발지
        for j in range(n):  # 도착지
            # k를 거쳐가는게 더 빠르면 갱신
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])



k=1일 때: 1번만 경유지로 사용한 최단 경로
k=2일 때: 1,2번을 경유지로 사용한 최단 경로
k=3일 때: 1,2,3번을 경유지로 사용한 최단 경로
'''


import sys
input = sys.stdin.readline
INF = float('inf')

n = int(input()) # 도시의 개수
m = int(input()) # 버스의 개수

#dist[a][b] : a에서 b로 가는 비용
dist = [[INF] * (n + 1) for _ in range(n + 1)] # 거리 배열

# 자기 자신에게 가는 비용 0 
for i in range(1, n + 1):
    dist[i][i] = 0

# 간선 정보
for _ in range(m):
    a, b, c = map(int, input().split()) #a: 시작 도시, b: 도착 도시, c: 비용
    dist[a][b] = min(dist[a][b], c)

for k in range(1, n + 1): # 경유지
    for i in range(1, n + 1): # 출발지
        for j in range(1, n + 1): # 도착지
            if dist[i][j] > dist[i][k] + dist[k][j]: # 경유지면 a에서 k, k에서 j로 이동한 것
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()