# BOJ 1932. 정수 삼각형 / D2
'''
문제
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.
맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
삼각형의 크기는 1 이상 500 이하이다. 삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.
입력
첫째 줄에 삼각형의 크기 n(1 ≤ n ≤ 500)이 주어지고, 둘째 줄부터 n+1번째 줄까지 정수 삼각형이 주어진다.
출력
첫째 줄에 합이 최대가 되는 경로에 있는 수의 합을 출력한다.
'''
import sys
input = sys.stdin.readline

N = int(input().strip())
tri = [list(map(int, input().split())) for _ in range(N)]
tri_dp = [[tri[0][0]]]+[[0]*(i+1) for i in range(1, N)]

for i in range(1, N):
    for j in range(i+1):
        if j == 0: # 왼쪽 끝일 때
            tri_dp[i][j] = tri_dp[i - 1][j] + tri[i][j]
        elif j == i: # 오른쪽 끝일 때
            tri_dp[i][j] = tri_dp[i - 1][j - 1] + tri[i][j]
        else: # dp 위에 있는 두 개중 큰 것을 더해서 범위 축소
            tri_dp[i][j] = max(tri_dp[i - 1][j - 1], tri_dp[i - 1][j]) + tri[i][j]

print(max(tri_dp[N-1]))

# 로직은 맞지만 메모리 시간 둘다 폭발하는 방식
'''
import sys
input = sys.stdin.readline
N = int(input().strip())
tri = [list(map(int, input().split())) for _ in range(N)]
tri_dp = [[tri[0][0]]]+[[] for _ in range(N-1)]
for i in range(N-1):
    for j in range(i+1):
        tri_dp[i+1].append(tri_dp[i][j] + tri[i+1][j])
        tri_dp[i+1].append(tri_dp[i][j] + tri[i+1][j+1])
print(max(tri_dp[N-1]))
'''

'''
일단 문제를 읽고 파스칼 삼각형과 매우 유사한 구조임을 확인하고
다이나믹 프로그래밍이라고 예상
처음에는 완전 구현으로 진행 ---> 틀렸습니다. (아마도 메모리초과 + 시간초과)
조금 더 축소시켜야 한다는 생각이 듦.
일단 큰 값을 구하는 것이기때문에 밑에 원소 입장에서 보면 위 두개 중 하나 선택해서 큰걸로 더하는 것으로 결점
양 끝은 선택권인 없으니 그냥 계산
'''
