# BOJ1002: 터렛
import sys
import math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    # 원이 완전이 일치할 때
    if d == 0 and r1 == r2:
        print(-1)

    # 원이 떨어져있거나 안에 포함되어있을 때
    elif d > r1 + r2 or d < abs(r1 - r2):
        print(0)

    # 한 점에서 만날 때(내접, 외접)
    elif d == r1 + r2 or d == abs(r1 - r2):
        print(1)

    # 두 점에서 만나는 경우
    else:
        print(2)
