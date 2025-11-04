'''
# [Silver I] 그림 - 1926

[문제 링크](https://www.acmicpc.net/problem/1926)

### 성능 요약

메모리: 120776 KB, 시간: 200 ms

### 분류

그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색, 격자 그래프, 플러드 필

### 제출 일자

2025년 9월 26일 00:29:29

### 문제 설명

<p>어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 대각선으로 연결이 된 것은 떨어진 그림이다. 그림의 넓이란 그림에 포함된 1의 개수이다.</p>

### 입력

 <p>첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다. (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)</p>

### 출력

 <p>첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이를 출력하여라. 단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.</p>

'''
from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

DIRS = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs(start_i, start_j) :
    q = deque([(start_i, start_j)])
    visited[start_i][start_j] = 1
    dist = 1

    while q :
        i, j = q.popleft()

        for di, dj in DIRS :
            ni, nj = i + di, j + dj
            if not (0 <= ni < n and 0 <= nj < m) : # 범위 체크
                continue
            if visited[ni][nj]: # 방문 체크
                continue
            if not graph[ni][nj] : # 연결되는 지 체크
                continue
            visited[ni][nj] = 1 # 표시
            dist += 1 # 거리 업데이트
            q.append((ni, nj)) # 다음 탐색 자리 추가
    return dist

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

max_dist = 0
cnt = 0
for i in range(n) :
    for j in range(m):
        if graph[i][j] and not visited[i][j] :
            cnt += 1
            max_dist = max(max_dist, bfs(i, j))

print(cnt)
print(max_dist)
