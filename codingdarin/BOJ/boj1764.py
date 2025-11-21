# BOJ 1764. 듣보잡 (D1 / S4)
# https://www.acmicpc.net/problem/1764

'''
문제
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 
듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
'''

# ------------------------------------------ 2회차 풀이

import sys
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

not_heard = set(input() for _ in range(n))
not_seen = set(input() for _ in range(m))

both = sorted(not_heard & not_seen)  # 교집합

print(len(both))
print(*both, sep='\n')



# # ------------------------------------------ 1회차 풀이
# import sys

# input = lambda: sys.stdin.readline().rstrip()

# not_heard, not_seen = map(int, input().split())

# name_set = set() # 세트

# both = []   # 답 담을 빈 리스트

# # 듣도 못한 사람 다 넣기
# for i in range(not_heard):
#     name = input()
#     name_set.add(name)

# # 세트에 다 넣어보고 안 넣어지는 사람은 중복이므로 정답 리스트에 추가
# for i in range(not_seen):
#     cur = len(name_set)
#     name = input()
#     name_set.add(name)
#     # 세트 길이가 여전하면 리스트에 추가
#     if len(name_set) == cur:
#         both.append(name)

# # 사전 순 정렬
# both.sort()

# print(len(both))
# print(*both, sep='\n')