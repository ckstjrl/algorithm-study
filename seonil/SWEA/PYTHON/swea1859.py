
def next_maximum_price_day(prices, N, now):
    maximum_price = 0
    max_price_day = now
    for i in range(now, N):
        if prices[i] > maximum_price:
            maximum_price = prices[i]
            max_price_day = i
    return max_price_day

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    sale_prices = list(map(int, input().split()))

    today = 0
    max_profit = 0

    while today < N: # 오늘이  N-1일 때까지 while loop

        # 다음 최대가인 날을 sale_day로 정함
        sale_day = next_maximum_price_day(sale_prices, N, today)

        # 오늘이 최대가라면 팔지 않고 그냥 지나감
        if sale_day == today:
            today += 1

        # 미래에 최대가가 되는 날이 오는 것을 알고 있다면
        else:
            # today부터 sale_day - 1일까지 매수 후 팔기
            for i in range(today, sale_day):
                max_profit += (sale_prices[sale_day] - sale_prices[i])

            # sale_day 이후로 이동
            today = sale_day + 1  

    print(f'#{test_case} {max_profit}')
