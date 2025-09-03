# 1트 - 틀림.. while문 바꿈
# a, d, k = map(int, input().split())
# res = -1
# i = 0
# while a + d * i < k:
#     i += 1
#     if a + d * i == k:
#         res = i + 1
#         break
#
# if res == -1:
#     print('X')
# else:
#     print(res)

# 2, 3트 - i = 0일때 생각안해서 고침 근데 틀림(?)
# a, d, k = map(int, input().split())
# res = -1
# i = 0
# while res == -1:
#     if a + d * i == k:
#         res = i + 1
#         break
#     elif a + d * i > k:
#         break
#     i += 1
#
# if res == -1:
#     print('X')
# else:
#     print(res)

# 공차가 -도 있구나
a, d, k = map(int, input().split())
res = -1
i = 0
while res == -1:
    if a + d * i == k:
        res = i + 1
        break
    elif d > 0 and a + d * i > k or d < 0 and a + d * i < k:
        break
    i += 1

if res == -1:
    print('X')
else:
    print(res)