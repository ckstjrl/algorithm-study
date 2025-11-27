"""
[문제]
체스판 위에 한 나이트가 놓여져 있다. 
나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 
나이트가 이동하려고 하는 칸이 주어진다. 
나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

[입력]
입력의 첫째 줄에는 테스트 케이스의 개수가 주어진다.
각 테스트 케이스는 세 줄로 이루어져 있다. 
첫째 줄에는 체스판의 한 변의 길이 l(4 ≤ l ≤ 300)이 주어진다. 
체스판의 크기는 l × l이다. 
체스판의 각 칸은 두 수의 쌍 {0, ..., l-1} × {0, ..., l-1}로 나타낼 수 있다. 
둘째 줄과 셋째 줄에는 나이트가 현재 있는 칸, 나이트가 이동하려고 하는 칸이 주어진다.

[출력]
각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력한다.
"""
import sys
from collections import deque
input = sys.stdin.readline

MOVES = [(-2, -1), (-2, +1), (-1, -2), (-1, +2),
         (+1, -2), (+1, +2), (+2, -1), (+2, +1)]

def bfs(l, si, sj, ei, ej):
    if si == ei and sj == ej:
        return 0
    dist = [[-1]*l for _ in range(l)]
    dist[si][sj] = 0
    q = deque([(si, sj)])
    while q:
        i, j = q.popleft()
        nd = dist[i][j] + 1
        for di, dj in MOVES:
            ni, nj = i + di, j + dj
            if 0 <= ni < l and 0 <= nj < l and dist[ni][nj] == -1:
                if ni == ei and nj == ej:   # 목표 발견 → 최소 이동
                    return nd
                dist[ni][nj] = nd
                q.append((ni, nj))
    return -1  # 이 문제에선 도달 불가 케이스는 거의 없음

T = int(input())
out = []
for _ in range(T):
    l = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split())
    out.append(str(bfs(l, si, sj, ei, ej)))

print("\n".join(out))