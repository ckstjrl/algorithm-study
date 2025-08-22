T = int(input())
for test_case in range(1, 1+T):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]  # 단위가 큰 돈부터 처리
    charge = []
    for i in money:
        a = N//i  # 필요한 화폐 개수
        charge.append(a)
        N = N - a * i  # 처리하고 남은 돈
    print(f'#{test_case}')
    print(*charge)