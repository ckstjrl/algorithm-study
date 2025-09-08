'''
문제
창영이는 강산이의 비밀번호를 훔치기 위해서 강산이가 사용하는 컴퓨터에 키로거를 설치했다. 며칠을 기다린 끝에 창영이는 강산이가 비밀번호 창에 입력하는 글자를 얻어냈다.

키로거는 사용자가 키보드를 누른 명령을 모두 기록한다. 따라서, 강산이가 비밀번호를 입력할 때, 화살표나 백스페이스를 입력해도 정확한 비밀번호를 알아낼 수 있다. 

강산이가 비밀번호 창에서 입력한 키가 주어졌을 때, 강산이의 비밀번호를 알아내는 프로그램을 작성하시오. 강산이는 키보드로 입력한 키는 알파벳 대문자, 소문자, 숫자, 백스페이스, 화살표이다.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한줄로 이루어져 있고, 강산이가 입력한 순서대로 길이가 L인 문자열이 주어진다. (1 ≤ L ≤ 1,000,000) 강산이가 백스페이스를 입력했다면, '-'가 주어진다. 이때 커서의 바로 앞에 글자가 존재한다면, 그 글자를 지운다. 화살표의 입력은 '<'와 '>'로 주어진다. 이때는 커서의 위치를 움직일 수 있다면, 왼쪽 또는 오른쪽으로 1만큼 움직인다. 나머지 문자는 비밀번호의 일부이다. 물론, 나중에 백스페이스를 통해서 지울 수는 있다. 만약 커서의 위치가 줄의 마지막이 아니라면, 커서 및 커서 오른쪽에 있는 모든 문자는 오른쪽으로 한 칸 이동한다.

출력
각 테스트 케이스에 대해서, 강산이의 비밀번호를 출력한다. 비밀번호의 길이는 항상 0보다 크다.
'''



def valid_current(current):     # 현재 current의 위치 (범위)가 적합한지 판단해보자.
    global result

    if current < 0:                 # 먼저, 커서의 위치가 음수일 수는 없으니
        current = 0                 # 커서의 위치가 음수라면 0으로 조정하자.
    elif current > len(result):     # 그리고, 커서의 위치가 문자열의 최대 길이를 더 초과할 순 없으니
        current = len(result)       # 커서의 위치가 문자열의 최대 길이를 넘지 않도록 조정하자.

    return current



T = int(input())
for test_case in range(T):
    text = list(input())  # 우선 문자열을 그대로 인풋을 받는다.

    result = []     # 최종적인 정답이 출력될 result.
    current = 0     # 현재 커서의 위치. 만약 current가 3이라면, 3번 인덱스 왼쪽에 커서가 있다는 것을 의미.

    for i in text:
        current = valid_current(current)    # current가 음수가 되지 않고 최대치도 초과하지 않도록 교정해주는 함수.

        if i == '<':            # 만약 문자열을 순회하다가 '<'을 만날 경우,
            current -= 1        # 커서의 위치를 왼쪽으로 한 칸 옮기자.
            continue

        elif i == '>':          # i가 만약 '>'라면
            current += 1        # 커서의 위치를 오른쪽으로 한 칸 옮기자.
            continue

        elif i == '-':          # i가 만약 '-'라면
            if current == 0: continue   # 커서가 가장 왼쪽이었을 때는 아무런 동작도 하지 않는다.
            result.pop(current-1)       # 그 외에는 i-1번째 인덱스에 있는 글자를 삭제한 뒤,
            current -= 1        # 커서의 위치도 오른쪽으로 한 칸 옮기자.
            continue

        else:                  # i가 화살표도 아니고 백스페이스도 아니라면 글자라는 의미.
            result.insert(current, i)    # i를 커서 (current)를 기준으로 text에 삽입한다.
            current += 1



    print(''.join(result))



# 그냥 이렇게만 하면 될 줄 알았는데 웹에 제출했을 때 [시간 초과] 에러 나서 실패...
# ChatGPT 왈 시간 초과는 신경도 안 쓴 방식이었다고 함. 이하는 ChatGPT가 교정해준 코드

