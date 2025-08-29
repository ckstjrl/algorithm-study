def yn(char): 
    stack = []
    for i in char:
        if i in '[(':  # 괄호 열리면 스택에 추가
            stack.append(i)
        elif i == ']': # 닫힌 괄호면 마지막으로 스택에 추가된 괄호가 짝이 맞는지 확인하고 없거나 안맞으면 'no'리턴
            if stack and stack[-1] == '[':
                stack.pop()
            elif stack and stack[-1] == '(':
                return 'no'
            elif len(stack) == 0:
                return 'no'
        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            elif stack and stack[-1] == '[':
                return 'no'
            elif len(stack) == 0:
                return 'no'
    if len(stack) > 0:  # 검사 끝나고 stack이 비어있으면 'yes'
        return 'no'
    else:
        return 'yes'

while True:
    a = input()
    if a == '.':
        break
    print(yn(a))


