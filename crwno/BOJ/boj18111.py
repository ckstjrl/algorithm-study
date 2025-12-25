N, M, B = map(int, input().split())
gr = [list(map(int, input().split())) for _ in range(N)]

height = [0] * 257
for i in range(N):
    for j in range(M):
        height[gr[i][j]] += 1

tm = float('inf')
mx_height = 0

for h in range(257):
    remove = 0
    add = 0

    for i in range(257):
        if i > h:
            remove += (i - h) * height[i]
        else:
            add += (h - i) * height[i]

    if B + remove >= add:
        time = remove * 2 + add
        if time < tm or (time == tm and h > mx_height):
            tm = time
            mx_height = h

print(tm, mx_height)











# N, M, B = map(int, input().split())
# gr = [[] for _ in range(N)]
# for i in range(N):
#     gr[i] = list(map(int, input().split()))
# # 제거 2초, 추가 1초
# mn = float('inf')
# mx = -float('inf')
#
# for i in range(N):
#     for j in range(M):
#         if mx < gr[i][j]:
#             mx = gr[i][j]
#         elif mn > gr[i][j]:
#             mn = gr[i][j]
# tm = 0
# mn_cnt = 0
# for i in range(N):
#     for j in range(M):
#         if mn == gr[i][j]:
#             mn_cnt += 1

# while 안에 for문 두개는 안되네네
# while mn_cnt < (2 * N * M) // 3 and B >= mn_cnt:
#     mn += 1
#     tm += mn_cnt
#     B -= mn_cnt
#     mn_cnt = 0
#     for i in range(N):
#         for j in range(M):
#             if mn == gr[i][j]:
#                 mn_cnt += 1
#
# for i in range(N):
#     for j in range(M):
#         if mn < gr[i][j]:
#             tm += 2 * (gr[i][j] - mn)
#             B += 1
# print(tm, mn)

# N, M, B = map(int, input().split())
# gr = [[] for _ in range(N)]
# for i in range(N):
#     gr[i] = list(map(int, input().split()))
# mn = 501
# mx = -1
#
# height = [0] * 257
# for i in range(N):
#     for j in range(M):
#         height[gr[i][j]] += 1
#         if mx < gr[i][j]:
#             mx = gr[i][j]
#         if mn > gr[i][j]:
#             mn = gr[i][j]
#
# tm = 0
# mn_cnt = height[mn]
#
# while mn_cnt < (2 * N * M) / 3:
#     height[mn] -= mn_cnt
#     mn += 1
#     height[mn] += mn_cnt
#     tm += mn_cnt
#     B -= mn_cnt
#     mn_cnt = height[mn]
#
#
# for i in range(N):
#     for j in range(M):
#         if mn < gr[i][j]:
#             tm += 2 * (gr[i][j] - mn)
#             B += (gr[i][j] - mn)
#             height[gr[i][j]] -= 1
#             height[mn] += 1
# if B < 0:
#     while B < 0:
#         B += N * M
#         mn -= 1
#     tm = 0
#     for i in range(N):
#         for j in range(M):
#             if gr[i][j] > mn:
#                 tm += 2 * (gr[i][j] - mn)
#             else:
#                 tm += (mn - gr[i][j])
#
# print(tm, mn)

# 블록 모라잘때 생각 안함
# N, M, B = map(int, input().split())
# gr = [list(map(int, input().split())) for _ in range(N)]
#
# height = [0] * 257
# s = 0
# for i in range(N):
#     for j in range(M):
#         height[gr[i][j]] += 1
#         s += gr[i][j]
#
# if s % (N * M) == 0:
#     mx_height = s // (N * M)
# elif s % (N * M) != 0 and s % (N * M) < (N * M) / 3:
#     mx_height = s // (N * M)
# else:
#     mx_height = s // (N * M) + 1
#
# need_B = 0
# tm = 0
# for i in range(N):
#     for j in range(M):
#         if gr[i][j] < mx_height:
#             need_B += mx_height - gr[i][j]
#             tm += mx_height - gr[i][j]
#         elif gr[i][j] > mx_height:
#             need_B -= gr[i][j] - mx_height
#             tm += 2 * (gr[i][j] - mx_height)
# print(need_B)
# print(tm, mx_height)

# N, M, B = map(int, input().split())
# gr = [list(map(int, input().split())) for _ in range(N)]
#
# height = [0] * 257
# s = 0
# for i in range(N):
#     for j in range(M):
#         height[gr[i][j]] += 1
#         s += gr[i][j]

# if s % (N * M) == 0:
#     mx_height = s // (N * M)
# 1/3 이상이면 1층추가 아니면 1층제거 <- 요게틀리네네# else:
#     if s % (N * M) >= (N * M) / 3 and (N * M) - (s % (N * M)) <= B:
#         mx_height = s // (N * M) + 1
#     else:
#         mx_height = s // (N * M)
#
# tm = 0
# for i in range(N):
#     for j in range(M):
#         if gr[i][j] < mx_height:
#             tm += mx_height - gr[i][j]
#         elif gr[i][j] > mx_height:
#             tm += 2 * (gr[i][j] - mx_height)
#
# print(tm, mx_height)
