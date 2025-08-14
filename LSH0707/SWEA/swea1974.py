T = int(input())
for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    for i in range(9):
        sum_a = 0
        sum_b = 0
        for j in range(9):
            sum_a = sum_a + arr[i][j]
            sum_b = sum_b + arr[j][i]
        if sum_a != 45:
            result = 0
        if sum_b != 45:
            result = 0

    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            sum_c = 0
            for di, dj in [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]:
                ni = i + di
                nj = j + dj
                sum_c = sum_c + arr[ni][nj]
            if sum_c != 45:
                result = 0
    
    print(f'#{test_case} {result}')