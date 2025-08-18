T = int(input())
for test_case in range(1, T+1):
    # N개의 정수, M초의 시간, K개의 붕어빵
    N, M, K = map(int, input().split())
    make = [0] * 11112
    bought = [-1] *11112
    for i in range(1, 11112):
        # 정확히 만든 시간에는 갓 나온 붕어빵
        if i % M == 0:
            make[i] = make[i-1] + K
        # 만들기 전까지도 누적합은 진행
        else:
            make[i] =  make[i-1]
    # 주문이 들어오는건 시간 순이므로 sorted
    arr = sorted(list(map(int, input().split())))
    flag = 'Possible'
    # 손님이 온 시간대에 빵이 있으면
    for b in arr:
        if make[b] > 0:
            make = [x-1 for x in make] # 전체적으로 빵 -1
        else:
            flag = 'Impossible'
            break
    print(f"#{test_case} {flag}")

