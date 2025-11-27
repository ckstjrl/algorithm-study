"""
문제 정의
1. 각 용액에는 용액의 특성을 나타내는 하나의 정수가 존재
2. 산성 용액은 1~1e10 / 알칼리성 용액은 -1~-1e10
3. 같은 양의 세 가지 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 표현
4. 세 용액을 섞어서 가장 0에 가까울 수 있도록!

로직 구상:
우선 sorting을 해서 양쪽 끝에 최저값 - - - 최대값 같은 느낌으로 있는게 좋지 않을까
그리고 양쪽 극단값에서 하나씩 좁혀가면서
left, left+1, right
left, right-1, right
이 두 가지의 경우의 수를 확인하고, 최소값을 갱신해나가면서 하고
만약에 합이 0이 나오면 바로 break
"""

import sys
input = sys.stdin.readline
N = int(input().strip())
arr = list(map(int, input().split()))
arr.sort()
# 1e9 3개 + 1로 최대값 설정
min_ans = 3e9 + 1

# 두 축을 옮기는 투포인터 + 한 점 지정
for i in range(N-2):
    left = i+1
    right = N-1
    while left < right:
        temp = arr[i] + arr[left] + arr[right]
        # 절대값을 통해서 대소 비교
        if abs(temp) < min_ans:
            min_ans = abs(temp)
            answer = [arr[i], arr[left], arr[right]]
        if temp == 0:
            break
        # 이미 정렬이 되어있기 때문에 작으면 left를 크면 right를 옮긴다
        if temp < 0:
            left += 1
        else:
            right -= 1
print(*answer)





























# while left < right-1 and left + 1< right:
#     temp_l = abs(arr[left] + arr[left+1] + arr[right])
#     temp_r = arr[left] + arr[right-1] + arr[right]

#     if temp_l < min_ans:
#         min_ans = temp_l
#         temp_ls = [arr[left], arr[left+1], arr[right]]
#         if temp_l == 0:
#             break
#     if temp_r < min_ans:
#         min_ans = temp_r
#         temp_ls=[arr[left], arr[right-1], arr[right]]
#         if temp_r == 0:
#             break
#     left 

# print(*temp_ls)