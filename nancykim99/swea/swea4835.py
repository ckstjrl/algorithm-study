T = int(input()) # 테스트 케이스

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 정수의 개수, 구간의 개수
    ai = list(map(int, input().split())) # N개의 정수

    list_of_sum = []
    for i in range(N-M+1): # 정수 내 구간 돌기
        s = 0
        for j in range(i, i+M): # 구간 내 sum
            s += ai[j]
        list_of_sum += [s] # s을 list_of_sum 리스트에 넣기

    max_v = list_of_sum[0] # 0번 원소를 최대로 가정
    min_v = list_of_sum[0] # 0번 원소를 최소로 가정

    for j in range(N-M+1):
        if max_v < list_of_sum[j]: # 최댓값
            max_v = list_of_sum[j]
        if min_v > list_of_sum[j]: # 최솟값
            min_v = list_of_sum[j]

    print(f'#{tc}', max_v - min_v)