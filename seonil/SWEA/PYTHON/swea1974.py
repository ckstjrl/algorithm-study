"""
1974. 스도쿠 검증
"""

# 리스트의 모든 원소가 1인지 확인하는 함수
def is_ones(lst):
    return lst == [1] * 9

T = int(input())

for test_case in range(1, T + 1):
    
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    result = True  # 스도쿠가 정답인지 판단

    # 각 행과 열 검사
    for i in range(9):

        # 각 행과 열마다 숫자 count 리스트를 만들고 0으로 초기화(1~9 => 인덱스 0~8)
        row_check = [0] * 9
        col_check = [0] * 9

        for j in range(9):
            row_num = sudoku[i][j]
            col_num = sudoku[j][i]

            # 유효한 숫자 범위(1~9)에서 숫자 확인하고 리스트에 저장
            if 1 <= row_num <= 9:
                row_check[row_num - 1] += 1
            if 1 <= col_num <= 9:
                col_check[col_num - 1] += 1

        # 중복 숫자가 있거나 빠진 숫자가 있다면 유효하지 않으므로 False 반환 후 loop 탈출
        if not is_ones(row_check) or not is_ones(col_check):
            result = False
            break
    
    # 위를 통과하면 3x3 박스 검사
    if result:

        # 시작 좌표는 (0,0), (0,3),..., (6,6)
        for i in range(0, 9, 3):  
            for j in range(0, 9, 3):
                box_check = [0] * 9  # 박스 count 리스트

                # 3x3 박스 내부에서 유효한 숫자 범위(1~9)에서 숫자 확인하고 리스트에 저장
                for p in range(3):  
                    for q in range(3):
                        num = sudoku[i + p][j + q]
                        if 1 <= num <= 9:
                            box_check[num - 1] += 1

                # 마찬가지로 중복이나 누락된 숫자가 있다면 유효하지 않으므로 False 반환 후 loop 탈출
                if not is_ones(box_check):
                    result = False
                    break 

    # 결과 출력: 유효하면 1, 아니면 0 출력
    print(f'#{test_case} {1 if result else 0}')

