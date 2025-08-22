T = int(input())

for test_case in range(1, T+1):

    N = int(input())

    pascal = []  # 파스칼 삼각형을 저장할 리스트

    for i in range(N):
        
        # 각 행은 i+1개의 요소를 가짐 (삼각형 형태)
        row = [0] * (i + 1)
        row[0] = 1  # 첫 번째 값
        row[-1] = 1  # 마지막 값

        # 중간 값 계산
        for j in range(1, i):
            row[j] = pascal[i-1][j-1] + pascal[i-1][j]

        pascal.append(row)  # 계산된 행을 추가

    # 출력
    print(f'#{test_case}')
    for row in pascal:
        print(' '.join(map(str, row)))
