"""
BOJ15486 - 퇴사2
문제 정의
1. N일 이후에 퇴사를 결정
2. N일간 최대한 돈을 많이 벌 수 있도록 상담 스케쥴링
3. 1~N일까지 상담 목록, Pi= 상담비용, Wi=상담기간
4. 하나의 상담이 끝나기 전까지는 다른 상담 불가
5. 최대 얼마를 벌 수 있는지 구하라

로직 정의
1. work, pay로 각 기간과 비용을 담는 리스트 선언
2. x 번째 날에는 기간을 넘기지 않는 선에서 반드시 일을 채택, 끝나는 날에 max연산
3. x번째 날 다음 날에도 최대값을 설정하기 위해 오늘의 값과 비교 후 max 연산
    -> 선택한 날과 안한 날 중 더 큰 값을 찾아가게 된다.
4. 마지막 날의 wi가 1인 경우 당일 정산이 가능
-> x <= N 이후 x+wx 의 범위는 N+1까지
"""

# 두 번째 풀이 -> 통과
import sys
input = sys.stdin.readline

N = int(input().strip())
work = [0]
pay = [0]
for _ in range(N):
    w, p = map(int, input().split())
    work.append(w)
    pay.append(p)

dp = [0] * (N+2) # N일까지의 1-based index DP 배열
for x in range(1, N+1): # 마지막 날도 하긴 해요
    wx = work[x]
    px = pay[x]
    if x+1 <= N+1:
        if dp[x+1] < dp[x]:
            dp[x+1] = dp[x]
    if x <= N:
        if x+wx <= N+1:
            temp = dp[x] + pay[x]
            if dp[x+wx] < temp:
                dp[x+wx] = temp
print(dp[N+1])


# 첫 풀이 -> 시간 초과
# import sys
# input = sys.stdin.readline

# N = int(input().strip())
# work = [0]
# pay = [0]
# for _ in range(N):
#     w, p = map(int, input().split())
#     work.append(w)
#     pay.append(p)

# dp = [0] * (N+1) # N일까지의 1-based index DP 배열
# for x in range(1, N+1): # 마지막 날도 하긴 해요
#     wx = work[x]
#     px = pay[x]
#     # 일이 퇴사 후에 끝나면
#     if x+wx >= N+2:
#         continue
#     else:
#         for i in range(x+wx,N+1):
#             dp[i] = max(dp[i],dp[x]+px)
#         dp[x] += px
# print(max(dp))