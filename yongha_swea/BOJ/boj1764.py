# BOJ1764 듣보잡

N, M = map(int, input().split())

# 기존 리스트에서 set으로 변경을 통해서 속도 향상, 추가로 중복 방지
not_see = set()

not_hear = set()

not_see_hear = set()

count = 0

for _ in range(N):
    not_see.add(input())

for _ in range(M):
    not_hear.add(input())

# 시간초과의 원인이 되는 연산, in을 하다보니 시간 효율이 많이 떨어진다
# if len(not_see) >= len(not_hear):
#     for i in not_see:
#         if i in not_see and i in not_hear:
#             not_see_hear.append(i)
#             count += 1
# else:
#     for i in not_hear:
#         if i in not_hear and i in not_see:
#             not_see_hear.append(i)
#             count += 1
# print(count)

# sorted를 통해서 교집합 연산으로 불필요한 부분을 날리고 새로운 리스트로 제작
not_see_hear = sorted(not_see & not_hear)

print(len(not_see_hear))
for i in not_see_hear:
    print(i)