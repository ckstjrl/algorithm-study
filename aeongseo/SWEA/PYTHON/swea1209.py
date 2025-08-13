'''
1209. Sum
'''

for _ in range(10):
    tc = int(input())
    N = 100

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0

    # 행 우선 순회
    for i in range(N):
        col_sum = 0
        for j in range(N):
            col_sum += arr[i][j]

        if max_sum <= col_sum:
            max_sum = col_sum

    # 열 우선 순회
    for j in range(N):
        row_sum = 0
        for i in range(N):
            row_sum += arr[i][j]
        
        if max_sum <= row_sum:
            max_sum = row_sum

    # 대각선
    diagonal_sum_left = 0       # 왼쪽 대각선
    diagonal_sum_right = 0      # 오른쪽 대각선

    for i in range(N):

        diagonal_sum_left += arr[i][i]
        diagonal_sum_right += arr[i][N-1-i]
    
    if max_sum <= diagonal_sum_left:
        max_sum = diagonal_sum_left
    if max_sum <= diagonal_sum_right:
        max_sum = diagonal_sum_right
    
    print(f'#{tc} {max_sum}')

