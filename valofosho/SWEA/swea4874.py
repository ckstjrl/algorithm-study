T = int(input())
for test_case in range(1, T+1):
    arr = list(input().split())
    flag = 'error'
    stack = []
    for i in arr:
        # 정수면 스택에
        if i.isdecimal():
            stack.append(i)
        # 연산자면 스택에서 뽑아서 연산 후 스택에
        elif i in '+*/-':
            if len(stack) >= 2:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == '+':
                    num = a+b
                    stack.append(num)
                elif i == '-':
                    num = a-b
                    stack.append(num)
                elif i == '*':
                    num = a*b
                    stack.append(num)
                elif i == '/':
                    num = a//b
                    stack.append(num)
            else:
                break
        else:
            # 스택이 최종 답안만 있는게 아니면
            if len(stack) != 1:
                break
            # 최종 답안 뽑기
            else:
                ans = stack.pop()
                flag = 'True'
    if flag == 'error':
        print(f"#{test_case} {flag}")
    else:
        print(f"#{test_case} {ans}")