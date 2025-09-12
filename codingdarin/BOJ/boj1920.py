# BOJ 1920. 수 찾기 (D2/S4)
#------------------------------------------------2회차 풀이

n = int(input())
origins = set(map(int, input().split()))  # set으로 저장하면 빠름! 해쉬!
m = int(input())
compares = list(map(int, input().split()))

for each in compares:
    if each in origins:  # O(1) 탐색
        print(1)
    else:
        print(0)

#------------------------------------------------1회차 풀이
# 접근법: 걍... 완탐하면 안되나...?: 안됨
# 이분 탐색

# import sys
# input = sys.stdin.readline

# def binary(arr, one):
#     left, right = 0, len(arr)-1

#     while left <= right:
#         mid = (left+right)//2
#         if one == arr[mid]:
#             return True
#         elif one > arr[mid]:
#             left = mid +1
#         elif one < arr[mid]:
#             right = mid -1
#     return False 


# N = int(input())
# origins = sorted(list(map(int, input().split())))
# M = int(input())
# compares = list(map(int, input().split()))

# for each in compares:
#     if binary(origins, each):
#         print(1)
#     else:
#         print(0)

