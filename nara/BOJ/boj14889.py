import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visit = [False for _ in range(N)]
min_diff = float('inf')


def dfs(depth, idx):
    global min_diff
    if N//2 == depth:
        team1, team2 = 0, 0
        for i in range(N):
            for j in range(N):
                if visit[i] and visit[j]:
                    team1 += S[i][j]
                elif not visit[i] and not visit[j]:
                    team2 += S[i][j]
        min_diff = min(min_diff, abs(team1-team2))
        return
    for i in range(idx, N):
        if not visit[i]:
            visit[i] = True
            dfs(depth+1, i+1)
            visit[i] = False


dfs(0, 0)
print(min_diff)