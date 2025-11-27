T = int(input()) # 테스트 케이스

for tc in range(1, T+1):
    N = int(input()) # 정수의 개수
    ai = list(map(int, input().split())) # N개의 정수

    # 아래부터 쌓아올리는 방식
    drop = []
    for i in range(N): # 정수의 개수만큼
        a = 0
        for j in range(i+1, N): # 정수의 개수에서 -1 : i를 빼기 때문
            if ai[i] > ai[j]: # i가 오른쪽 숫자보다 크면
                a += 1 # 1개 더하기
        drop += [a] # drop에 추가

    max_drop = drop[0]

    for i in range(N): # drop의 최댓값
        if max_drop < drop[i]:
            max_drop = drop[i]

    print(f'#{tc}', max_drop)