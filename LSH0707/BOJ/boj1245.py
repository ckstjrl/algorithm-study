import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
peak = []  # 산봉우리 후보 리스트
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        peak_p = []
        stack = []
        if arr[i][j] >= 1 and visited[i][j] == 0:  # 1보다 큰 경우 방문처리, 스택에 append
            peak_p.append((i, j))
            visited[i][j] = 1
            stack.append((i, j))
        while stack:  # 인접한 구역 중에 같은 높이인 좌표 dfs
            si, sj = stack.pop()
            for di, dj in [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]:
                ni = si + di
                nj = sj + dj
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] == arr[si][sj] and visited[ni][nj] == 0:
                        peak_p.append((ni, nj))
                        visited[ni][nj] = 1
                        stack.append((ni, nj))
        if peak_p:  # 같은 높이 좌표 리스트 후보리스트에 append
            peak.append(peak_p)

def is_peak(lst):
    h = arr[lst[0][0]][lst[0][1]]  # 산봉우리 높이
    for si,sj in lst:  # 산봉우리 후보의 모든 좌표의 모든 인접구역의 높이가 산봉우리 높이보다 낮은 경우 1, 아니면 0 리턴
        for di,dj in [[-1,0],[1,0],[0,-1],[0,1],[-1,-1],[-1,1],[1,-1],[1,1]]:
            ni = si + di
            nj = sj + dj
            if (ni,nj) not in lst:
                if 0 <= ni < N and 0 <= nj < M:
                    if arr[ni][nj] >= h:
                        return 0
    return 1

ans = 0
for i in range(len(peak)):  # 산봉우리 후보 순회
    ans = ans + is_peak(peak[i])
print(ans)
