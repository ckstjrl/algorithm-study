# BOJ 2346. 풍선 터드리기 / D2
'''
1번부터 N번까지 N개의 풍선이 원형으로 놓여 있고. i번 풍선의 오른쪽에는 i+1번 풍선이 있고, 왼쪽에는 i-1번 풍선이 있다.
단, 1번 풍선의 왼쪽에 N번 풍선이 있고, N번 풍선의 오른쪽에 1번 풍선이 있다.
각 풍선 안에는 종이가 하나 들어있고, 종이에는 -N보다 크거나 같고, N보다 작거나 같은 정수가 하나 적혀있다.
이 풍선들을 다음과 같은 규칙으로 터뜨린다.

우선, 제일 처음에는 1번 풍선을 터뜨린다.
다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 값만큼 이동하여 다음 풍선을 터뜨린다.
양수가 적혀 있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동한다.
이동할 때에는 이미 터진 풍선은 빼고 이동한다.

예를 들어 다섯 개의 풍선 안에 차례로 3, 2, 1, -3, -1이 적혀 있었다고 하자.
이 경우 3이 적혀 있는 1번 풍선, -3이 적혀 있는 4번 풍선, -1이 적혀 있는 5번 풍선,
1이 적혀 있는 3번 풍선, 2가 적혀 있는 2번 풍선의 순서대로 터지게 된다.
'''
import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque(map(int, sys.stdin.readline().split()))
num = deque(i for i in range(1, N+1))

order = []
stk = [1]
num.popleft()
while num:
    a = stk.pop()
    b = q.popleft()
    if b > 0:
        for _ in range(b-1):
            num.rotate(-1)
            q.rotate(-1)
        stk.append(num.popleft())
        order.append(a)
    else:
        for _ in range(abs(b)):
            num.rotate(1)
            q.rotate(1)
        stk.append(num.popleft())
        order.append(a)

ans = order+stk
print(f'{" ".join(map(str, ans))}')

'''
덱을 사용하여 문제 풀이
풍선 번호를 뽑아서 stk에 넣고
스택을 활용하여 풍선 안에 있는 숫자에 따라 rotate를 진행하여 다음 풍선 선택
마지막 풍선의 경우 스택에 계속 남아있어서
num+stk로 ans 출력
'''