import sys
input = sys.stdin.readline
import heapq
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
hq = []
for j in range(N):  # 맨 아랫줄 최대힙 push
    heapq.heappush(hq, (-arr[N-1][j], N-1, j))
ans = None
for _ in range(N):  # N번 pop
    x, i, j = heapq.heappop(hq)
    ans = -x
    if (-arr[i-1][j], i-1, j) not in hq:  # pop한 숫자의 바로 윗 칸 숫자 push
            heapq.heappush(hq, (-arr[i-1][j], i-1, j))
print(ans)
