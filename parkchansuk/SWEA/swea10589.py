# 부분집합의 합 / D2
T = int(input())
for tc in range(1, T+1):
    arr = []
    for a in range(1, 13): # 1부터 12까지의 원소를 가진 집합 만들기
        arr.append(a)

    N, K = map(int, input().split())

    cnt = 0 # N, K를 만족하는 부분집합의 개수
    for i in range(1<<12): # arr의 부분집합 비트연산자를 사용하여 만듦
        sub_set = [] # 부분집합 추출
        for j in range(12):
            if i & (1<<j):
                sub_set.append(arr[j])

        if len(sub_set) == N: # 부분집합의 길이가 N 과 동일할 경우 아래 코드 진행
            sum_set = 0
            for s in sub_set: # 부분집합의 원소의 합 구하기
                sum_set += s
            if sum_set == K: # 부분집합 원소의 합이 K와 동일하면 cnt 증가
                cnt += 1

    print(f'#{tc} {cnt}')