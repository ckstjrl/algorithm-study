import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    nums = []
    result = 0

    if N == 1:
        nums.append(N)

    while N > 1:
        check = 0
        for j in range(9, 1, -1):
            if N % j == 0:
                nums.append(j)
                N //= j
                check = 1
                break
        if check == 0 and N > 10:
            result = -1
            break
    if result == -1:
        print(result)
    else:
        print(len(nums))