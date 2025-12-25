'''
# [Silver III] 구간 합 구하기 4 - 11659

[문제 링크](https://www.acmicpc.net/problem/11659)

### 성능 요약

메모리: 122480 KB, 시간: 172 ms

### 분류

누적 합

### 제출 일자

2025년 11월 19일 16:28:17

### 문제 설명

<p>수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.</p>

### 입력

 <p>첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.</p>

### 출력

 <p>총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.</p>
'''
# 초기설정
import sys
input = lambda :sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * N
dp[0] = arr[0]

for i in range(1, N):
    dp[i] = dp[i -1] + arr[i]

for _ in range(M):
    S, E = map(int, input().split())
    # 인덱스 맞추기
    S -= 1
    E -= 1
    if S == 0:
        print(dp[E])
    else:
        print(dp[E] - dp[S - 1])