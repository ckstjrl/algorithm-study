# 시간 초과
# def day(H, N, M, box):
#     global cnt
#     changed = False
#     pos = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
#     for h in range(H):
#         for n in range(N):
#             for m in range(M):
#                 if box[h][n][m] == 1:
#                     for dh, dn, dm in pos:
#                         nh, nn, nm = h + dh, n + dn, m + dm
#                         if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and box[nh][nn][nm] == 0:
#                             box[nh][nn][nm] = 2
#                             changed = True
#     for h in range(H):
#         for n in range(N):
#             for m in range(M):
#                 if box[h][n][m] == 2:
#                     box[h][n][m] = 1
#     cnt += 1
#     return changed
#
# M, N, H = map(int, input().split())
# box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# cnt = 0
# while day(H, N, M, box):
#     pass
#
# for h in range(H):
#     for n in range(N):
#         for m in range(M):
#             if box[h][n][m] == 0:
#                 cnt = 0
#                 break
#
# print(cnt - 1)

from collections import deque

M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
pos = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

q = deque()
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 1:
                q.append((h, n, m))
ans = 0
while q:
    h, n, m = q.popleft()
    for dh, dn, dm in pos:
        nh, nn, nm = h + dh, n + dn, m + dm
        if 0 <= nh < H and 0 <= nn < N and 0 <= nm < M and box[nh][nn][nm] != -1:
            if box[nh][nn][nm] == 0:
                box[nh][nn][nm] = box[h][n][m] + 1
                q.append((nh, nn, nm))

ans = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:
                print(-1)
                exit()
            else:
                ans = max(ans, box[h][n][m])
print(ans - 1)
