'''boj14940 쉬운 최단거리
지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.
문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.

입력
지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)

다음 n개의 줄에 m개의 숫자가 주어진다.
0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 
입력에서 2는 단 한개이다.

출력
각 지점에서 목표지점까지의 거리를 출력한다. 
원래 갈 수 없는 땅인 위치는 0을 출력하고, 
원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.
'''
from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[-1]*m for _ in range(n)]

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

q = deque()

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            q.append([i, j])
            visited[i][j] = 0
            break
    
    if q:
        break

while q:
    ti, tj = q.popleft()

    for ni, nj in zip(di, dj):
        fi, fj = ti+ni, tj+nj
        if 0 <= fi < n and 0 <= fj < m and visited[fi][fj] == -1 and arr[fi][fj] != 0:
            visited[fi][fj] = visited[ti][tj] + 1 # 방문한 곳이 사실상 거리정보도 담고있음
            q.append([fi, fj])

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0 and visited[i][j] == -1: # 입력받은 지도상에서 갈수있는 곳인데 최종적으로 방문을 못함
            visited[i][j] = -1
        
        elif arr[i][j] == 0 and visited[i][j] == -1: # 지도에서 0이라 원래 못가서 방문 못한곳은 0
            visited[i][j] = 0

for i in visited:
    print(*i)