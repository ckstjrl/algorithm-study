import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

# 사다리든 뱀이든 둘 다 첫 번째 칸에 도착하면 두 번째 칸으로 이동함
move = dict()
for _ in range(N + M):
    a, b = map(int, sys.stdin.readline().split())
    move[a] = b

board = [0] * 101
visited = [0] * 101

q = deque([1])
while q:
    x = q.popleft()
    if x == 100: # 100번째 칸에 도착했을 시
        print(board[x])
        break
    for dice in range(1, 7):
        next_place = x + dice
        if next_place <= 100 and visited[next_place] == 0:
            if next_place in move.keys():
                next_place = move[next_place]
            if visited[next_place] == 0:
                visited[next_place] = 1
                board[next_place] = board[x] + 1
                q.append(next_place)