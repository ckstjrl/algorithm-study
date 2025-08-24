"""
10828. 스택
"""

import sys

N = int(input())

# 스택을 구현하기 위한 고정 크기 배열 (최대 10000개까지 저장 가능)
stack = [0] * 10000
top = -1  # 스택의 가장 위(top) 원소의 인덱스. 비어있으면 -1

for i in range(N):
    command = sys.stdin.readline().split()  # 명령 입력 (push X / pop / size / empty / top)

    if command[0] == 'pop':  # pop 연산
        if top == -1:  # 스택이 비어있으면
            print(-1)
        else:  # 스택이 비어있지 않으면
            pop = stack[top]  # 스택에서 top 위치의 값 꺼내기
            top -= 1  # top을 한 칸 내림
            print(pop)  # 꺼낸 값 출력

    elif command[0] == 'size':  # size 연산
        print(top + 1)  # size = (top 인덱스 + 1)

    elif command[0] == 'empty':  # empty 연산
        if top == -1:  # 스택이 비어있으면
            print(1)
        else:  # 비어있지 않으면
            print(0)

    elif command[0] == 'top':  # top 연산
        if top == -1:  # 스택이 비어있으면
            print(-1)
        else:  # 스택이 비어있지 않으면
            print(stack[top])  # top 위치의 값 출력

    else:  # push X 연산
        x = int(command[1])  # 푸시할 값을 정수 형태로 저장
        top += 1  # top 인덱스를 한 칸 올림
        stack[top] = x  # 스택의 해당 위치에 값 저장(push)