N, K = map(int, input().split())

cnt = 1
while cnt < N:
    cnt += 1
    K = K // 2
print(K)