'''
아래 코드는 두 스택(left/right) 기법으로 커서를 O(1)에 이동·삽입·삭제해, L ≤ 1,000,000 입력에서도 통과합니다.
리스트 중간 insert/pop(O(n)) 대신 왼쪽 스택 ↔ 오른쪽 스택 사이에서 append/pop만 사용합니다.
왜 빠른가?
	•	list.insert(i, x)/pop(i)는 O(n) 이지만,
	•	append/pop는 맨끝에서 O(1)
	•	커서 이동 = 문자 하나를 다른 스택으로 옮김(O(1)) → 전체 O(L)

엣지 케이스
	•	<<< 처럼 왼쪽이 비었는데 <가 와도 무시됨
	•	>>> 처럼 오른쪽이 비었는데 >가 와도 무시됨
	•	---- 처럼 지울 게 없는데 -가 와도 무시됨
	•	줄 끝이 개행만 있어도 rstrip('\n')으로 안전 처리
'''

'''
import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    out = []

    for _ in range(T):
        s = input().rstrip('\n')  # 한 줄 입력(개행 제거)
        left, right = [], []      # 커서 왼쪽/오른쪽

        for ch in s:
            if ch == '<':
                if left:                 # 왼쪽에 문자가 있으면 커서를 왼쪽으로
                    right.append(left.pop())
            elif ch == '>':
                if right:                # 오른쪽에 문자가 있으면 커서를 오른쪽으로
                    left.append(right.pop())
            elif ch == '-':
                if left:                 # 백스페이스: 커서 앞(왼쪽) 문자 삭제
                    left.pop()
            else:
                left.append(ch)          # 일반 문자: 커서 위치에 삽입(왼쪽 스택에 push)

        # 결과: left + reversed(right)
        if right:
            left.extend(reversed(right))
        out.append(''.join(left))

    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()
'''



# 또 다른 추천 코드

'''
cursor 변수 하나만으로도 O(L)로 풀 수 있습니다. 핵심은 연결 리스트(linked list)를 배열로 흉내 내는 방식이에요.
파이썬 리스트의 insert/pop을 쓰면 중간 삽입/삭제가 O(n) 이라 L=10⁶에서 시간 초과가 나지만, 배열 3개(prev, next, ch)와 커서 1개(cur) 로 연결을 관리하면 모든 연산이 O(1) 입니다.

아이디어 (갭 버퍼 느낌의 연결 리스트)
	•	노드 0은 더미 헤드(문자 없음).
	•	cur = 커서 왼쪽 노드의 인덱스(커서가 가리키는 위치의 왼쪽에 있는 문자 노드).
	•	시작은 cur = 0 (맨 앞).
	•	삽입: cur 오른쪽에 새 노드 끼워넣고, cur을 그 새 노드로 이동
	•	백스페이스 -: cur이 가리키는 왼쪽 문자(=cur 노드)를 삭제하고 cur = prev[cur]
	•	좌/우 화살표: cur = prev[cur] 또는 cur = next[cur]
	•	출력: next[0]부터 오른쪽으로 쭉 따라가며 ch[]를 이어붙임
'''

'''
import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    out = []

    for _ in range(T):
        s = input().rstrip('\n')
        L = len(s)

        # 배열로 연결리스트 구현
        # 0은 더미 헤드: prev[0] = -1, next[0] = 첫 문자 노드(없으면 -1)
        prev = [-1] * (L + 1)
        next = [-1] * (L + 1)
        ch   = ['']  * (L + 1)

        cur = 0       # 커서 왼쪽 노드(더미부터 시작)
        unused = 1    # 다음에 쓸 노드 인덱스(1..L)

        for c in s:
            if c == '<':
                if prev[cur] != -1:      # 왼쪽에 문자가 있으면
                    cur = prev[cur]
            elif c == '>':
                if next[cur] != -1:      # 오른쪽에 문자가 있으면
                    cur = next[cur]
            elif c == '-':
                if cur != 0:             # 커서 왼쪽 문자가 존재
                    left = cur
                    a = prev[left]       # 왼쪽 이웃
                    b = next[left]       # 오른쪽 이웃
                    # 연결 끊고 이웃끼리 잇기
                    next[a] = b
                    if b != -1:
                        prev[b] = a
                    cur = a              # 커서를 한 칸 왼쪽으로
                    # (left 노드는 재사용 안 해도 됨)
            else:
                # 새 노드 idx를 cur 오른쪽에 삽입
                idx = unused
                unused += 1
                ch[idx] = c

                a = cur
                b = next[a]

                prev[idx] = a
                next[idx] = b
                next[a] = idx
                if b != -1:
                    prev[b] = idx

                cur = idx                # 커서를 새 노드로 이동

        # 결과 문자열 만들기: head의 오른쪽부터 끝까지 순회
        res = []
        p = next[0]
        while p != -1:
            res.append(ch[p])
            p = next[p]
        out.append(''.join(res))

    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()
'''