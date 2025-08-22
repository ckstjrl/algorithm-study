T = int(input())
for test_case in range(1, 1+T):
    k = int(input())
    n = int(input())
    arr = [[0]*n for _ in range(k+1)]  # 계산에 필요한 층,호 만큼 0으로 된 2차원리스트 생성
    for i in range(k+1):
        for j in range(n):
            if i == 0:
                arr[i][j] = j+1  # 0층
            else:
                arr[i][j] = sum(arr[i-1][0:j+1])  # 1층 ~
    print(arr[k][n-1]) 