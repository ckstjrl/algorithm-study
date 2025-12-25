'''
# [Gold IV] 알고스팟 - 1261

[문제 링크](https://www.acmicpc.net/problem/1261)

### 성능 요약

메모리: 115040 KB, 시간: 128 ms

### 분류

그래프 이론, 그래프 탐색, 최단 경로, 데이크스트라, 격자 그래프, 0-1 너비 우선 탐색

### 제출 일자

2025년 9월 18일 23:10:40

### 문제 설명

<p>알고스팟 운영진이 모두 미로에 갇혔다. 미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다. 미로는 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.</p>

<p>알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 즉, 여러 명이 다른 방에 있을 수는 없다. 어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다. 즉, 현재 운영진이 (x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다. 단, 미로의 밖으로 이동 할 수는 없다.</p>

<p>벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 벽을 부수면, 빈 방과 동일한 방으로 변한다.</p>

<p>만약 이 문제가 <a href="https://www.algospot.com">알고스팟</a>에 있다면, 운영진들은 궁극의 무기 sudo를 이용해 벽을 한 번에 다 없애버릴 수 있지만, 안타깝게도 이 문제는 <a href="https://www.acmicpc.net">Baekjoon Online Judge</a>에 수록되어 있기 때문에, sudo를 사용할 수 없다.</p>

<p>현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 미로의 크기를 나타내는 가로 크기 M, 세로 크기 N (1 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 미로의 상태를 나타내는 숫자 0과 1이 주어진다. 0은 빈 방을 의미하고, 1은 벽을 의미한다.</p>

<p>(1, 1)과 (N, M)은 항상 뚫려있다.</p>

### 출력

 <p>첫째 줄에 알고스팟 운영진이 (N, M)으로 이동하기 위해 벽을 최소 몇 개 부수어야 하는지 출력한다.</p>

'''

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def dijkstra(i, j):
    global min_break

    q = deque([(i, j)])
    dists[i][j] = 0

    while q:
        now_i, now_j = q.popleft()

        for di, dj in dirs:
            new_i, new_j = now_i + di, now_j + dj
            if not (0 <= new_i < M and 0 <= new_j < N):
                continue
            if maze[new_i][new_j] == '0': # '0' 만나면 새치기 우선순위에 넣음
                new_dist = dists[now_i][now_j]
                if new_dist < dists[new_i][new_j]:
                    dists[new_i][new_j] = new_dist
                    q.appendleft((new_i, new_j))

            else:
                new_dist = dists[now_i][now_j] + 1 # '1'이면 넣긴 하지만 append로 넣음
                if new_dist < dists[new_i][new_j]:
                    dists[new_i][new_j] = new_dist
                    q.append((new_i, new_j))

    return dists[M - 1][N - 1]

N, M = map(int, input().split()) # N, M이 반대로 들어옴
maze = [list(input()) for _ in range(M)]

min_break = 0
INF = float('inf')
dists = [[INF] * N for _ in range(M)]
cnt = 0
result = dijkstra(0, 0)
print(result)