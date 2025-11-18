# 1781. 컵라면

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]   # (데드라인, 받는 컵라면 수)  리스트
arr.sort()      # 데드라인 빠른 순으로 정렬

schedule = []   # 받을 수 있는 컵라면 수들을 저장할 리스트

for x in arr:   # 문제 x의 (데드라인, 컵라면) 에 대해
    heappush(schedule, x[1])    # schedule로 x의 컵라면 push
    if len(schedule) > x[0]:    # schedule의 길이가 일자보다 길다: 일정상 받기 불가능한 컵라면이 포함되었다는 뜻
        heappop(schedule)       # 최대 컵라면 수를 구하기 위해 heappop으로 정리

print(sum(schedule))    # 받을 수 있는 컵라면 개수 합 