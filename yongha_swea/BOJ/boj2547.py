T = int(input())

for tc in range(T):
    #빈 공간 받아주기
    space = input()

    student = 0
    collect = 0
    count = 0
    
    #학생 수를 제공해 주는 첫 줄
    N = int(input())
    
    #학생 수만큼 loop 하여 사탕 수를 더해주고 학생 수 구하기 (N과 동일하기 때문에 사실 불필요)
    for _ in range(N):
        candy = int(input())
        student += 1
        collect += candy
    #나머지 연산을 통해 평등한 분배 가능 여부 결정
    if collect % student == 0:
        print('YES')
    else:
        print('NO')