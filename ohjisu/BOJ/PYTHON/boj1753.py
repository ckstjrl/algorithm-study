'''
# [Gold IV] 최단경로 - 1753

[문제 링크](https://www.acmicpc.net/problem/1753)

### 성능 요약

메모리: 135432 KB, 시간: 444 ms

### 분류

그래프 이론, 최단 경로, 데이크스트라

### 제출 일자

2025년 9월 16일 21:58:26

### 문제 설명

<p>방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.</p>

### 입력

 <p>첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.</p>

### 출력

 <p>첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.</p>

'''

import sys
input = sys.stdin.readline
from heapq import heappush, heappop

# 모든 정점에 대해 최단 경로를 구하는 문제 == 다익스트라
# bfs 처럼 푸는데 가중치를 비교함
# heapq를 씀
def dijkstra(start_node) :
    pq = [(0, start_node)]
    dists[start_node] = 0

    while pq :
        dist, node = heappop(pq)

        if dists[node] < dist :
            continue

        for next_dist, next_node in graph[node] :
            new_dist = dist + next_dist

            # 새로 찍은 거리가 기존 거리보다 더 크거나 같다면 continue
            if dists[next_node] <= new_dist :
                continue

            dists[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    return dists

V, E = map(int, input().strip().split())
K = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E) :
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end)) # 단방향

INF = int(21e9)
dists = [INF for _ in range(V + 1)]


dists = dijkstra(K)

for i in range(1, V + 1) :
    if dists[i] == INF :
        print('INF')
    else :
        print(dists[i])