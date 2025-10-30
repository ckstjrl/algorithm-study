from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dirs = [(-1,0),(1,0),(0,1),(0,-1)]

def check():  # 항상 외부공기인(0,0)부터 bfs로 외부공기 표시(0->내부공기 2->외부공기)
    visited = [[0]*M for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1
    arr[0][0] = 2
    while q:
        i, j = q.popleft()
        for di,dj in dirs:
            ni = i + di
            nj = j + dj
            if 0 <= ni < N and 0 <= nj < M:
                if visited[ni][nj] == 0:
                    if arr[ni][nj] == 0 or arr[ni][nj] == 2:
                        visited[ni][nj] = 1
                        q.append((ni, nj))
                        arr[ni][nj] = 2
def cheese(t):
    global time
    delete = []  # 녹은 치즈 좌표 리스트
    check()  # 외부공기 표시(2)
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:  # 치즈 격자 인접점이 외부공기인 경우 cnt+1
                cnt = 0
                for di,dj in dirs:
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < N and 0 <= nj < M:
                        if arr[ni][nj] == 2:
                            cnt = cnt + 1
                if cnt >= 2:  # 외부공기 2이상이면
                    delete.append((i, j))  # 녹은 치즈
    if delete:  # 녹은 치즈가 있으면 0으로 좌표값 변경 후 다음시간함수 재귀
        for i,j in delete:
            arr[i][j] = 0
        time = time + 1
        cheese(t+1)
    else:  # 없으면 종료
        return

time = 0
cheese(1)
print(time)