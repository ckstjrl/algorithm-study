# BOJ9095. 1, 2, 3 더하기

T = int(input())

for _ in range(T):
    N = int(input())

    def find_sum_list(e):
        if e == 1:
            return 1
        if e == 2:
            return 2
        if e == 3:
            return 4
        return find_sum_list(e - 1) + find_sum_list(e - 2) + find_sum_list(e - 3)


    ans = find_sum_list(N)
    print(ans)
