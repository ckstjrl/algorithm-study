T = int(input())
for test_case in range(1, 1+T):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append([0]*(i+1))
    arr[0][0] = 1
    for i in range(1, N):
        for j in range(len(arr[i])):
            arr[i][0] = 1
            arr[i][i] = 1
            if arr[i][j] == 0:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
 
    print(f'#{test_case}')
    for i in range(N):
        print(*arr[i])