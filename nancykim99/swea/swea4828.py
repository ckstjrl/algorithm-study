# 입력받기
T = int(input()) # 테스트 케이스의 수

for tc in range(1, T+1):
    N = int(input()) # 양수의 개수
    ai = list(map(int, input().split())) # N개의 양수 -> 배열 ai

    # 최댓값 구하기
    max_v = ai[0]
    for i in range(1, N):
        if max_v < ai[i]:
            max_v = ai[i]

    # 최솟값 구하기
    min_v = ai[0]
    for j in range(1, N):
        if min_v > ai[j]:
            min_v = ai[j]

    # 최댓값, 최솟값 차이 출력
    print(f'#{tc}', max_v - min_v)