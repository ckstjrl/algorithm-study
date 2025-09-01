T = int(input())
for _ in range(1, T + 1):
    answer = input()
    res = 0
    cnt = 0

    for i in range(len(answer)):
        if answer[i] == "O":
            cnt += 1
            res += cnt
        else:
            cnt = 0

    print(res)