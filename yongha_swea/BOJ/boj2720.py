#BOJ2720 세탁소 사장 동혁

# 동전 단위: 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)

#받는 동전은 최소화, 예시 거스름돈 형식: 124 -> $ 1.24

T = int(input())

for tc in range(T):
    coin = ['0', '0', '0', '0']

    change = int(input())

    #quarter 동전 수
    if (change // 25) > 0:
        coin[0] = str(change // 25)
        change = change - (25 * (int(coin[0])))

    #dime 동전 수
    if (change // 10) > 0:
        coin[1] = str(change // 10)
        change = change - (10 * (int(coin[1])))

    #nickel 동전 수
    if (change // 5) > 0:
        coin[2] = str(change // 5)
        change = change - (5 * (int(coin[2])))

    # penny 동전 수
    if (change // 1) > 0:
        coin[3] = str(change // 1)
        change = change - (1 * (int(coin[3])))

    ans = ' '.join(coin)
    print(ans)