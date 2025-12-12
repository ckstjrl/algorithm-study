'''
[문제]
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.

[입력]
첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.
둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.

[출력]
check 연산이 주어질때마다, 결과를 출력한다.
'''

S = set()                 # 공집합 S 초기화 하기
M = int(input())          # 명령 개수 입력받기

for _ in range(M):
    parts = input().split()   # 명령과 인자 분리하기
    cmd = parts[0]            # 명령어 추출하기

    if cmd == 'add':
        x = int(parts[1])     # 추가할 원소 x 읽기
        S.add(x)              # 원소 추가하기

    elif cmd == 'remove':
        x = int(parts[1])     # 제거할 원소 x 읽기
        S.discard(x)          # 원소 제거하기(없으면 무시하기)

    elif cmd == 'check':
        x = int(parts[1])     # 확인할 원소 x 읽기
        print(1 if x in S else 0)  # 포함 여부 출력하기

    elif cmd == 'toggle':
        x = int(parts[1])     # 토글할 원소 x 읽기
        if x in S:
            S.remove(x)       # 포함 시 제거하기
        else:
            S.add(x)          # 미포함 시 추가하기

    elif cmd == 'all':
        S = set(range(1, 21)) # 전체 집합으로 설정하기

    else:  # 'empty'
        S.clear()             # 공집합으로 비우기
