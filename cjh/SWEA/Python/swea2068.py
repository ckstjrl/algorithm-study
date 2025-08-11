t = int(input())
for test_case in range(1, t + 1):
    nums = list(map(int, input().split()))

    maximum = max(nums)

    print(f"#{test_case} {maximum}")