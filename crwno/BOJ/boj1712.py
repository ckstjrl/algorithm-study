A, B, C = map(int, input().split())

mk = C - B
total = A + 1

if mk <= 0:
    print(-1)
elif total % mk == 0:
    print(total // mk)
elif total % mk != 0:
    print((total // mk) + 1)