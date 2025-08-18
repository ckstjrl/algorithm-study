for test_case in range(1, 11):
    N = int(input())
    # + 기호로 연결되어 있으므로 + 를 기준으로 split ^^
    stack = list(map(int,input().split('+')))
    cnt = 0
    # 다 더해주기
    for i in stack:
        cnt += i
    print(f"#{test_case} {cnt}")
