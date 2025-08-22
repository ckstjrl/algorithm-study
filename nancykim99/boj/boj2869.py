# 2869. 달팽이는 올라가고 싶다 D2
# 땅 위에 달팽이가 있다. 이 달팽이는 높이가 V미터인 나무 막대를 올라갈 것이다.
# 달팽이는 낮에 A미터 올라갈 수 있다. 하지만, 밤에 잠을 자는 동안 B미터 미끄러진다. 또, 정상에 올라간 후에는 미끄러지지 않는다.
# 달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸리는지 구하는 프로그램을 작성하시오.
# [입력]
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)
# [출력]
# 첫째 줄에 달팽이가 나무 막대를 모두 올라가는데 며칠이 걸리는지 출력한다.

# math.ceil() : 반올림

# 시간 초과
# A, B, V = map(int, input().split())
#
# snail = 0
# has_arrived = False
# cnt = 0
# while not has_arrived :
#     if snail >= V:
#         has_arrived = True
#         break
#     else:
#         snail += A
#         if snail >= V:
#             has_arrived = True
#             cnt += 1
#             break
#         else:
#             snail -= B
#             cnt += 1
#
# print(cnt)

###
import math
A, B, V = map(int, input().split())

if A >= V:
    print(1)
else:
    ans = math.ceil((V-A) / (A-B)) + 1 # 마지막 날을 빼고 ceil로 무조건 반올림 (올라갔기 때문)
    print(ans)









