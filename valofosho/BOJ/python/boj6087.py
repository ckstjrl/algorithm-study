"""
BOJ6087 - 레이저 통신
문제 정의
1. W x H 지도, 각 칸은 빈칸, 벽, 두 칸은 'c'로 이루어짐
2. 'c'로 이루어진 두 칸을 레이저로 통신하기 위해 설치해야 하는 거울의 최소 개수
3. 레이저로 통신하는 건 두 칸을 레이저로 연결할 수 있다는 뜻
4. 레이저는 'c' 에서만 발사할 수 있고, 빈칸에 거울('/''\')을 설치해서 방향 90도 회전 가능

로직 생각
1. 무난한 길찾기 문제 같지만 과연 가장 빠른 길이 거울의 수가 최소라고 확언할 수 있을까?
2. 다익스트라를 회전의 수, 즉 거울의 수로 생각해야하지 않을까?
3. 방향은 왼쪽, 오른쪽, 직진만 가능, 뒤돌아보려면 180도인데 -

알고보니 사실은 그냥 갈 수 있는 길들에서 꺾는 수를 고르고 꺾는 수가 가장 작은 애를 하면 되는건 아닐까
난 천재야
천재의 설명 추가
1. 기존의 다익스트라나 BFS의 길찾기가 해당 좌표까지의 거리를 기반으로 min 값을 갱신하면서 진행했다면
2. 이 문제는 원하는 최소값이 회전, 즉 거울을 설치한 개수
3. 그러면 해당 좌표까지 가는데 꺾인 횟수를 기반으로 계속 값을 갱신하면 되지 않을까!
4. 회전을 한다는 것을 어떻게 알아야 할까? -> 강제로 직진, 좌회전, 우회전을 넣어! (cnt형식 +1 %4 이걸로)
5. 하지만 cost만 따지면 방향을 잃어...ㅜ -> 그럼 방향도 같이 넣어주는건 어때
6. 그러면 결국 맵을 0, 1 + dir로만 그려가는 0-1bfs혹은 다익스트라다




""" 
# 정답 풀이 -> (0-1 BFS 활용)
import sys
from collections import deque

input = sys.stdin.readline

def check(i,j):
    if 0<=i<N and 0<=j<M:
        return True
    else:
        return False
    

def bfs(start, goal):
    si, sj = start[0]
    q = deque([])
    # 시작 방향은 네 방향 모두 가능해서 다 0 처리, 큐에 추가
    for d in range(4):
        visited[si][sj][d] = 0
        q.append((si,sj,d))
    while q:
        ci, cj, d = q.popleft()
        ni, nj = ci+di[d], cj+dj[d]
        if check(ni,nj) and maps[ni][nj] != '*':
            # 방향은 그대로 직진인 경우 이전 값과 동일하게 진행
            if visited[ni][nj][d] > visited[ci][cj][d]:
                visited[ni][nj][d] = visited[ci][cj][d]
                # 0을 먼저 시작(사실상 직진을 끝까지 돌린다고 생각)
                q.appendleft((ni,nj,d))
        # 방향을 바꾸는 경우(좌, 우 로만)
        for nd in ((d + 1) % 4, (d - 1) % 4):
            ni, nj = ci+di[nd], cj+dj[nd]
            if check(ni,nj) and maps[ni][nj] != '*':
                # 비교는 방향을 바꾸기 전의 값과!
                cost = visited[ci][cj][d] + 1
                if visited[ni][nj][nd] > cost:
                    visited[ni][nj][nd] = cost
                    q.append((ni,nj,nd)) 

M, N = map(int, input().split())
INF = float('inf')
visited = [[[INF]*4 for _ in range(M)] for __ in range(N)]
maps = [list(input().strip()) for _ in range(N)]
start = []
goal = []
# 순서 중요 카운트 처리 할거라 그럼
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


# 찾아라, c의 위치
for i in range(N):
    for j in range(M):
        if maps[i][j] == 'C':
            if start:
                goal.append((i,j))
                break
            else:
                start.append((i,j))
bfs(start, goal)
gi, gj = goal[0]
print(min(visited[gi][gj]))














# 시간 초과 코드 - BFS Pruning
"""
import sys
from collections import deque
input = sys.stdin.readline
def bfs(x,y):
    queue = deque([(x,y)])
    visited[x][y] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            ## 동 남 서 북 순서
            nx, ny = x+dx[i], y+dy[i]
            while True:
                ## 범위를 벗어난다
                if not(0<=nx<n and 0<=ny<m): break
                ## 벽을 만난다
                if board[nx][ny]=='*': break
                ## 지난 적 있는 곳인데, 지금 경로로는 너무 많은 거울이 필요해서 break
                if visited[nx][ny] < visited[x][y]+1: break
                ## board업데이트, queue 추가
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                nx = nx+dx[i]
                ny = ny+dy[i]

if __name__=='__main__':
    ## 입력값
    m,n = map(int, input().split())
    board = [input() for _ in range(n)]

    ## 동 남 서 북
    dx = (0,1,0,-1)
    dy = (1,0,-1,0)

    ## C위치
    C = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'C':
                C.append((i,j))
    ## sx,sy : 시작지점
    ## ex,ey : 도착지점
    (sx,sy), (ex,ey) = C

    visited = [[float('inf')]*m for _ in range(n)]
    bfs(sx,sy)
    
    print(visited[ex][ey]-1)
"""