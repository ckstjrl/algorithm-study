N = int(input())
pnt = list(map(int, input().split()))
res = [0] * N

for i in range(N):
    M = int(input())
    route = [[pnt[0], pnt[1]]]

    for j in range(M):
        route.append(list((map(int, input().split()))))
    route.append([pnt[2], pnt[3]])
    dist = 0

    for k in range(M + 1):
        dist += abs(route[k][0] - route[k + 1][0])
        dist += abs(route[k][1] - route[k + 1][1])

    res[i] += dist

mn_d = float('inf')

for i in range(len(res)):
    if mn_d > res[i]:
        mn_d = res[i]
        ans = i

print(ans + 1)