# sum /D3
for tc in range(10): # 10개의 case를 input으로 받아야 함
    T = int(input()) # test case number
    arr = [list(map(int, input().split())) for _ in range(100)] # 100 X 100 행렬 받기
    sum_list = [] # 행, 열, 대각의 합 담는 list
    row_sum_lst = [] # 행의 합 list
    col_sum_lst = [] # 열의 합 list
    cross_sum_lst = [] # 대각의 합 list
    for i in range(100): 
        row_sum = 0
        col_sum = 0
        for j in range(100):      # 행과 열은 같은 반복을 사용하면서 i, j 위치만 변경해줄 수 있음
            row_sum += arr[i][j]  # 행의 합 구하기
            col_sum += arr[j][i]  # 열의 합 구하기
        row_sum_lst.append(row_sum) # 행의 합 리스트 담기
        col_sum_lst.append(col_sum) #열의 합 리스트 담기
    cross_sum1 = arr[0][0] # 좌상 -> 우하 대각의 합 구하기 [0][0] 시작 [99][99] 끝
    for c in range(1, 100):
        cross_sum1 += arr[c][c]
    cross_sum_lst.append(cross_sum1)
    cross_sum2 = arr[0][99] # 우상 -> 좌하 대각의 합 구하기 [0][99] 시작 [99][0] 끝
    for s in range(1, 100):
        cross_sum2 += arr[s][99-s]
    cross_sum_lst.append(cross_sum2)

    sum_list = cross_sum_lst + row_sum_lst + col_sum_lst # list 합

    # 최대값 구하기 
    max_v = 0
    for m in sum_list:
        if max_v < m:
            max_v = m

    print(f'#{T} {max_v}')