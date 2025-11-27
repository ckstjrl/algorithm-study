# 준환이의 운동관리 / D3
T = int(input())
for tc in range(1, T+1):
    L, U, X = map(int, input().split())

    ex_time = -1
    if X < L:
        ex_time = L - X
    elif L <= X <= U:
        ex_time = 0

    print(f'#{tc} {ex_time}')