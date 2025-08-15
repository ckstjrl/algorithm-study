"""
[1] 0
[1,1] 1
[1,2,1] 2
[1,3,3,1] 3
[1,4,6,4,1] 4

"""
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    total = []
    for i in range(N):
        ls = []
        for j in range(i+1):
            # 좌측 첫번째 값이라면 1로
            if j == 0:
                ls.append(1)
            # 우측 마지막 값이라면 1로
            elif j == i:
                ls.append(1)
            else:
                # 이전 행에서 이전 열과 같은 열의 값을 더해주기
                ls.append(total[i-1][j-1]+ total[i-1][j])
        total.append(ls)
    print(f"#{test_case}")
    for i in range(len(total)):
        for j in range(len(total[i])):
            # 행 내 각각의 값을 한 줄로 출력
            print(total[i][j], end = " ")
        # 한 행이 끝나면 줄 바꿈
        print()    
    """
    간결한 출력 버전
    print(f"#{test_case})
    for row in total:
        print(*row)
    """