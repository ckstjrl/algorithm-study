# 금액이 높은 돈을 우선적으로 계산
# N : 손님에게 거슬러 주어야할 금액 N / 10 <= N <= 1000000
# 각 종류의 돈이 몇개씩 필요한지

# T : 테스트 케이스

T = int(input())

money_type = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, T+1):
    N = int(input())

    arr = []
    for i in range(len(money_type)):
        arr.append(str(N // money_type[i]))
        N = N % money_type[i]


    print(f'#{tc}')
    print(' '.join(arr))



