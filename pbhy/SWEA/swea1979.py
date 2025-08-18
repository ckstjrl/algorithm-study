# 1979. 어디에 단어가 들어갈 수 있을까

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    result = 0  # K와 같아지는 갯수 -> 찾아야 하는 수

    for i in range(N):  # 가로로 행 우선 순회
        cnt = 0 # 1의 숫자 갯수
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                cnt = 0 # 1 다음에 0이 나오면 그냥 초기화해버림

            if cnt == K :
                    if j == N-1 or arr[i][j+1] == 0 :    # 순서 바꾸지 말자! -> 순서 바꾸면 범위 벗어남
                            result += 1

    for j in range(N):  # 세로로 열 우선 순회
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
            else:
                cnt = 0

            if cnt == K :
                if i == N-1 or arr[i+1][j] == 0 :    # 순서 바꾸지 말자!
                    result += 1

    print(f'#{tc} {result}')