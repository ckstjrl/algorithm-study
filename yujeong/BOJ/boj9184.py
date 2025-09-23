# 9184. 신나는 함수 실행
import sys
input = sys.stdin.readline

# 함수 계산 결과를 미리 저장해둘 리스트 dp
# 0보다 작거나 20보다 큰 a, b, c에 대해서는 함수 결과값이 고정되므로 고려할 필요 x
dp = [[[0]*21 for _ in range(21)] for _ in range(21)]

# 구현해야 하는 함수 w
def w(a, b, c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20, 20, 20)
    
    # dp에 저장해둔 결과값이면 바로 리턴 
    if dp[a][b][c]:
        return dp[a][b][c]
    
    # 계산하며 결과값을 dp에 저장해 다음에 활용할 수 있게 함
    if a<b<c:
        # dp에 기록
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)  
    else:
        # dp에 기록
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]


i, j, k = map(int, input().split())
while not(i == j == k == -1):
    print(f'w({i}, {j}, {k}) = {w(i, j, k)}')
    i, j, k = map(int, input().split())