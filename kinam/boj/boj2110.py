'''boj2110 - 공유기 설치
도현이의 집 N개가 수직선 위에 있다. 
각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 
최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 
한 집에는 공유기를 하나만 설치할 수 있고, 
가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 
가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
'''
# 정렬해서 처음과 끝 거리가 최대 거리..
# 정렬한 김에 이진탐색 해보기 

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()

l = 1
r = houses[-1] - houses[0] # 최대 거리

ans = 0

while l <= r:
    mid = (l + r) // 2

    cnt = 1 # 처음 하나는 설치
    last = houses[0] # 설치한 곳

    for i in range(1, N): # 집들 순회
        if houses[i] - last >= mid: # 두 집 사이의 거리가 
            cnt += 1
            last = houses[i]
    
    if cnt >= C: # C개 이상 설치해버리면 l 늘림
        ans = mid
        l = mid + 1

    else: # C개만큼 설치 못하면 r 줄임
        r = mid - 1

print(ans)