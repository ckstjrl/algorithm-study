# 2547. 사탕 선생 고창영
'''
N명의 학생이 가져온 사탕을 공평하게 나누자.

[입력]
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 빈 줄로 구분.
테스트 케이스의 첫째 줄에 학생의 수 N이 주어진다.
다음 N개의 줄에는 각 학생들이 가져온 사탕의 수가 주어진다.

T 다음 빈 줄 처리 : while문에서 사탕 수 입력받고 빈 줄이 아니면 입력받은 수로 할 수 있음
'''
T = int(input())
for _ in range(1, T+1):
    while True:
        n = input()
        if n != '':   # 빈 줄이 아닌 n 구하기
            n = int(n)
            break
    cnt = 0
    for _ in range(n):
        cnt += int(input()) # n 안에서만 도니까 input도 n개 받고 for문 나감
    if cnt % n == 0:
        print('YES')
    else:
        print('NO')