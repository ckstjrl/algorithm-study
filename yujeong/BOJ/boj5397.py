# 5397. 키로거

from collections import deque

N = int(input())
for _ in range(N):
    str = input()   # 입력 문자열 + 명령어 (input)
    l = deque()     # 커서 왼쪽
    r = deque()     # 커서 오른쪽

    for s in str:
        if s == '>':    # 명령어가 > 이면
            if r:       # 오른쪽으로 옮길 수 있는 경우에만 옮기기
                l.append(r.popleft())   # (커서 오른쪽 문자 1개를 왼쪽으로)
        elif s == '<':  # < 인 경우에도 마찬가지 반대로 
            if l: 
                r.appendleft(l.pop())
        elif s == '-':  # - 이면
            if l:       # 커서 왼쪽에 삭제할 문자가 있는 경우에만 삭제
                l.pop()
        else:           # 그 외(문자) 인 경우는 커서 왼쪽에 차례로 입력 
            l.append(s)

    # 출력: 왼쪽, 오른쪽 차례로 join해서 출력 
    print(''.join(l) + ''.join(r))  