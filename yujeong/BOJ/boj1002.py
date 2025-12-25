# 1002. 터렛

import sys
import math
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # (x1, y1)에서 r1만큼, (x2, y2)에서 r2만큼 떨어진 점이 위치할 수 있는 곳의 경우의 수 찾기
    # 각 점을 중심으로 해서 r1, r2 반지름을 갖는 원이 있을 때 ...

    # (x1, y1), (x2, y2) 거리 미리 구하기
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    # case 1. 무한대인 경우
    # 두 원이 겹칠 때
    if d == 0 and r1 == r2:
        print(-1)

    # case 2. 1개인 경우
    # 두 원이 외접 (반지름 합 == d)
    elif (r1 + r2) == d:
        print(1)

    # 두 원이 내접 (반지름 차 == d)
    elif abs(r1 - r2) == d:
        print(1)

    # case 3. 2개인 경우
    # d가 내접할 때보다 크고 외접할 때보다 작음
    elif abs(r1 - r2) < d < (r1 + r2):
        print(2)

    # 그 외 = 0개
    else:
        print(0)