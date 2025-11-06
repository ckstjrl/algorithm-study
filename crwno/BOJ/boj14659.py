N = int(input())
height = list(map(int, input().split()))

mx_cnt = 0
for i in range(N):
    cnt = 0
    if mx_cnt > N - i - 1:
        break
    for j in range(i + 1, N):
        if height[i] > height[j]:
            cnt += 1
        else:
            break

    mx_cnt = max(mx_cnt, cnt)

print(mx_cnt)

#가지치기..