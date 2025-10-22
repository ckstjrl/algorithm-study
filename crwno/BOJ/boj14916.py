n = int(input())
k = n // 5
while True:
    if (n - k) % 2 == 0:
        m = (n - 5 * k) // 2
        print(m + k)
        break
    k -= 1
    if k < 0:
        print(-1)
        break