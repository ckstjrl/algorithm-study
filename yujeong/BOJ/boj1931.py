# 1931. 회의실 배정

import sys
input = sys.stdin.readline 

# 주어진 스케줄에서, 가능한 최대 회의 개수를 찾는 방법은
# 남아있는 스케줄 중 가장 종료시간이 빠른 회의를 우선적으로 택하는 것 

schedules = []
N = int(input())
for _ in range(N):
    start, end = map(int, input().split())
    schedules.append((end, start))          # 종료시간 기준 정렬하기 위해 end를 먼저

schedules.sort()
cnt = 1     # 최소 1개 회의는 무조건 가능하니까 

i = 0
while i < N:
    prev_end = schedules[i][0]
    for j in range(i+1, N):
        if schedules[j][1] >= prev_end:     # 지금 회의 종료시간보다 시작시간이 늦거나 같은 회의면 가능
            cnt += 1
            i = j
            break
    else:
        break

print(cnt)