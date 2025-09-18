"""
[문제]
N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

[입력]
첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.

[출력]
첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.
"""
# 20 1 15 8 4 10 -> 62
import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
best = 0

def abs_sum(sequence):
    return sum(abs(sequence[i] - sequence[i+1]) for i in range(len(sequence) - 1))

for perm in permutations(A):
    if abs_sum(perm) >= best:
        best = abs_sum(perm)

print(best)


############## permutations 호출 없이 ################
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

best = 0
used = [False] * N
current = []

def abs_sum(seq):
    return sum(abs(seq[i] - seq[i+1]) for i in range(len(seq) - 1))

def backtrack():
    global best

    if len(current) == N:
        total = abs_sum(current)
        if total > best:
            best = total
        return

    for i in range(N):
        if not used[i]:
            used[i] = True
            current.append(A[i])
            backtrack()
            current.pop()
            used[i] = False

backtrack()
print(best)
