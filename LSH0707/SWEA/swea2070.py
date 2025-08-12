T = int(input())
for test_case in range(1, T + 1):
    AB = list(map(int, input().split()))
    A = AB[0]
    B = AB[1]
    if A > B:
        print(f'#{test_case} >')
    elif A == B:
        print(f'#{test_case} =')
    else:
        print(f'#{test_case} <')