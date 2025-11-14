'''
BOJ2075 : N번째 큰 수 (S3)

해결 방법 : 한 줄씩 돌아가면서, 힙큐 최소값과 비교하는 방법으로 다섯번째로 작은 숫자 구하기 (n번째로 작은 숫자)
'''

from heapq import heappop, heappush

n = int(input())
num_arr = [list(map(int,input().split())) for _ in range(n)]

temp_que = []

for i in range(n):
    for j in range(n):
        if len(temp_que) < n:
            heappush(temp_que, num_arr[i][j])
        if temp_que[0] < num_arr[i][j]:
            heappop(temp_que)
            heappush(temp_que, num_arr[i][j])

print(temp_que[0])
