T = int(input())

for tc in range(1, T+1):
    arr = list(input())
    top = -1
    stack = [0] * 1000 # 1000개 이상

    for x in arr:
        if x == stack[top]:
            top -= 1
        else:
            top += 1
            stack[top] = x
    if top != -1:
        result = top + 1 # top은 0부터 시작하기 때문
    print(f'#{tc} {result}')