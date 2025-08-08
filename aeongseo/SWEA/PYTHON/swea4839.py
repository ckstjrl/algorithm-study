'''
4839. 이진탐색 (D2)
'''

T = int(input())
 
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
 
    la, ra = 1, P
    lb, rb = 1, P
    cnt_A, cnt_B = 0, 0
 
    while la <= ra:                 # A의 탐색
        ca = int((la + ra) / 2)
 
        if ca == Pa:                # 중간값과 찾는 값이 같으면 종료
            cnt_A += 1
            break
        elif ca > Pa:               # 중간값이 찾는 값보다 크면 오른쪽 값 <- 중간값
            ra = ca
            cnt_A += 1
        else:                       # 중간값이 찾는 값보다 작으면 왼쪽 값 <- 중간값
            la = ca
            cnt_A += 1
 
    while lb <= rb:                 # B의 탐색
        cb = int((lb + rb) / 2)
 
        if cb == Pb:                # 중간값과 찾는 값이 같으면 종료
            cnt_B += 1
            break
        elif cb > Pb:               # 중간값이 찾는 값보다 크면 오른쪽 값 <- 중간값
            rb = cb
            cnt_B += 1
        else:                       # 중간값이 찾는 값보다 작으면 왼쪽 값 <- 중간값
            lb = cb
            cnt_B += 1
 
    # 비교
    if cnt_A < cnt_B:               # A의 탐색 횟수가 B의 탐색 횟수보다 작으면 A 이김
        print(f'#{tc} A')
    elif cnt_A > cnt_B:             # A의 탐색 횟수가 B의 탐색 횟수보다 크면 B 이김
        print(f'#{tc} B')
    else:                           # A의 탐색 횟수와 B의 탐색 횟수가 같으면 비김
        print(f'#{tc} 0')
