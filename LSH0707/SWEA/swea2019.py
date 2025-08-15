N = int(input())
arr = []
for i in range(N + 1):
    arr.append(2 ** i)  # 2^0 ~ 2^N까지 출력
 
print(*arr)