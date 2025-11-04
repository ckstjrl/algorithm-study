#첫 항의 값, 공차(첫 항과 둘째 항의 값의 차), 위치를 찾아야 하는 수
a, d, k = map(int, input().split())

num = a

count = 1

#다음 항으로 갈수록 값이 커지는 경우
if d >= 0:
    while num < k:
        count += 1
        num += d
#다음 항으로 갈수록 값이 작아지는 경우
elif d < 0:
    while num > k:
        count += 1
        num += d

#공차를 일정 횟수 반복하였을때 값이 일치하는 경우 반복횟수를 출력
if num == k:
    print(count)

#일치하지 않는 경우 X출력
if num != k:
    print('X')