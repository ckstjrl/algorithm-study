# 2056. 연월일 달력

T = int(input())

for tc in range(1, T+1):
    num = str(input())
    result = 0
    year = num[0:4]
    month = num[4:6]
    day = num[6:8]

    for _ in range(len(num)):
        result = year + '/' + month + '/' + day
        if int(month) >= 13:
            result = -1
        elif int(month) == 00:
            result = -1
        elif int(day) > 31:
            result = -1
        elif (int(month) == 4 or int(month) == 6
            or int(month) == 9 or int(month) ==11)\
            and int(day) >=31:
            result = -1
        elif int(month) ==2 and int(day) >= 29:
            result = -1

    print(f'#{tc} {result}')