T = int(input())
for test_case in range(1, T+1):
    a, b = input().split()
    cnt = 0
    while True:
        # b가 a문자열에 있다면
        if b in a:
            # 한번씩만 대치
            a = a.replace(b,'', 1)
            cnt += 1
        else:
            break
    # 대치한 횟수와 남은 문자열의 길이 더해주기
    print(f"#{test_case} {len(a)+ cnt}")