# BOJ14696 딱지놀이

# strength: star(4) > circle(3) >square(2) > triangle(1)

# line 1: round info
T = int(input())

for tc in range(T):

    # line even: A의 딱지 정보 (숫자1: 도형 갯수, 숫자2: 도형 정보)
    A = list(map(str, input().split()))

    A_star = 0
    A_cir = 0
    A_squ = 0
    A_tri = 0

    mark_num_A = A.pop(0)

    for mark in A:
        if mark == '4':
            A_star += 1
        elif mark == '3':
            A_cir += 1
        elif mark == '2':
            A_squ += 1
        else:
            A_tri += 1

    # line ode: B의 딱지 정보 (숫자1: 도형 갯수, 숫자2: 도형 정보)
    B = list(map(str, input().split()))

    B_star = 0
    B_cir = 0
    B_squ = 0
    B_tri = 0

    mark_num_B = B.pop(0)

    for mark in B:
        if mark == '4':
            B_star += 1
        elif mark == '3':
            B_cir += 1
        elif mark == '2':
            B_squ += 1
        else:
            B_tri += 1

    # 문제를 푼 이후 대화를 나누다가 elif를 사용하면 별도로 continue를 칠 필요가 없다는 점을 깨닫았다.
    # 해당 방법을 사용하면 코드 길이를 줄일 수 있을것 같다. 
    if A_star > B_star:
        print('A')
        continue
    if B_star > A_star:
        print('B')
        continue
    if A_cir > B_cir:
        print('A')
        continue
    if B_cir > A_cir:
        print('B')
        continue
    if A_squ > B_squ:
        print('A')
        continue
    if B_squ > A_squ:
        print('B')
        continue
    if A_tri > B_tri:
        print('A')
        continue
    if B_tri > A_tri:
        print('B')
        continue
    if A_star == B_star:
        if A_cir == B_cir:
            if A_squ == B_squ:
                if A_tri == B_tri:
                    print('D')
                    continue