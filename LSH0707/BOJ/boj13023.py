N, M = map(int, input().split())
a = {}
for i in range(N):
    a[i] = []
for _ in range(M):  # 친구 dict에 친구정보 추가(양방향)
    x, y = map(int, input().split())
    a[x].append(y)
    a[y].append(x)
ans = 0
visited = [0] * N
def fr(s, cnt):  # fr(시작점, 카운트)
    global ans
    if ans == 1:  # ans=1이면 종료
        return
    if cnt == 4:  # 카운트=4면 ans=1
        ans = 1
        return
    for i in a[s]:  # 시작점의 친구중 하나 고르기
        if visited[i] == 0:  # 방문한적없는 친구면
            visited[i] = 1  # 방문기록
            fr(i, cnt+1)  # fr(시작점의 친구, 카운트+1)
            visited[i] = 0  # 방문기록 초기화
for i in range(N):  # 모든 시작점에대해 함수실행
    visited[i] = 1  # 시작점 방문기록
    fr(i,0)  # (시작점, 카운트0)
    visited[i] = 0  # 시작점 방문기록초기화
print(ans)
