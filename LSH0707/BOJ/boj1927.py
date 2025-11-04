import heapq
import sys
input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    i = int(input())
    if i == 0:  # 입력값 0일때
        if arr:  # 배열에 뭐가 있으면 최솟값 출력
            print(heapq.heappop(arr))
        else:  # 없으면 0출력
            print(0)
    else:  # 자연수 힙큐 추가
        heapq.heappush(arr, i)
        