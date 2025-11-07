while True:
    nums = list(map(int, input().split()))

    if nums[0] == 0 and nums[1] == 0 and nums[2] == 0:
        break

    nums.sort()

    if (nums[0]**2) + (nums[1]**2) == nums[2]**2:
        print('right')
    else:
        print('wrong')
