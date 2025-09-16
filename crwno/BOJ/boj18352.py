# GPT 긁음 sys쓰기라니
from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
route = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    route[a].append(b)

v = [-1] * (N + 1)
v[X] = 0
q = deque([X])

while q:
    start = q.popleft()
    for i in route[start]:
        if v[i] == -1:
            v[i] = v[start] + 1
            q.append(i)

res = [i for i in range(1, N + 1) if v[i] == K]
if res:
    res.sort()
    print("\n".join(map(str, res)))
else:
    print(-1)



# from collections import deque
#
# N, M, K, X = map(int, input().split())
# AB = [list(map(int, input().split())) for _ in range(M)]
#
# route = [[] for _ in range(N + 1)]
# for a, b in AB:
#     route[a].append(b)
#
# v = [-1] * (N + 1)
# v[X] = 0
# q = deque()
# q.append(X)
#
# while q:
#     start = q.popleft()
#     for i in route[start]:
#         if v[i] == -1:
#             v[i] = v[start] + 1
#             q.append(i)
# res = []
# for i in range(1, N + 1):
#     if v[i] == K:
#         res.append(i)
# res.sort()
# if len(res) == 0:
#     print(-1)
# else:
#     for i in range(len(res)):
#         print(res[i])