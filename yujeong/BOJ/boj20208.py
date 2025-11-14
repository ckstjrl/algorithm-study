# 20208. 진우의 민트초코우유

import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())     # 마을 크기 N, 초기 체력 M, 체력 증가량 H
# grid = [list(map(int, input().split())) for _ in range(N)]
hx, hy = 0, 0
milks = []
ans = 0

# 입력받으며 집 위치, 우유들 위치 찾기
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            hx, hy = i, j   # 집 위치 
        elif row[j] == 2:
            milks.append((i, j))    # 우유 위치

visited = [False] * len(milks)  # 우유들 마셨는지 여부 저장

# 백트래킹으로 다음 우유를 마실 수 있는지 체크
def backtracking(px, py, hp, cnt):
    global ans
    # 남은 우유를 다 마셔도 ans 최댓값을 갱신할 수 없는 경우 리턴
    if cnt + len(milks) - sum(visited) <= ans:
        return

    # 집으로 갈 체력이 남은 경우 현재까지 마신 우유 개수로 ans 갱신 
    to_home = abs(px - hx) + abs(py - hy)
    if to_home <= hp:
        ans = max(ans, cnt)

    # 백트래킹 탐색
    for x in range(len(milks)):     # x: 우유 인덱스 
        if not visited[x]:          # 아직 마신 적 없는 우유면
            nx, ny = milks[x][0], milks[x][1]       # 다음 우유를 milk[x]로
            milk_dist = abs(px - nx) + abs(py - ny) # 다음 우유까지 갈 수 있으면
            if milk_dist > hp:
                continue
            visited[x] = True       # milk[x] 마시고 다음 탐색
            backtracking(nx, ny, hp - milk_dist + H, cnt+1)
            visited[x] = False      # 복구 

backtracking(hx, hy, M, 0)  # 탐색 시작
print(ans) 