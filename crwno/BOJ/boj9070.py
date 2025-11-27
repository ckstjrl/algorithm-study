T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    price = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    prc = float('inf')
    for i in range(N):
        j = price[i][1] / price[i][0]
        if prc > j:
            prc = j
            ans = price[i][1]
        elif prc == j and ans > price[i][1]:
            prc = j
            ans = price[i][1]

    print(ans)