# BOJ1924 2007년

# 월에 따른 일 수 추가
month = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31,
}

# 7로 나눴을때 나머지를 기준으로 요일 배정
week = {
    1 : 'MON',
    2 : 'TUE',
    3 : 'WED',
    4 : 'THU',
    5 : 'FRI',
    6 : 'SAT',
    7 : 'SUN',
}

# 월/일 정보를 기준으로 일수를 받을 var
days = 0

# 월/일 정보 받기
mon, day = map(int, input().split())

# 받은 달의 이전까지 달의 요일을 일수에 더해주기
for i in range(1, mon):
    days += month[i]

# 받은 달의 흐른 일 만큼 일수에 더해주기
days += day

# 7의 나머지를 통해서 요일 정해주기, 7로 나눠떨어지는 경우 일요일
rest = days % 7
if rest == 0:
    rest = 7

# 요일 출력
print(week[rest])