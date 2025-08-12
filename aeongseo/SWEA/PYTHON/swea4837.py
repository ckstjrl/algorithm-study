'''
4837. 부분집합의 합 (D2)
'''

T = int(input())
 
for tc in range(1, T+1):
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N, K = map(int, input().split())
    cnt = 0
 
    for i in range(1<<12):                  # 부분 집합의 갯수
        arr = []
        result = 0

        for j in range(12):                 
            if i & (1<<j):                  # i 와 2^j 의 값이 모두 참이면 부분집합에 원소 추가
                arr.append(A[j])

        for k in arr:                       
            result += k
        if len(arr) == N and result == K:   # 부분집합의 원소의 갯수가 N이고, 합이 K 이면 cnt 증가
            cnt += 1
 
    print(f'#{tc} {cnt}')