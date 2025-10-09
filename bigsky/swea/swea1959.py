# SWEA1959: 두 개의 숫자열
T = int(input())
for tc in range(1, T + 1) : 
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        A, B = B, A
    
    arr = []

    for k in range(len(B) - len(A) + 1):
        total = 0
        for r in range(len(A)):
            total += A[r] * B[r + k]
        arr.append(total)
    
    print(f'#{tc} {max(arr)}')