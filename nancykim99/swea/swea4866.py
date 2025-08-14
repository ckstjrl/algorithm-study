T = int(input())

for tc in range(1, T+1):
    arr = list(input())

    top = -1 # 하나씩 넣기 위해 -1
    stack = [0] * 100 # 스택을 만듬

    ans = 1 # 일단 괄호 성공
    for x in arr:
        if x in ['(','{']: # 열린 괄호가 있을 때
            top += 1
            stack[top] = x # stack에 push
        elif x in [')','}']: # 닫힌 괄호가 있을 때
            if top == -1: # 열린 괄호 push 된게 없으면
                ans = 0
                break
            elif (stack[top] == '(' and x == ')' or
            stack[top] == '{' and x == '}'): # 괄호가 짝을 이룰 경우
                top -= 1 # stack을 pop
            else:
                ans = 0 # 괄호가 짝을 못 이룬 경우
                break
    if top != -1: # top을 다 pop 하지 못한 경우 = 짝을 못 이룬 경우
        ans = 0
    print(f'#{tc} {ans}')