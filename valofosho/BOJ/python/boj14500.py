"""
1. ㅗ 모양을 제외하면  3번의 이동을 통해 모든 모양은 만들어진다
우선은 그러면 ㅗ 모양만 제외하고 진행
"""
def check(i,j):
    if 0 <= i < N and 0 <= j < M:
        return True
    else:
        return False


def dfs(i,j,cnt, depth):
    global max_cnt

    # 3 번 기준 점에서 이동했다면 모양 완성!
    if depth == 3:
        #max_cnt랑 cnt랑 비교
        if max_cnt < cnt:
            max_cnt = cnt
        return
    
    di = [0,1,0,-1]
    dj = [1,0,-1,0]
    # 시작 점 visited
    visited[i][j] = 1
    for d in range(4):
        ni, nj = i+di[d], j+dj[d]
        if check(ni,nj) and visited[ni][nj] == 0:
            # visited[ni][nj] = 1
            dfs(ni, nj, cnt + maps[ni][nj], depth + 1)
            # visited[ni][nj] = 0
    # visited 풀어주기
    visited[i][j] = 0
    return 

# ㅗ 모양은 DFS로 돌아가며 찾을 수 없기 때문에 새로 함수를 작성
def mountain(i,j):
    global max_cnt
    # ㅜ
    if check(i,j) and check(i,j+1) and check(i,j+2) and check(i+1,j+1):
        cnt = maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i+1][j+1]
        max_cnt = max(max_cnt, cnt)
    # ㅏ
    if check(i,j) and check(i+1,j) and check(i+2,j) and check(i+1,j+1):
        cnt = maps[i][j] + maps[i+1][j] + maps[i+2][j] + maps[i+1][j+1]
        max_cnt = max(max_cnt, cnt)
    # ㅗ
    if check(i,j) and check(i,j+1) and check(i,j+2) and check(i-1,j+1):
        cnt = maps[i][j] + maps[i][j+1] + maps[i][j+2] + maps[i-1][j+1]
        max_cnt = max(max_cnt, cnt)
    # ㅓ
    if check(i,j) and check(i,j+1) and check(i-1,j+1) and check(i+1,j+1):
        cnt = maps[i][j] + maps[i][j+1] + maps[i-1][j+1] + maps[i+1][j+1]
        max_cnt = max(max_cnt, cnt)
    return



N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
max_cnt = 0
visited = [[0] * M for _ in range(N)]
# 모든 지점에서 시작하는 dfs 시작
for i in range(N):
    for j in range(M):
        dfs(i,j,maps[i][j],0)
        mountain(i,j)

print(max_cnt)