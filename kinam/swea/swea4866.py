'''swea4866 괄호지우기
주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.

예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.

정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.

print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.
'''
# 이프문 난사로 짠 코드
# T = int(input())
# for t in range(1, T + 1):
#     stack = []
#     txt = input()
#     top = -1
#     ans = 1
#     for x in txt:
#         if x in ['(', '{']:
#             stack.append(x)
#
#         elif x == ')':
#             if len(stack) == 0:
#                 ans = 0
#                 break
#
#             elif stack[-1] == '(':
#                 stack.pop()
#
#             elif stack[-1] != '(':
#                 ans = 0
#                 break
#
#         elif x == '}':
#             if len(stack) == 0:
#                 ans = 0
#                 break
#
#             elif stack[-1] == '{':
#                 stack.pop()
#
#             elif stack[-1] != '{':
#                 ans = 0
#                 break
#
#     if len(stack) != 0:
#         ans = 0
#
#     print(f"#{t} {ans}")


#딕셔너리로 구현한 코드
T = int(input())
for t in range(1, T + 1):
    stack = [0] * 100
    top = -1
    txt = input()
    ans = 1

    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    for x in txt:
        if x in brackets.keys():  # 여는 괄호들이면
            top += 1
            stack[top] = x

        elif x in brackets.values():  # 닫는 괄호들이면
            if top == -1:  # 스택이 비어있으면
                ans = 0
                break

            elif x != brackets[stack[top]]:  # 닫는괄호가 여는괄호와 일치해야함
                ans = 0
                break

            else:
                top -= 1

    if top != -1:
        ans = 0

    print(f"#{t} {ans}")

