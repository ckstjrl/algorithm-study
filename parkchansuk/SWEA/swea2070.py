# 큰 놈, 작은 놈, 같은 놈 / D1
T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())

    if A > B:
        equ = '>'
    elif A < B:
        equ = '<'
    else:
        equ = '='
    
    print(f'#{tc} {equ}')