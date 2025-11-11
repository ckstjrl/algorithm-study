# BOJ 14659. 한조서열정리하고옴ㅋㅋ (D1 / B1)

import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))

# 아 몇 명 쳤는데ㅋㅋ
def attack(n):
    cnt = 0
    start = arr[n]
    for i in range(n+1, N):
        if start >= arr[i]:
            cnt += 1
        else:
            return cnt
    return cnt

max_cnt = 0
# 왼쪽부터 각자 몇 명씩 쳤는데ㅋㅋ
for i in range(N):
    kills = attack(i)
    # 누가 젤 많이 쳤는데ㅋㅋ
    max_cnt = max(kills, max_cnt)
    
    # 왼쪽 애가 이미 전부 다 죽였으면 나머진 더 볼 것도 없음ㅋㅋ
    if kills == N-i-1:
        break

print(max_cnt)