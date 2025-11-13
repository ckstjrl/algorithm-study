# BOJ 2075. N번째 큰 수 / D2
'''
N×N의 표에 수 N2개 채워져 있다. 채워진 수에는 한 가지 특징이 있는데, 모든 수는 자신의 한 칸 위에 있는 수보다 크다는 것이다.
N=5일 때의 예를 보자.

12	7	9	15	5
13	8	11	19	6
21	10	26	31	16
48	14	28	35	25
52	20	32	41	49
이러한 표가 주어졌을 때, N번째 큰 수를 찾는 프로그램을 작성하시오. 표에 채워진 수는 모두 다르다.

입력
첫째 줄에 N(1 ≤ N ≤ 1,500)이 주어진다. 다음 N개의 줄에는 각 줄마다 N개의 수가 주어진다.
표에 적힌 수는 -10억보다 크거나 같고, 10억보다 작거나 같은 정수이다.

출력
첫째 줄에 N번째 큰 수를 출력한다.
'''
import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
arr = []

for _ in range(N):
    for a in map(int, input().split()):
        if len(arr) < N:
            heapq.heappush(arr, a)

        else:
            if a > arr[0]:
                heapq.heappop(arr)
                heapq.heappush(arr, a)
print(arr[0])

# 메모리 초과
'''
left = []
right = []
for _ in range(N):
    for a in map(int, input().split()):
        heapq.heappush(left, -a)

        if right and -left[0] > right[0]:
            max_left = -heapq.heappop(left)
            min_right = heapq.heappop(right)
            heapq.heappush(left, -min_right)
            heapq.heappush(right, max_left)

        if len(left) > (N**2-N):
            max_left = -heapq.heappop(left)
            heapq.heappush(right, max_left)

print(heapq.heappop(right))
'''

'''
우선순위 큐 사용
숫자들을 받아서 arr에 N개까지 채워넣고
그 이후부터는 제일 작은 수와 a를 비교하고
a가 더 큰 경우
교환하는 방식으로 진행
다 확인한 후 arr에서 가장 작은 수를 뽑으면 그게 N번째로 큰 숫자
'''
