N = int(input())
weight = []
height = []
for i in range(N):
    w, h = map(int, input().split())
    weight.append(w)
    height.append(h)

ans = [0] * N
cnt = 0
for i in range(N):
    for j in range(N):
        if weight[i] < weight[j] and height[i] < height[j]:
            cnt += 1
    ans[i] = cnt + 1
    cnt = 0

for i in range(N):
    print(ans[i], end=' ')