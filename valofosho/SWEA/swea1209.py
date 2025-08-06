for case in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    # print(arr)
    count_list = []
    count_fslash = 0
    count_bslash = 0
    for i in range(100):
        count_list.append(sum(arr[i]))
        cnt = 0
        for j in range(100):
            cnt += arr[j][i]
            if i == j:
                count_bslash += arr[i][j]
            if i+j == 99:
                count_fslash += arr[i][j]
        count_list.append(cnt)
    count_list.append(count_bslash)
    count_list.append(count_fslash)
    print(f"#{T} {max(count_list)}")
