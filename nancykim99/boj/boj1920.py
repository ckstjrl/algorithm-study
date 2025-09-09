# BOJ1920. 수 찾기

import sys

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
M = int(input())
arr_num = list(map(int, sys.stdin.readline().split()))
arr.sort()

# 시간 초과로 이분 탐색 재공부 후 진행
# for i in range(M):
#     if arr_num[i] in arr:
#         print(1)
#     else:
#         print(0)

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1

        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return 0

for num in arr_num:
    print(binary_search(num, arr))