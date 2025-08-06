T = int(input()) # 테스트 케이스


for tc in range(1, T+1):
    v_num = 0
    value_num = 10
    odd_num = []
    list_of_num = list(map(int, input().split()))

    for i in range(value_num): # 10개의 수를 돌면서
        if list_of_num[i] % 2 == 1: # 홀수인 경우
            odd_num += [list_of_num[i]] # odd_num에 리스트 추가
            v_num += 1 # odd_num 값의 수
        else:
            continue

    x = 0
    for i in range(v_num): # odd_num sum
        x += odd_num[i] # x에 odd_num 추가
    
    print(f'#{tc}', x)

# 항상 헷갈리는 거 : 어디에 빈 리스트, 0 등을 위치해야할지 고민된다.
# 틀린 거: 빈칸이 있다고 `print(f'#{tc} ', x)`에서 {} 뒤에 빈칸 넣어서 fail 나옴