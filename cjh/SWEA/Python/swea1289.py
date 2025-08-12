t = int(input())
for test_case in range(1, t + 1):
    nums = list(input())

    cnt_1 = 0
    flag1 = 0
    flag0 = 1
    for i in range(len(nums)):
        if nums[i] == "1":
            flag0 = 0
            if flag1 == 1:
                continue
            else:
                flag1 = 1
                cnt_1 += 1
        else:
            flag1 = 0
            if flag0 == 1:
                continue
            else:
                flag0 = 1
                cnt_1 += 1
    print(f"#{test_case} {cnt_1}")