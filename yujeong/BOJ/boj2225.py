# 2225. 합분해

N, K = map(int, input().split())    # N까지의 수 K개를 더해서 N 만들기
dp = [[0] * (N+1) for _ in range(K+1)]

"""
N, K 규칙 찾아보기 
    0 1 2 3 4 5 6 7 8 9 10 ... [N]
0   0 0 0 0 0 ...
1   1 1 1 1 0 ...
2   1 2 3 4 5 6 ...
3   1 3 6 10 15 ...
4   1 4 10 ...
5   1 5 15 ...
6   1 6 21 ...
7   1 7 28 ...
...
[K]
"""

# case 1: K=0이면 경우의 수 0개
if K == 0:
    print(0)

# case 2: K=1이면 경우의 수는 1개
elif K == 1:
    print(1)

# 그 외: dp 배열 채워서 찾기 
else:
    for x in range(N+1):
        dp[2][x] = x+1
    # N까지의 수 K개를 더해 N을 만드는 경우의 수는
    # K-1개로 0~N에 대해 다 더한 값 (위 테이블 참고)
    for i in range(3, K+1):
        for j in range(N+1):
            dp[i][j] = sum(dp[i-1][:j+1])

    print(dp[K][N] % 1000000000)    # 형식에 맞게 출력

