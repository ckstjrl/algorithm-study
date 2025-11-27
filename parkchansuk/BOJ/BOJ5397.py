# BOJ 5397. 키로거 / D2
'''
창영이는 강산이의 비밀번호를 훔치기 위해서 강산이가 사용하는 컴퓨터에 키로거를 설치했다.
며칠을 기다린 끝에 창영이는 강산이가 비밀번호 창에 입력하는 글자를 얻어냈다.

키로거는 사용자가 키보드를 누른 명령을 모두 기록한다.
따라서, 강산이가 비밀번호를 입력할 때, 화살표나 백스페이스를 입력해도 정확한 비밀번호를 알아낼 수 있다.

강산이가 비밀번호 창에서 입력한 키가 주어졌을 때, 강산이의 비밀번호를 알아내는 프로그램을 작성하시오.
강산이는 키보드로 입력한 키는 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표이다.
'''
import sys
N = int(sys.stdin.readline())
for _ in range(N):
    arr = list(sys.stdin.readline().strip())
    left, right = [], []

    for a in arr:
        if a == '<':
            if left:
                right.append(left.pop())

        elif a == '>':
            if right:
                left.append(right.pop())

        elif a == '-':
            if left:
                left.pop()
        else:
            left.append(a)

    pw = left + right[::-1]
    print(f'{"".join(pw)}')

    # while arr:
    #     a = arr.popleft()
    #     if a == '<':
    #         if cusor > 0:
    #             cusor -= 1
    #
    #     elif a == '>':
    #         if cusor < len(pw)+1:
    #             cusor += 1
    #
    #     elif a == '-':
    #         if pw and 0 < cusor <= len(pw)+1:
    #             pw.pop(cusor-2)
    #             cusor -= 1
    #     else:
    #         pw.insert(cusor, a)
    #         cusor += 1
'''
시간 초과로 인해 커서를 숫자로 표현하고 움직이면서 제작하는 것 포기
두개의 스택을 사용하여 풀이
커서를 기준으로 왼쪽 오른쪽 나눠서 생각
오른쪽의 경우 append하게 되면 맨 뒤에 들어가게 되므로
마지막 출력할 때 슬라이싱을 통해 거꾸로 넣어주는 것 중요
'''