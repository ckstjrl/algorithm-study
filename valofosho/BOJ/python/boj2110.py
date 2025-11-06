"""
문제
도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

입력
첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

출력
첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

로직 정의
1. 문제를 돌이켜 생각한다. 
기존 문제: 어디에 공유기를 설치해야 가장 인접한 두 공유기 사이의 거리를 최대로 할 수 있는가
-> 거리가 d일 때 몇 개의 공유기를 설치할 수 있는가?

2. 거리 d의 초기값은 start + end // 2 -> 중간값으로 시작
만약 거리 d로 주어진 개수를 못한다면 d를 줄인다
반대로 거리 d로 주어진 개수를 넘긴다면 d를 높인다

3. start+end //2 를 기반으로 이분 탐색 방법을 활용
1. mid = (start + end) // 2
if mid -> cnt >= c -> start = mid 




"""
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))
houses.sort()
# 시작점을 houses[0]으로 하지 않는 이유
# -> 거리의 최소 값을 찾는 것이기 때문에 
start, end = 1, houses[-1] - houses[0]
answer = 0
while start <= end:
    mid = (start + end) // 2
    cur = houses[0]
    cnt = 1
    for i in range(1, N):
        # 현재 집이 다음 집과 mid 이상 거리 차이가 난다면 설치
        if houses[i] - cur >= mid:
            cnt += 1
            cur = houses[i]
    if cnt >= C:
        start = mid+1
        answer = mid
    else:
        end = mid-1
print(answer)


