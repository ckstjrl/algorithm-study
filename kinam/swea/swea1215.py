'''swea1215 회문1
"기러기", "토마토", "스위스"와 같이 똑바로 읽어도 거꾸로 읽어도 똑같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.

8x8 평면 글자판에서 제시된 길이를 가진 회문의 개수를 구하라.'''

T = 10
for t in range(1, T+1):
    N = 8 # 배열의 크기
    M = int(input()) # 회문의 길이
    arr = [list(map(str, input())) for _ in range(N)]
    # print(arr)

    cnt = 0
    for i in range(N):
        for j in range(N-M+1):
            reversed_arr = arr[i][j:j+M]

            if reversed_arr == reversed_arr[::-1]:
                # print(f"reversed_arr : {reversed_arr}")
                cnt += 1


            rev_col = []
            for x in range(M):
                rev_col += arr[j+x][i]


            if rev_col == rev_col[::-1]:
                # print(f"rev_col : {rev_col}")
                cnt += 1

    print(f"#{t} {cnt}")