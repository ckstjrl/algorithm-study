# BOJ2810 컵홀더

# 들어온 인원 수
aud = int(input())

# 들어온 좌석 배치도
arr = list(map(str, input().strip()))

# 인원 카운트
count = 0

while arr:

    # 개인석인 경우는 하나의 인원을 제거하고 팝콘통 +1
    if arr[0] == 'S':
        arr.pop(0)
        count += 1
    # 커플석은 두 좌석마다 팝콘통 +1 이기 때문에 두명 제거
    else:
        arr.pop(0)
        arr.pop(0)
        count += 1

# 맨 앞 자리에 있는 팝콘통 +1
count = count + 1

# 인원을 넘겨서 할 수는 없기 때문에 팝콘통이 그 이상이라면 인원 전체가 팝콘통 사용 가능    
if count >= aud:
    print(aud)

# 그게 아니라면 팝콘통 만큼만 사용 가능
else:
    print(count)
