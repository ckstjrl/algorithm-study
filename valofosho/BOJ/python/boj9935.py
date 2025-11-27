"""
문제 정의
1. 폭발 문자열이 숨겨져 있다
-> 폭발 문자열이 폭발하면 해당 문자는 사라지고 남은 문자열을 순서대로 붙인다.
-> 새로 생긴 문자열에 폭탄이 나타날수도 있다

로직 정의
첫 번째 풀이
1. 입력값을 스택에 넣어주면서 bomb의 첫 글자와 겹치면
    -> cnt를 높여가면서 완벽하게 일치하면 넣고 pop
    -> 중간에 다른 글자가 섞이면 cnt = 0
2. 한 회차가 끝나면 해당 스택을 다시 chars처럼 받아서 진행
    -> stack이 비어있으면 FRULA 출력 후 break
    -> stack이 bomb보다 길고 pop연산을 해서 다시 검사해야되면 chars로 진행
    -> 둘 다 아니면 stack 조인으로 문자열 반환 후 break 
두 번째 풀이
1. 스택에 넣으면서 bomb의 끝자리와 동일한 지 체크
    -> 만약 동일하면 슬라이싱으로 모든 자리가 동일한지 체크한 후 같다면 pop
    -> 아니면 그대로 
2. 스택이 남아있으면 스택 조인 출력, 아니면 FRULA 출력
"""


import sys
input = sys.stdin.readline

chars = list(input().strip())
bomb = list(input().strip())
b = len(bomb)
stack = []
for i in range(len(chars)):
    stack.append(chars[i])
    # 스택의 탑과 폭탄문자의 끝자리가 같으면
    if stack[-1] == bomb[-1]:
        # 슬라이싱으로 확인
        if stack[-b:] == bomb:
            # 같으면 문자열들 pop
            for j in range(b):
                stack.pop()
        # 다르면 그냥 진행
        else:
            continue
if stack:
    print(''.join(stack))
else:
    print('FRULA')




"""
첫 번째 풀이 -> 시간 초과
chars = list(input().strip())
bomb = list(input().strip())
stack =[]
b = len(bomb)
while True:
    cnt = 0
    stack =[]
    flag = False
    for i in range(len(chars)):
        if chars[i] != bomb[cnt]:
            stack.append(chars[i])
            cnt = 0
            if chars[i] == bomb[cnt]:
                cnt += 1
        else:
            stack.append(chars[i])
            cnt += 1
            if cnt == b:
                flag = True
                for p in range(b):
                    stack.pop()
                    
                cnt = 0
    if not stack:
        print("FRULA")
        break
    # 한번 더! 
    elif len(stack) >= b and flag:
        chars = stack[:]
    else:
        print(''.join(stack))
        break

"""