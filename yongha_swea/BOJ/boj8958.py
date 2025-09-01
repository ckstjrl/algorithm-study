T = int(input())

for i in range(T):
    #각 줄마다 계산을 해야하기 때문에 매 loop마다 득점을 계산
    arr = list(map(str, input()))

    total_score = 0
    score = 0
    extra = 0

    for que in arr:
        #정답인 경우에
        if que == 'O':
            extra += 1
            total_score += extra
        #오답인 경우에
        else:
            extra = 0

    print(total_score)