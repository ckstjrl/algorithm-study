# boj 1924. 2007년 (D1, B1)

import sys
input = lambda: sys.stdin.readline().rstrip()

x, y = map(int, input().split())
days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

# 해당 일자의 총 일수 계산
total_days = sum(days_of_month[:x-1]) + y
day_of_week = week[total_days % 7 - 1]

print(day_of_week)
