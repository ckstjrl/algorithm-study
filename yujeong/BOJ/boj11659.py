# 11659. 구간 합 구하기 4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())        # 수 개수 M, 합을 구해야 하는 횟수 M
arr = list(map(int, input().split()))   # 수 리스트

pf_sum = [0]*(N+1)      # 수 리스트에서, 앞에서부터 i번째까지 수들을 더한 값 미리 구해놓기
for i in range(1, N+1):
    pf_sum[i] = pf_sum[i-1]+arr[i-1]

for _ in range(M):  # M번 동안 합 구하기
    i, j = map(int, input().split())    # i, j 주어지면 (j >= i)
    print(pf_sum[j] - pf_sum[i-1])      # j까지의 합 - (i-1)까지의 합이 i~j 합 