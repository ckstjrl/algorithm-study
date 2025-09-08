# BOJ 10866. 덱 /D2
'''
정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
명령은 총 여덟 가지이다.

push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''
import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()
size = 0
for _ in range(N):
    op = list(sys.stdin.readline().split())

    if op[0] == 'push_front':
        q.append(int(op[1]))
        q.rotate(1)
        size += 1

    elif op[0] == 'push_back':
        q.append(int(op[1]))
        size += 1

    elif op[0] == 'pop_front':
        if size > 0:
            print(q.popleft())
            size -= 1
        else:
            print(-1)

    elif op[0] == 'pop_back':
        if size > 0:
            print(q.pop())
            size -= 1
        else:
            print(-1)

    elif op[0] == 'size':
        print(size)

    elif op[0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)

    elif op[0] == 'front':
        if size > 0:
            print(q[0])
        else:
            print(-1)

    elif op[0] == 'back':
        if size > 0:
            print(q[-1])
        else:
            print(-1)

'''
여태까지 풀어왔던 스택, 큐와 같은 문제로
풀이 방식 동일
'''