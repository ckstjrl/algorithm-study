# 1트 - 출력 형식이 잘못되었습니다(?)
# N = int(input())
#
# for i in range(1, N + 1):
#     print(' ' * (N - i), '*' * i)

# 2트 - 틀렸습니다(???)
# N = int(input())
#
# arr = [[] for _ in range(N)]
#
# for i in range(1, N + 1):
#     for j in range(N, 0, -1):
#         if N - i + j <= 5:
#             arr[i - 1].append('*')
#         else:
#             arr[i - 1].append(' ')
#
# for i in range(N):
#     print(''.join(arr[i]))

# 3트, 4트 5가 아니라 N..
N = int(input())

arr = [[] for _ in range(N)]

for i in range(1, N + 1):
    for j in range(N, 0, -1):
        if N - i + j <= N:
            arr[i - 1].append('*')
        else:
            arr[i - 1].append(' ')
res = [0] * N
for i in range(N):
    res[i] = ''.join(arr[i])
for i in range(N):
    print(res[i])

# print(a, b)면 'a b' print(a + b)면 'ab'
# N = int(input())
#
# for i in range(1, N + 1):
#     print(' ' * (N - i) + '*' * i)
# 요렇게쓰면 답처리
