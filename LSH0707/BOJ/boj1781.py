import sys
input = sys.stdin.readline
import heapq
N = int(input())
arr = [[] for _ in range(N+1)]

for _ in range(N):
    time, x = map(int, input().split())
    arr[time].append(x)  # arr[데드라인] => 같은 데드라인을 갖는 문제의 컵라면 수 리스트

ans = 0
hq = []

for i in range(N, 0, -1):  # 시간 거꾸로 순회
    for x in arr[i]:  # 해당 시간에 풀 수 있는 문제 컵라면 갯수 heappush(최대힙)
        heapq.heappush(hq, -x)
    if hq:  # 풀 수 있는 문제가 있다면 heappop => ans에 기록
        ans = ans + -(heapq.heappop(hq))
        
print(ans)