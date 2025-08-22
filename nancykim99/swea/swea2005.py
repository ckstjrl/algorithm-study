# 크기가 N인 파스칼의 삼각형
# 1. 첫번째 줄은 항상 숫자 1
# 2. 두번째 줄은 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합
# 1 <= N <= 10

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    arr = []
    for i in range(N):
        if i == 0:
            arr.append([1])
        else:
            arr_sub = []
            for j in range(i+1):
                if j == 0 or j == i:
                    arr_sub.append(1)
                else:
                    arr_sub.append(arr[i-1][j-1]+arr[i-1][j])
            arr += [arr_sub]
    
    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])

