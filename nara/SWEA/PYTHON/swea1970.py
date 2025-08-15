T = int(input())
for tc in range(1, T + 1):
    money = {
        50000: 0,
        10000: 0,
        5000: 0,
        1000: 0,
        500: 0,
        100: 0,
        50: 0,
        10: 0
    }
    N = int(input())
    print(f"#{tc}")
    for i in money.keys():
        if N >= i:
            money[i] = N // i
            N = N % i
        print(money[i], end=' ')
    print()
