hour, minute, second = map(int, input().split())

cook_time = int(input())

#요리 초
sec_add = cook_time % 60

#요리 분
min_add = cook_time // 60

#요리 시
hour_add = 0

#60분을 넘게 추가하는 경우 추가 시로 60의 몫만큼 추가 및 60의 나머지는 추가분으로 남겨두기
if min_add >= 60:
    hour_add = min_add // 60
    min_add = min_add % 60

#조리 시간 기존시간에 추가
hour = hour + hour_add

minute = minute + min_add

second = second + sec_add

#60초를 넘으면 분 +1 이후 초 -60
if second >= 60:
    minute += 1
    second -= 60

#60분이 넘으면 시 +1 이후 분 -60
if minute >= 60:
    hour += 1
    minute -= 60

#한번에 48시간, 72시간 등이 추가되는 경우를 대비해서 24시간보다 큰 동안이라는 조건 부여
while hour >= 24:
    hour = hour -24

print(f'{hour} {minute} {second}')