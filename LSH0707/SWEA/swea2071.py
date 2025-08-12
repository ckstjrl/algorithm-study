T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    ans = round(sum(arr) / len(arr))
    print(f'#{test_case} {ans}')