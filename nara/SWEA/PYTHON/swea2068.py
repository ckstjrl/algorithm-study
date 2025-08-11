T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    max_v = arr[0]
    for i in arr:
        if i > max_v:
            max_v = i
    print(f"#{test_case} {max_v}")