'''boj2473 - 세 용액
KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다. 
각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다.  
산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고, 
알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.

같은 양의 세 가지 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다. 
이 연구소에서는 같은 양의 세 가지 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다. 

예를 들어, 주어진 용액들의 특성값이 [-2, 6, -97, -6, 98]인 경우에는 
특성값이 -97와 -2인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 
이 용액이 특성값이 0에 가장 가까운 용액이다. 
참고로, 세 종류의 알칼리성 용액만으로나 혹은 세 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.

산성 용액과 알칼리성 용액이 주어졌을 때, 이 중 같은 양의 세 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 세 용액을 찾는 프로그램을 작성하시오.
'''
# 3중 for문이라 너무 오래걸림

# import sys
# input = sys.stdin.readline

# N = int(input().strip())
# liquid = list(map(int, input().split()))

# min_liq = float('inf')
# ans_list = []


# for i in range(N-2):
#     for j in range(i+1, N-1):
#         for k in range(j+1, N):
#             min_liq = min(min_liq, abs(0 - (liquid[i] + liquid[j] + liquid[k])))
#             if min_liq == abs(0 - (liquid[i] + liquid[j] + liquid[k])):
#                 ans_list.append([liquid[i], liquid[j], liquid[k]])

# ans = ans_list.pop()
# ans.sort()
# print(*ans)

#############################################################

import sys
input = sys.stdin.readline

N = int(input().strip())
liquid = list(map(int, input().split()))
liquid.sort()

min_sum = float('inf')
ans_list = []


# 첫 번째 수 고정하고 양쪽 수 하나씩 좁혀나가기
for i in range(N-2):
    l = i + 1
    r = N - 1

    while l < r:
        current_sum = liquid[i] + liquid[l] + liquid[r]

        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            ans_list = [liquid[i], liquid[l], liquid[r]]

        # 합이 0보다 작으면? 더 큰 값을 더해야하므로, left 증가시키기
        if current_sum < 0:
            l += 1

        # 합이 0보다 크면, 작은 값이 필요. right 줄이기
        elif current_sum > 0:
            r -= 1

        else:
            print(*ans_list)
            exit()

print(*ans_list)
