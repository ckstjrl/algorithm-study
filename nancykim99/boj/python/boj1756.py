'''
BOJ1756 : 피자 굽기 (G5)

해결 방법 : 
1. 오븐에서 다음 숫자가 더 큰 경우, 어차피 안 들어가기 때문에, 작은 숫자로 만들기
    - 5, 6이면 어차피 6에는 5만 들어가니까 5만 넣기
2. 오븐을 아래에서 위로 올라가면서, 만약 0보다 작은 경우, 못 채우는 거니까 0
3. 오븐 최상단은 1이기에 마지막으로 넣은 도우 위치에 +1하기

메모 : 
그냥 구현했더니 시간 초과... 젤 싫어
'''

import sys
input = sys.stdin.readline

o, n = map(int, input().split())
oven = list(map(int, input().split()))
doughs = list(map(int, input().split()))
is_filled = [0] * (o)

for i in range(1, o):
    if oven[i] > oven[i-1]:
        oven[i] = oven[i-1]

slide = o-1
last = -1

for dough in doughs:
    while slide >= 0 and oven[slide] < dough:
        slide -= 1
    if slide < 0:
        print(0)
        sys.exit()
    last = slide
    slide -= 1

print(last+1)