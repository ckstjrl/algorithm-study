month, day = map(int, input().split())

cnt = 0
days_num = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_str = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
for i in range(month - 1):
    cnt += days_num[i]
cnt += day

ans = cnt % 7
print(days_str[ans])