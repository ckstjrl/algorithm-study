N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]

score = {
    'A+': 4.3,
    'A0': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B0': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C0': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D0': 1.0,
    'D-': 0.7,
    'F': 0.0
}

res1 = 0
res2 = 0
ans = 0
for i in range(N):
    res1 += float(arr[i][1]) * score[arr[i][2]]
    res2 += float(arr[i][1])

ans = str(res1 / res2)

if len(ans) <= 3:
    print(ans, end='')
    print(0)
elif len(ans) == 4:
    print(ans)
else:
    if int(ans[4]) >= 5:
        if int(ans[3]) + 1 >= 10:
            if int(ans[2]) + 1 >= 10:
                print(int(ans[0]) + 1, end='')
                print(ans[1], end='')
                print(int(ans[2]) - 9, end='')
                print(int(ans[3]) - 9, end='')
            else:
                print(ans[0:2], end='')
                print(int(ans[2]) - 9, end='')
                print(int(ans[3]) - 9, end='')
        else:
            print(ans[0:3], end='')
            print(int(ans[3]) + 1, end='')
    else:
        print(ans[0:4])