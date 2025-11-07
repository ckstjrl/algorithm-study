T = int(input())
for tc in range(T):
    N = int(input())
    ans = []
    while N >= 10:
        if N % 9 == 0:
            new_N = N // 9
            ans.append(9)
        elif N % 8 == 0:
            new_N = N // 8
            ans.append(8)
        elif N % 7 == 0:
            new_N = N // 7
            ans.append(7)
        elif N % 6 == 0:
            new_N = N // 6
            ans.append(6)
        elif N % 5 == 0:
            new_N = N // 5
            ans.append(5)
        elif N % 4 == 0:
            new_N = N // 4
            ans.append(4)
        elif N % 3 == 0:
            new_N = N // 3
            ans.append(3)
        elif N % 2 == 0:
            new_N = N // 2
            ans.append(2)
        else:
            break
        N = new_N
    res = 0
    if N >= 10:
        res = -1
    else:
        res = len(ans) + 1

    print(res)