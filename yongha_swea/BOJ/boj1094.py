# BOJ1094 막대기

target = int(input())

stick = 64

count = 0

# 문제가 길어서 좀 이해가 한번에 안 되지만 결국 한 줄 요약하면: 
# '64를 반씩 줄여가며 몇 조각을 붙여야 목표 길이가 되느냐' -> 32 -> 16 -> 8 -> 4 -> 2 -> 1
while target > 0:
    if target >= stick:
        #사용 조각의 수를 1늘리고, 그 조각 길이 만큼 목표에서 빼기
        count += 1
        target = target - stick
    else:
        #target이 0이 되었다는건 목표를 도달했다는 의미
        if target == 0:
            break
        #목표가 도달되지 않았다면 다시금 막대를 반토막 내기 (//2)
        else:
            stick = (stick // 2)
#목표를 도달한 시점에서의 count수, 사용한 조각의 수, 를 출력
print(count)