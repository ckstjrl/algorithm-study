T = int(input())
for test_case in range(T):
    a = input()
    stack = []  
    ans = 'YES'
    for x in a:  # 문자열 순회하면서 '('-스택에 추가 ')'-스택검사후 pop혹은 NO출력 순회종료후 스택검사
        if x == '(':
            stack.append(x)
        elif stack and x == ')':
            stack.pop()
        elif len(stack) == 0 and x == ')':
            ans = 'NO'
            break
    if stack:
        ans = 'NO'
    
    print(ans)