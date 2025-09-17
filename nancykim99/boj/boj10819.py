'''
BOJ10819. 차이를 최대로
N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
[입력]
첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.
[출력]
첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

해결 방법 : 완전 탐색으로 배열을 순열으로 돌고, 순열이 완성되면, 식의 결과를 받고, 그 결과를 최댓값과 비교하는 방식으로 해결
궁금증 1. 가지치기를 해서 재귀를 조금 덜 돌게 할 수 있을까? 근데 최솟값이 아니라서, 어떻게 가지치기를 해야할지 모르겠음.
작다고 continue 하기엔, 작으면 숫자를 더하면 바뀔테고, 크다고 continue하기엔, 최댓값이라 클때 그냥 가는게 맞고...
'''

import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

visited = [0] * (N+1)
curr_perm = []
max_sum = 0
# 완전 탐색
def recur(i):
    global curr_perm, max_sum
    # 1. 종료조건 : 만약 숫자를 다 더 했을 경우
    if i == N:
        curr_sum = 0
        for k in range(N-1):
            num_d = abs(curr_perm[k] - curr_perm[k+1])
            curr_sum += num_d
        max_sum = max(curr_sum, max_sum)
        return max_sum
    # 2. 가지의 수 : 수의 순서 -> 순열 구해서 식의 최댓값을 구하고, max_sum과 비교해서 max(current_sum, max_sum)을 구하기
    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = 1
                curr_perm.append(arr[j])
                recur(i+1)
                # 3. 백트래킹
                curr_perm.pop()
                visited[j] = 0
recur(0)
print(max_sum)