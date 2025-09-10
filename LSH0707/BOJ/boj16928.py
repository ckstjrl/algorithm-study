from collections import deque
N, M = map(int, input().split())
board = {}
for i in range(1, 106):
    board[i] = 0
for _ in range(N):  # 사다리 
    a, b  = map(int, input().split())
    board[a] = b
for _ in range(M):  # 뱀
    a, b = map(int, input().split())
    board[a] = b
visited = [0] * 106  # 1 ~ 105 방문기록
ans = 0
q = deque()  # bfs
q.append([1,0])  # [현재위치, 주사위횟수] 초기값
visited[1] = 0  # 방문기록
while q:
    p = q.popleft()
    cur = p[0]  # 현재위치
    cnt = p[1]  # 주사위횟수
    if cur == 100:  # 100 도착하면
        ans = cnt  # 주사위횟수 기록하고 break
        break
    for i in range(1, 7):  # 주사위 1~6
        n_cur = cur + i  # 현재위치 + 주사위 눈
        if board[n_cur] == 0 and visited[n_cur] == 0:  # 뱀이나 사다리 없는 칸
            visited[n_cur] = 1
            q.append([n_cur, cnt+1])  # [다음위치, 주사위횟수+1]
        elif board[n_cur] != 0 and visited[board[n_cur]] == 0:  # 뱀이나 사다리 있는 칸
            visited[board[n_cur]] = 1
            q.append([board[n_cur], cnt+1])  # [다음위치(뱀,사다리), 주사위횟수+1]
print(ans)
