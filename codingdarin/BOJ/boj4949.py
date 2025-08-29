# BOJ 4949 - 균형잡힌 세상 (D2)

# 스택으로 풀기

while True:
    line = input()
    if line == '.':
        break

    stack = []
    ans = 'yes'

    for i in line:
        if i in '([':
            stack.append(i)
        
        elif i in ')]':
            if not stack:
                ans = 'no'
                break
            
            top = stack.pop()
            if i == ')':
                if top != '(':
                    ans = 'no'
                    break
            elif i == ']':
                if top != '[':
                    ans ='no'
                    break
    
    if stack:
        ans = 'no'
    
    print(ans)