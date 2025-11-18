#BOJ2493 D2 탑

from collections import deque

towers = int(input())

arr = list(map(int, input().split()))

receive = [0] * len(arr)

#stack을 사용
stack = []

for i in range(len(arr)):
    # i 번째 타워의 높이, 현재 타워
    tower = arr[i]

    # stack 안에 들어있는 탑의 높이가 현재 탑 높이보다 낮은 경우 해당 탑이 시그널을 받을 가능성은 없기 때문에 pop
    while stack and arr[stack[-1]] < tower:
        stack.pop()

    # 가장 최근에 스택에 들어가 타워의 인덱스 넘버를 받기 위해 index 정보 + 1(타워가 1부터 시작하니까)
    if stack:
        receive[i] = stack[-1] + 1

    # 마지막에 stack에 현재 탑의 값을 넣어주기
    stack.append(i)

print(' '.join(map(str, receive)))

# # 시간초과
# towers = int(input())
#
# arr = list(map(int, input().split()))
#
# receive = [0] * len(arr)
#
# #레이저를 발사하는 탑
# for i in range(len(arr)):
#     #레이저가 지나가는 타워의 위치기 때문에 레이저를 쏜 탑의 하나 왼쪽부터 시작
#     for j in range(i -1, -1, -1):
#         #높이가 같거나 더 높은 경우
#         if arr[i] <= arr[j]:
#             #레이저 수신 위치 갱신
#             receive[i] = j + 1
#             #하나의 타워만 수신 가능하기 때문에 break
#             break
#
# print(' '.join(map(str, receive)))

