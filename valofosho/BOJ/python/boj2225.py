"""
BOJ2225 - 합분해

문제 정의
1. 0~N 까지의 정수 K 개를 더해서 합이 N이 되는 경우의 수를 구해라
2. 덧셈의 순서가 바뀐 경우는 다른 경우로 센다.
3. 한 개의 수를 여러 번 사용할 수 있다.

생각 정의
문제에서 바라는 바는 그런게 아닐까
숫자들의 조합을 먼저 고른 뒤에
그 숫자들을 나열하는 경우를 구하는게 맞지 않을까

로직 정의
1. DP 테이블을 0~N, 1~K 까지 만들기(2차원)
2. DP 테이블의 규칙은 DP[i][j] = DP[i-1][j] + DP[i][j-1]
3. 주의사항! DP 테이블에서 0을 K개로 만드는 경우도 확장해야한다!!!

"""

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# N을 1개의 숫자로 만드는 경우 채워넣기
top = [[1] * (N+1)]
DP = top + [[0]*(N+1) for _ in range(K-1)]
# 0을 K개로 만드는 경우도 채워넣기
for i in range(1,K):
    DP[i][0] = 1
for i in range(1,K):
    for j in range(1,N+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1]
print(DP[K-1][N] % 1000000000)