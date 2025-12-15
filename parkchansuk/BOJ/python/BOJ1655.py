# BOJ 1655. 가운데를 말해요 / D3
'''
문제
백준이는 동생에게 "가운데를 말해요" 게임을 가르쳐주고 있다.
백준이가 정수를 하나씩 외칠때마다 동생은 지금까지 백준이가 말한 수 중에서 중간값을 말해야 한다.
만약, 그동안 백준이가 외친 수의 개수가 짝수개라면 중간에 있는 두 수 중에서 작은 수를 말해야 한다.

예를 들어 백준이가 동생에게 1, 5, 2, 10, -99, 7, 5를 순서대로 외쳤다고 하면,
동생은 1, 1, 2, 2, 2, 2, 5를 차례대로 말해야 한다.
백준이가 외치는 수가 주어졌을 때, 동생이 말해야 하는 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에는 백준이가 외치는 정수의 개수 N이 주어진다.
N은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수이다.
그 다음 N줄에 걸쳐서 백준이가 외치는 정수가 차례대로 주어진다.
정수는 -10,000보다 크거나 같고, 10,000보다 작거나 같다.

출력
한 줄에 하나씩 N줄에 걸쳐 백준이의 동생이 말해야 하는 수를 순서대로 출력한다.
'''
import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())

left = [] # 작은 값 저장, 음수로 저장해서 -heapq.heappop(left) 출력하면 최댓값 나옴
right = [] # 큰 값 저장

for _ in range(N):
    a = int(input().strip())
    heapq.heappush(left, -a) # 일단 작은 쪽에 넣음

    if right and -left[0] > right[0]: # 오른쪽 작은 값이 왼쪽 큰 값보다 작을 때 교환
        max_left = -heapq.heappop(left)
        min_right = heapq.heappop(right)
        heapq.heappush(left, -min_right)
        heapq.heappush(right, max_left)

    if len(left) > len(right) + 1: # 왼쪽이 오른쪽보다 한개 초과로 많은 경우 왼쪽의 큰 값을 오른쪽으로 옮김
        max_left = -heapq.heappop(left)
        heapq.heappush(right, max_left)

    print(-left[0]) # 왼쪽에서 제일 큰 값을 뽑으면 중간값
    



# N번 sort 진행해서 시간 초과
'''
import sys
input = sys.stdin.readline

N = int(input().strip())
num_arr = []
mid_num = []
for _ in range(N):
    a = int(input().strip())
    num_arr.append(a)


    num_arr.sort()

    if len(num_arr) % 2 == 1:
        i = len(num_arr) // 2
        mid_num.append(num_arr[i])
    else:
        i = len(num_arr) // 2 - 1
        mid_num.append(num_arr[i])

print('\n'.join(map(str, mid_num)))
'''

'''
숫자를 하나씩 저장하면서 리스트를 정렬해서 가운데 값을 뽑는 과정은 시간초과 발생
우선순위 큐 방식 활용
이전에 풀었던 커서 같은 문제와 유사
left는 작은 수
right는 큰 수 리스트로 하고
left로 일단 숫자 받고
right 최솟값과 left 최댓값 비교하고 만약 left 최댓값이 더 크다면 right 최솟값과 교환
left는 항상 right보다 한개 많은 숫자가 들어있거나 같은 양의 숫자가 들어있게 함.
'''
