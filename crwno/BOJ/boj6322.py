# 제발 예제출력 잘보기
arr = []

while True:
    line = input()
    if line == '0 0 0':
        break
    row = list(map(int, line.split()))
    arr.append(row)

T = len(arr)
for tc in range(1, T + 1):
    line = arr[tc - 1]
    res = -1

    a = line[0]
    b = line[1]
    c = line[2]

    if a == -1:
        if c > b:
            a = (c ** 2 - b ** 2) ** (1 / 2)
            ans = a
            ans_w = 'a'
        else:
            res = 0
    elif b == -1:
        if c > a:
            b = (c ** 2 - a ** 2) ** (1 / 2)
            ans = b
            ans_w = 'b'
        else:
            res = 0
    elif c == -1:
        c = (a ** 2 + b ** 2) ** (1 / 2)
        ans = c
        ans_w = 'c'

    if res == 0:
        print(f'Triangle #{tc}\nImpossible.')
    else:
        print(f'Triangle #{tc}\n{ans_w} = {ans:.3f}')

    if tc != T:
        print()

