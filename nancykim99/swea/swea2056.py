# 2056. 연월일 달력 D1
# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
# ”YYYY/MM/DD”형식으로 출력하고,
# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
# 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
# 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
# ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)
#
# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
#
# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

T = int(input()) # 테스트 케이스

for tc in range(1, T+1):
    N = str(input())

    result = 0
    year = N[0:4]
    month = N[4:6]
    day = N[6:]
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    month_30 = [4, 6, 9, 11]
    if int(month) > 12 or int(month) < 1:
        result = -1
    else:
        if int(month) in month_31:
            if int(day) > 31:
                result = -1
        if int(month) in month_30:
            if int(day) > 30:
                result = -1
        if int(month) == 2:
            if int(day) > 28:
                result = -1

    if result != -1:
        result = f'{year}/{month}/{day}'
    else:
        result = -1

    print(f'#{tc}', result)

# 시행착오 1 : month, day가 비교연산을 하기 위해서는 int로 바꿔야 함. 그러나 답은 str이여야 함.