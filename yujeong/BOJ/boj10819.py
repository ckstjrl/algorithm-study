# 10819. 차이를 최대로
from itertools import permutations

# |A[0] - A[1]| + ... + |A[N-2] - A[N-1]| 값을 리턴하는 함수 get_sum()
def get_sum(lst):
    sum_v = 0
    for i in range(N-1):
        sum_v += abs(lst[i] - lst[i+1])
    return sum_v


N = int(input())
arr = list(map(int, input().split()))
max_sum = 0

# 배열로 가능한 순열 생성해, 각 경우마다 문제에 주어진 식의 합 구하기 
for p in permutations(arr):
    temp_sum = get_sum(list(p))
    # 기존 최댓값보다 크면 갱신 
    if temp_sum > max_sum:
        max_sum = temp_sum

print(max_sum)
