N = int(input())  # 목표 채널
M = int(input())  # 고장 버튼 갯수
xuse = set()  # 고장 버튼 집합
if M > 0:
    arr = list(map(int, input().split()))
    for x in arr:
        xuse.add(str(x))

min_value = abs(N - 100)  # (+,-) 버튼만 사용한 초기값
for i in range(0, 1000000):  # 0 ~ 999999 모든 수
    x = str(i)
    ok = True
    for j in x:  # 숫자에 고장 버튼 있으면 break
        if j in xuse:
            ok = False
            break
    if ok:  # 고장 버튼 아닌 수로만 이루어진 경우
        cnt = len(x) + abs(N - i)  # 최솟값 기록
        if cnt < min_value:
            min_value = cnt
print(min_value)