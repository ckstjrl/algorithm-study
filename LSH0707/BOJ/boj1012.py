from collections import deque
def find():  # 배추 심어져 있는 위치 i,j좌표 반환
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                return (i, j)
    return 0  # 배추 없으면 0 리턴

def worm(cnt):
    if find() == 0:  # 배추없으면 사용한 지렁이 수 반환
        return cnt
    else:
        si, sj = find()  # 배추 좌표 초기값
        q = deque()  # bfs
        q.append((si, sj))
        arr[si][sj] = 0
        while q:
            pi, pj = q.popleft()
            for di,dj in [[1,0],[-1,0],[0,1],[0,-1]]:  # 인접구역
                ni = pi + di
                nj = pj + dj
                if 0 <= ni < N and 0 <= nj < M:  # 범위안에 있고 아직 방문한곳이아니면 0으로 값변경
                    if arr[ni][nj] == 1:
                        arr[ni][nj] = 0
                        q.append((ni,nj))
        return worm(cnt+1)  # 한마리 풀고 난 이후 지렁이+1 하고 재귀

T = int(input())
for test_case in range(1, 1+T):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(K):
        a, b = map(int, input().split())
        arr[b][a] = 1 
    print(worm(0))