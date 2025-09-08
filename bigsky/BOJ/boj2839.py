# BOJ2839: 설탕배달
N = int(input())
cnt = 0
div = N // 5
for i in range(div, -1, -1):
    if (N - (5 * i)) % 3 == 0:
        print(i + ((N - (5 * i)) // 3))
        break
else:
    print(-1)