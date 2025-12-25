# boj5052(D3): 전화번호 목록
t = int(input())
for _ in range(t):
    n = int(input())
    nums = [0] * n
    for i in range(n):
        nums[i] = input()

    nums.sort()
    for i in range(n - 1):
        if nums[i] in nums[i + 1][:len(nums[i])]:
            print('NO')
            break
    else:
        print('YES')