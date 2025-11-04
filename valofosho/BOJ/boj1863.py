"""
건물의 모양은 모두 직사각형
최소한의 건물 수를 찾아내라

왼쪽부터 스카이라인을 보면서 고도가 바뀌는 지점의 좌표인 x,y 가 주어진다
첫 번째 지점의 x 좌표는 항상 1이다.

로직 정의:
1. 건물의 높이를 담아놓는 stack 설정
2. 스택이 비어있다면 건물의 높이를 넣어준다(1이상인 경우만)
3. 스택이 차있다면 값을 비교해서 높이가 큰 경우에는 append
   높이가 작다면 크기가 같거나 작아질때까지 반복해서 pop, cnt += 1
   높이가 작으면 append( 1 3 이 들어있다가 2가 h인 경우 )
4. 위의 과정들을 거쳐서 cnt를 쌓고 stack에 남은 값이 있다면 cnt에 더해주기
   """
import sys
input = sys.stdin.readline

N = int(input())
stack = []
cnt = 0
for _ in range(N):
    idx, h = map(int,input().split())
    if stack:
        # 0이 나오면 스택 정리하고 초기화
        if h == 0:
            cnt += len(stack)
            stack = []
        # 스택의 마지막 높이보다 현재 높이가 더 크면 추가
        elif stack[-1] < h:
            stack.append(h)
        # 스택의 마지막 높이보다 현재 높이가 더 작으면
        # 같거나 커질때까지 stack.pop
        elif stack[-1] > h:
            while stack:
                if stack[-1] > h:
                    stack.pop()
                    cnt += 1
                else:
                    # stack의 맨 윗값이 높이보다 작다면 append
                    # 새로운 건물을 위해 break
                    if stack[-1] !=  h:
                        stack.append(h)
                    break
            # 스택이 비어있는데 0이 아닌 값이 들어오면 append
            if not stack and h != 0:
                stack.append(h)
    # 초기값을 넣어주는 부분
    else:
        if h != 0:
            stack.append(h)
cnt += len(stack)
print(cnt)
                
            