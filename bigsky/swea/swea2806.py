T = int(input())    # 테스트 케이스 수 입력
for tc in range(1, T + 1):  # 각 테스트 케이스마다 반복
    N = int(input())    # 체스판의 크기 = 퀸의 개수 = N 입력 (N x N)

    count = 0   # 퀸을 올바르게 배치한 경우의 수를 저장할 변수
    used_cols = set()   # 이미 퀸이 놓인 열(세로줄)의 집합
    used_diag1 = set()  # 이미 퀸이 놓인 ↘ 대각선 (row - col)의 집합
    used_diag2 = set()  # 이미 퀸이 놓인 ↙ 대각선 (row + col)의 집합

    def solve(row):
        global count    # 함수 바깥의 count 변수를 수정하기 위해 global 사용

        # 베이스 케이스: N개의 퀸을 모두 성공적으로 놓았을 경우
        if row == N:
            count += 1  # 경우의 수 하나 증가
            return
        
        # 현재 행(row)에 대해 가능한 열(col)을 시도
        for col in range(N):
            # 같은 열, 같은 ↘대각선, ↙대각선 중 하나라도 이미 사용 중이면 건너뜀
            if col in used_cols or (row - col) in used_diag1 or (row + col) in used_diag2:
                continue    # 다음 열로 넘어감

            # 현재 위치에 퀸을 놓기 (상태 저장)
            used_cols.add(col)          # 현재 열 사용 표시
            used_diag1.add(row - col)   # ↘ 방향 대각선 사용 표시
            used_diag2.add(row + col)   # ↙ 방향 대각선 사용 표시
            
            solve(row + 1)  # 다음 행(row + 1)으로 재귀 호출 (다음 퀸 놓기 시도)

            # 백트래킹: 놓았던 퀸을 되돌리기 (상태 복원)
            used_cols.remove(col)
            used_diag1.remove(row - col)
            used_diag2.remove(row + col)

    solve(0)  # 0번째 행부터 퀸 놓기 시작

    print(f'#{tc} {count}')  # 테스트케이스 번호와 결과 출력