# BOJ 16928. 뱀과 사다리 (D3 / G5)
#------------------------------------------------1회차 풀이
# 사다리랑 뱀만 인접리스트에 넣기?

import sys
from collections import deque

input = sys.stdin.readline
arr = [0]*101
N, M = map(int, input().split())

for _ in range(N):
    s, e = map(int, input().split())
    arr[s] = e

for _ in range(M):
    s, e = map(int, input().split())
    arr[s] = e

#방문 리스트, 큐 초기화
visited = [0] *101
q = deque([(1,0)])

# 이동 시작 (BFS)
while q:
    current, cnt = q.popleft()
    if current == 100:
        print(cnt)
        break
    
    # 모든 주사위 눈의 결과를 다음 후보로
    for dice in range(1,7):
        next_pos = current + dice
        if next_pos <= 100:
            # 뱀과 사다리가 있을 경우
            if arr[next_pos] != 0:
                next_pos = arr[next_pos]
            # 미방문시 방문체크, 큐 추가
            if visited[next_pos] == 0:
                visited[next_pos] = 1
                q.append((next_pos, cnt +1))