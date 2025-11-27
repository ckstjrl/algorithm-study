# 10162 전자레인지 / D1
'''
A : 5분 = 300초, B : 1분 = 60초, C : 10초
음식마다 시간초 T 제공
A+B+C = T 무조건 최소 횟수
T를 정확하게 맞출 수 없는 경우 -1 출력
누르지 않은 버튼은 0으로 출력
'''
import sys
T = int(sys.stdin.readline())
A = 300
B = 60
C = 10


if T % C != 0:
    print(-1)

else:
    a = T//A
    T %= A

    b = T // B
    T %= B

    c = T // C

    print(f'{a} {b} {c}')
