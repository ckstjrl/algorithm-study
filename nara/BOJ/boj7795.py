import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    cnt_B = M
    max_A = N-1
    max_B = M-1
    cnt = 0

    while max_B >= 0 and max_A >= 0:
        if A[max_A] > B[max_B]:
            cnt += cnt_B
            max_A -= 1
        elif A[max_A] <= B[max_B]:
            max_B -= 1
            cnt_B -= 1
    print(cnt)