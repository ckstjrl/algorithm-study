# BOJ10844(D2): 쉬운 계단 수
N = int(input())
dp = [[0] * 10 for _ in range(N + 1)]

# 길이가 1인 쉬운 계단 수 초기화
for j in range(1, 10):
    dp[1][j] = 1

# 점화식을 이용한 계산
for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][1]
    dp[i][9] = dp[i - 1][8]
    for j in range(1, 9):
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1])

result = sum(dp[N]) % 1000000000
print(result)

# 메모리 터졌음
# from collections import deque

# N = int(input())
# q = deque([(x, 1) for x in range(1, 10)])
# cnt = 0

# while q:
#     node, depth = q.popleft()

#     # 깊이가 N이라면 cnt += 1 하고 continue
#     if depth == N:
#         cnt += 1
#         continue
    
#     # 각 노드의 경우마다 appendleft로 추가
#     if node == 0:
#         q.appendleft((1, depth + 1))
#     elif node == 9:
#         q.appendleft((8, depth + 1))
#     else:
#         q.appendleft((node - 1, depth + 1))
#         q.appendleft((node + 1, depth + 1))
    
# print(cnt)