T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    profit_sum = 0  # 판매 이익이 모아지는 곳

    # 1. 가장 큰 수가 있는 인덱스 번호를 알아내기
    # 2. 그 인덱스 번호가 0이 아니라면, 그 때가 팔아야 할 때
    # 3. 그 전까지의 개수 == 총 판매량, 그 전까지의 합 == 총 원가
    # 4. "가격 * 총판매량 - 총원가" 로 계산
    # 5. arr을 판매하고 난 이후의 상황으로 초기화 후 반복
    while len(arr) > 1:
        big_idx = arr.index(max(arr))
        if big_idx != 0:
            profit = arr[big_idx] * big_idx - sum(arr[:big_idx])
            profit_sum += profit
        arr = arr[big_idx + 1:]

    print(f'#{tc} {profit_sum}')
