# 11723. 집합
'''
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

- add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
- remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
- check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
- toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
- all: S를 {1, 2, ..., 20} 으로 바꾼다.
- empty: S를 공집합으로 바꾼다.

[입력]
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

[출력]
check 연산이 주어질때마다, 결과를 출력한다.

연산 종류별로 어떤 함수를 사용할지 먼저 결정
집합 - >`set` 사용
- 리스트에 비해 시간이 빠름
입력에 전부 숫자가 나오는 게 아니기 때문에 (all, empty) 하나의 변수로 받은 다음 나눠야 함.
출력은 check만 함
'''
import sys
input = sys.stdin.readline
s = set()
m = int(input())
for _ in range(m):
    m_val = input().split()
    if len(m_val) == 1:
        char = m_val[0]
    else:
        char, x = m_val[0], int(m_val[1])
    if char == 'add':
        s.add(x)
    if char == 'remove':
        s.discard(x)
    if char == 'check':
        if x in s:
            print(1)
        else:
            print(0)
    if char == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    if char == 'all':
        s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
    if char == 'empty':
        s.clear()