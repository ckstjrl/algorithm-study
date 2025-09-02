# 4949. 균형잡힌 세상
from collections import deque

left = ['[', '(']
right = [']', ')']

while True:
    stack = deque()
    string = input()

    # 입력받은 문자열이 '.'이 아니면 진행
    if string != ".":
        ans = "yes"
        for s in string:
            if s in left:   # 왼쪽 괄호면 stack에 넣기 
                stack.append(s)
            elif s in right:    # 오른쪽 괄호면
                if not stack:   # 스택이 비어있으면 균형 x
                    ans = "no"
                    break
                lp = stack.pop()
                if right.index(s) != left.index(lp):    # 짝이 맞지 않는 괄호면 균형 x
                    ans = "no"
                    break
        else:   # 문자열 끝까지 다 봤는데 스택에 괄호가 남아있으면 균형 x
            if stack:
                ans = "no"
        
        print(ans)

    # 입력받은 문자열이 '.'이면 종료 
    else:
        break