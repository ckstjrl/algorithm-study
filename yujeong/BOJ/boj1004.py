# 1004. 어린왕자

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    x1, y1, x2, y2 = map(int, input().split())  # 출발점 (x1, y1), 도착점 (x2, y2)
    n = int(input())                            # 행성 개수
    stars = [list(map(int, input().split())) for _ in range(n)]     # 행성 중점과 반지름 (cx, cy, r)

    cnt = [0] * n           # 각 행성별로, 출발점 or 도착점이 행성 내부에 있는지 
    for i in range(n):
        cx, cy, r = stars[i]
        if ((x1-cx)**2 + (y1-cy)**2) < r**2:    # 출발점이 행성 내부에 있으면 +1
            cnt[i] += 1
        if ((x2-cx)**2 + (y2-cy)**2) < r**2:    # 도착점이 행성 내부에 있으면 +1
            cnt[i] += 1
    
    # 출발점 또는 도착점 중 1개만 행성 내부에 있으면 그만큼 경계를 건너야 함
    cross_cnt = sum(x for x in cnt if x==1)
    print(cross_cnt)
