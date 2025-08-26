# 2161. 카드1

import sys
input = sys.stdin.readline

N = int(input())

q = list(range(1, N+1))     # 숫자 카드 리스트
result = []                 # 버리는 카드 차례로 담을 리스트

for _ in range(N):
    result.append(q.pop(0)) # 맨 위 카드 버리기
    if q:                   # 카드가 남아 있으면
        q.append(q.pop(0))  # 그 다음 카드를 맨 아래로

print(*result)
