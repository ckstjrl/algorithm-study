T  = int(input())
for test_case in range(1, T+1):
    # N: 배열의 크기, M: 회문의 길이
    N, M = map(int, input().split())
    # maps의 배열 크기는 N * N
    maps = [list(input()) for _ in range(N)]
    ans = ''
    # 행에서 회문 검사
    for i in range(N):
        for j in range(N-M+1):
            # 행을 고정하고 열을 슬라이싱
            str1 = ''.join(maps[i][j:j+M])
            # 문자열을 뒤집어도 원본과 동일한지
            if str1 == str1[::-1]:
                ans = str1
    # 열에서 회문 검사
    for j in range(N):
        # 행은 움직이면서 봐야 하므로 N-M+1까지
        for i in range(N-M+1):
            temp = []
            # 열을 고정시키고 행을 순회
            for k in range(M):
                temp.append(maps[i+k][j])
            # 리스트 to 문자열
            str2 = ''.join(temp)
            # 뒤집어도 문자열이 동일한지
            if str2 == str2[::-1]:
                ans = str2

    print(f"#{test_case} {ans}")
