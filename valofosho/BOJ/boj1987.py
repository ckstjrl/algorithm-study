"""
상하좌우 인접 칸 이동
새로 이동한 칸에 적힌 알파벳은 모든 칸에 있던 애랑 달라야 한다
말이 갈 수 있는 최대한의 수
시작 자리 문자열에 + 로 가는 곳 문자열 더하기
cnt를 1부터 dfs돌리면서 최대값 찾기 만약 len(str) 과 cnt가 다르면 break

"""
# 최초 제출 버전 (DFS + 문자열 사용) - 6100ms
import sys
input = sys.stdin.readline

def check(i,j):
    if 0<=i<R and 0<=j<C:
        return True
    else:
        return False


def dfs(i, j, cnt, string):
    global answer
    if cnt > answer:
        answer = cnt
    
    visited[i][j] = True
    for d in range(4):
        ni,nj = i+di[d], j+dj[d]
        if check(ni,nj) and maps[ni][nj] not in string:
            if not visited[ni][nj]:
                visited[ni][nj] = True
                dfs(ni,nj,cnt+1, string + maps[ni][nj])
    visited[i][j] = False

R, C = map(int, input().split())
maps = [list(input().strip()) for _ in range(R)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

visited = [[False] * C for _ in range(R)]
answer = 0
dfs(0,0,1,maps[0][0])
print(answer)

# 2번 풀이 (DFS + set 활용) - 6472ms
import sys
input = sys.stdin.readline

def check(i,j):
    return 0<=i<R and 0<=j<C

def dfs(i, j, cnt, string):
    global answer
    answer = max(answer, cnt)
    if answer == 26:
        return

    for d in range(4):
        ni, nj = i+di[d], j+dj[d]
        if check(ni,nj) and maps[ni][nj] not in string:
            string.add(maps[ni][nj])
            dfs(ni,nj,cnt+1,string)
            string.remove(maps[ni][nj])  # 백트래킹

R, C = map(int, input().split())
maps = [list(input().strip()) for _ in range(R)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

answer = 0
dfs(0,0,1,set(maps[0][0]))
print(answer)
