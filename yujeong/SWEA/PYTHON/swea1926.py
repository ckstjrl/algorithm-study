# 1926. 간단한 369게임 / D2

N = int(input())
target = ['3', '6', '9']

for number in range(1, N+1):
    cnt_369 = 0
    for t in target:
        # 3, 6, 9가 등장한 횟수를 카운트
        cnt_369 += str(number).count(t)
    
    # 3, 6, 9가 들어가지 않은 수면 그대로 숫자로,
    # 들어간 수면 그 횟수만큼 '-'
    result = number if not cnt_369 else '-'*cnt_369

    print(result, end=' ')