T = int(input())
MONTH = [['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'], ['31', '28', '31', '30', '31', '30', '31', '31', '30', '31', '30', '31']]
for test_case in range(1, T + 1):
    N = input()
     
    if N[4:6] not in MONTH[0]:
        print(f'#{test_case} -1')
    else:
        for i in range(12):
            if N[4:6] == MONTH[0][i]:
                month = i
        if 0 < int(N[6:]) and int(N[6:]) <= int(MONTH[1][month]):
            print(f"#{test_case} {N[:4]}/{N[4:6]}/{N[6:]}")
        else:
            print(f'#{test_case} -1')