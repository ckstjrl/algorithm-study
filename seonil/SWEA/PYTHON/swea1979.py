T = int(input())  # 테스트 케이스 개수 입력

for test_case in range(1, T + 1):

    N, K = map(int, input().split())

    # 퍼즐 정보 입력 (1: 빈칸, 0: 채워진 칸)
    word_puzzle = [list(map(int, input().split())) for _ in range(N)]

    cnt_k_len_words = 0  # K 길이 단어가 들어갈 수 있는 자리 개수

    # 1. 가로 방향 검사
    for i in range(N):  # 각 행(row) 순회
        cnt_ones = 0  # 연속된 1의 개수
        for j in range(N):  # 각 열(column) 순회
            if word_puzzle[i][j] == 1:  # 칸이 빈칸(1)이면
                cnt_ones += 1
            else:  # 칸이 채워진칸(0)이면
                if cnt_ones == K:  # 지금까지의 연속된 칸 길이가 K라면
                    cnt_k_len_words += 1  # 가능한 자리로 카운트
                cnt_ones = 0  # 연속 카운트 초기화
        # 행의 끝까지 왔는데 연속된 칸 길이가 K라면 카운트
        if cnt_ones == K:
            cnt_k_len_words += 1

    # 2. 세로 방향 검사(가로 방향 검사와 동일한 로직으로 진행)
    for i in range(N):  # 각 열(column) 순회
        cnt_ones = 0
        for j in range(N):  # 각 행(row) 순회
            if word_puzzle[j][i] == 1:
                cnt_ones += 1
            else:
                if cnt_ones == K:
                    cnt_k_len_words += 1
                cnt_ones = 0

        if cnt_ones == K:
            cnt_k_len_words += 1

    # 결과 출력
    print(f'#{test_case} {cnt_k_len_words}')