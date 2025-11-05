# BOJ11034 캥거루 세마리2

# 몇 번 입력을 받을지 모르기 때문에 try-except 사용
while True:
    try:
        ans = 0

        # 3마리 캥거루 위치 받기
        kang1, kang2, kang3 = map(int, input().split())

        # 사이로만 이동이 가능하기 때문에 더 큰 간격을 기준으로 하여 들어갈 횟수를 결정하게 된다, 더 큰 간격 -1 = 최대 위치 변경 가능 횟수
        if (kang3 - kang2) > (kang2 - kang1):
            ans = (kang3 - kang2 - 1)
        else:
            ans = (kang2 - kang1 - 1)

        print(ans)

    except:
        break