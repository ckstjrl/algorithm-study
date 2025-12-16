# BOJ 1244. 스위치 켜고 끄기 / D2
'''
1부터 연속적으로 번호가 붙어있는 스위치들이 있다. 스위치는 켜져 있거나 꺼져있는 상태이다.
<그림 1>에 스위치 8개의 상태가 표시되어 있다.
‘1’은 스위치가 켜져 있음을, ‘0’은 꺼져 있음을 나타낸다.
그리고 학생 몇 명을 뽑아서, 학생들에게 1 이상이고 스위치 개수 이하인 자연수를 하나씩 나누어주었다.
학생들은 자신의 성별과 받은 수에 따라 아래와 같은 방식으로 스위치를 조작하게 된다.

남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다.
<그림 1>과 같은 상태에서 남학생이 3을 받았다면, 이 학생은 <그림 2>와 같이 3번, 6번 스위치의 상태를 바꾼다.

여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서,
그 구간에 속한 스위치의 상태를 모두 바꾼다. 이때 구간에 속한 스위치 개수는 항상 홀수가 된다.
'''
import sys
N = int(sys.stdin.readline()) # 전구 개수
light = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline()) # 학생 수
for _ in range(M):
    S, num_ = map(int, sys.stdin.readline().split())
    num = num_ -1                               # 남학생의 경우 인덱스와 카드의 숫자가 다른 부분을 조정을 조건문에서 진행
                                                # 여학생의 경우 인덱스와 카드 숫자의 차이를 미리 잡고 들어가면 편함
    if S == 1:                                  # 남학생 case
        for time in range(1, N+1):              # 배수를 구해주기 위해 곱해주는 값, card 숫자가 1인 경우를 고려하여 범위 설정
            if num_*time<=N:                    # 배수가 부조건 N 안에 있어야함
                if light[num_*time-1] == 1:     # num_*time 번째 전구는 인덱스 값으로 num_*time - 1 이다
                    light[num_*time-1] = 0
                else:
                    light[num_*time-1] = 1

    else:
        for i in range(1, N):
            # num을 중심으로 같은 칸 차이가 존재한 곳 끼리 비교
            # 만약 다른 경우가 존재한다면 그 순간 부터 끝이므로 else: break 사용
            if 0 <= num-i < N and 0 <= num+i < N and light[num-i] == light[num + i]:
                if light[num-i] == 1 :
                    light[num-i] = 0
                    light[num+i] = 0
                else:
                    light[num-i] = 1
                    light[num+i] = 1
            else:
                break
        if light[num] == 1:
            light[num] = 0
        else:
            light[num] = 1

for a in range(0, len(light), 20):          # 20개씩 슬라이싱하는 방식을 활용하여 20개씩 끊어서 여러줄로 표현하게 만듦
    one_line = light[a:a+20]
    print(' '.join(map(str, one_line)))

'''
남학생의 경우 인덱스와 카드의 숫자가 다른 부분을 조정을 조건문에서 진행
여학생의 경우 인덱스와 카드 숫자의 차이를 미리 잡고 들어가면 편함
남학생 case
배수를 구해주기 위해 곱해주는 값, card 숫자가 1인 경우를 고려하여 범위 설정
배수가 부조건 N 안에 있어야함
num_*time 번째 전구는 인덱스 값으로 num_*time - 1 이다
여학생 case
num을 중심으로 같은 칸 차이가 존재한 곳 끼리 비교
만약 다른 경우가 존재한다면 그 순간 부터 끝이므로 else: break 사용
20개씩 슬라이싱하는 방식을 활용하여 20개씩 끊어서 여러줄로 출력하게 만듦
'''