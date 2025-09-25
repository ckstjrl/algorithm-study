'''
BOJ25192 / D2): 인사성 밝은 곰곰이

해결 방법 : set이 list보다 빠르다. 시간 초과가 나와서, set으로 바꿨더니 바로 해결!
'''

import sys

N = int(sys.stdin.readline())

cnt = 0
greetings = set()
for _ in range(N):
    person = sys.stdin.readline().strip()
    if person == 'ENTER':
        greetings.clear()
    else:
        if person not in greetings:
            cnt += 1
            greetings.add(person)

print(cnt)