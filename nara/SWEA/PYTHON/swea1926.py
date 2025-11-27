N = int(input()) # 입력받은 수
for i in range(1, N + 1):
    tmp_1 = i # i의 자릿수를 알기 위한 임시변수
    cnt = list() # i의 자릿수 리스트
    count = 0
    while tmp_1 > 0:
        cnt.append(tmp_1 % 10)
        tmp_1 = tmp_1 // 10
    for j in cnt: # 자리 수 확인
        if j != 0 and j % 3 == 0: # 3인 자리가 있으면
            count += 1
    if count == 0: # 3, 6, 9가 들어있지 않은 수인 경우 숫자 그대로 출력
        print(i, end= ' ')
    else: # 3, 6, 9가 들어있는 경우
        for k in range(count): # 3, 6, 9의 수만큼 반복
            if k == count - 1: # -의 마지막 출력인 경우 end=' ' (공백)
                print('-', end=' ')
            else: # 공백 X : -가 이어서 출력될 수 있도록
                print('-', end='')