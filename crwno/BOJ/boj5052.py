T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    nums = [str(input()) for _ in range(n)]
    # nums.sort(key=len)
    nums.sort()

    # for i in range(n):
    #     length = len(nums[i])
    #     nums[i] += 'F' * (10 - length)

    flag = True
    for i in range(n - 1):
        if nums[i + 1][:len(nums[i])] == nums[i]:
            flag = False
            break

    if flag:
        print("YES")
    else:
        print("NO")
