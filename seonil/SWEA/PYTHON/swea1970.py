"""
1970. 쉬운 거스름돈
"""

T = int(input())

for test_case in range(1, T+1):

    N = int(input())

    # 사용 가능한 화폐 단위 (큰 금액부터 나열)
    money_types = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    
    # money_types.sort(reverse = True)

    # 각 화폐 단위별로 필요한 개수를 저장할 리스트를 만들고 0으로 초기화
    change_counts = [0] * len(money_types)


    for i in range(len(money_types)):

        # 현재 금액이 해당 화폐 단위보다 크거나 같은 경우
        if N >= money_types[i]:
            # 해당 화폐 단위로 몇 장(개) 필요한지 계산
            change_counts[i] = N // money_types[i]
            # 남은 금액 갱신 (나머지 연산)
            N %= money_types[i]

    # 출력 형식에 맞게 결과 출력
    print(f'#{test_case}')
    print(' '.join(map(str, change_counts)))
