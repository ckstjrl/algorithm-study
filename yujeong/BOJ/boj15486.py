# 15486. 퇴사 2

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)    # dp[i]: i일까지 일했을때 최대 이익

for i in range(1, N+1):
    t, p = map(int, input().split())    # 이번 상담에 걸리는 기간, 상담 완료 시 받는 금액
    dp[i] = max(dp[i-1], dp[i])         # 전날까지의 최대이익과 비교해 최댓값으로 갱신
    if i+t-1 <= N:  # 이번 상담 종료일이 N일까지 끝나면 반영
        dp[i+t-1] = max(dp[i+t-1], dp[i-1]+p)   # i+t-1일차까지의 이익

print(dp[N])
