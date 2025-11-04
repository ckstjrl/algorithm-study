# 16928. 뱀과 사다리 게임

import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())
board = list(range(101))        # 1~100 칸; 기본적으로 각 칸에 자기 자신 
for _ in range(N+M):            # 사다리, 뱀 정보 담기 (start 칸에서 end 칸으로 이동)
    start, end = map(int, input().split())
    board[start] = end

cnt = [-1] * 101    # 각 칸에 도착하기 위해 주사위 굴린 횟수 저장
cnt[1] = 0
ans = 0

q = deque([board[1]]) # 이동한 칸 담을 큐

while q:
    pos = q.popleft()

    if pos == 100:      # 100에 도착
        ans = cnt[pos]
        break

    for i in range(6): # 주사위 굴리기
        next_pos = pos + i + 1
        if next_pos > 100:
            continue
        next_pos = board[next_pos]  # 사다리나 뱀 있으면 이동
        if cnt[next_pos] == -1:     # 방문한 적 없는 칸이면 이동
            cnt[next_pos] = cnt[pos] + 1    # 주사위 굴린 횟수 갱신
            q.append(next_pos)

print(ans)