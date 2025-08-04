T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(str, input())) #[54555555]
    year = int(''.join(arr[0:4]))
    month = int(''.join(arr[4:6]))
    day = int(''.join(arr[6:8]))
    year_s = ''.join(arr[0:4])
    month_s = ''.join(arr[4:6])
    day_s = ''.join(arr[6:8])
    if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
        print(f'#{test_case} {year_s}/{month_s}/{day_s}')
    elif month in [4, 6, 9, 11] and 1 <= day <= 30:
        print(f'#{test_case} {year_s}/{month_s}/{day_s}')
    elif month == 2 and 1 <= day <= 28:
        print(f'#{test_case} {year_s}/{month_s}/{day_s}')
    else:
        print(f'#{test_case} -1')