# BOJ 20438. 출석체크 / D2
'''
문제
코로나 바이러스로 인해 H 대학은 비대면 강의를 실시하고 있다. 조교를 담당하게 된 지환이는 출석체크 방식을 바꾸려고 한다.

학생들은 접속 순서대로 3번부터 N + 2번까지 입장 번호를 받게 된다.

지환이가 한 학생에게 출석 코드를 보내게 되면, 해당 학생은 본인의 입장 번호의 배수인 학생들에게 출석 코드를 보내어 해당 강의의 출석을 할 수 있게끔 한다.

하지만, K명의 졸고 있는 학생들은 출석 코드를 제출하지 않고, 다른 학생들에게 보내지 않는다.

지환이는 무작위로 한 명의 학생에게 출석 코드를 보내는 행위를 Q번 반복한 뒤, 출석부 정리를 위해 특정 구간의 입장 번호를 받은 학생들 중에서 출석이 되지 않은 학생들의 수를 구하고 싶다.

많은 인원을 담당해서 바쁜 지환이를 위해 프로그램을 만들어주자!

입력
1번째 줄에 학생의 수 N, 졸고 있는 학생의 수 K, 지환이가 출석 코드를 보낼 학생의 수 Q, 주어질 구간의 수 M이 주어진다. (1 ≤ K, Q ≤ N ≤ 5,000, 1 ≤ M ≤ 50,000)

2번째 줄과 3번째 줄에 각각 K명의 졸고 있는 학생의 입장 번호들과 Q명의 출석 코드를 받을 학생의 입장 번호들이 주어진다.

4번째 줄부터 M개의 줄 동안 구간의 범위 S, E가 공백을 사이에 두고 주어진다. (3 ≤ S < E ≤ N + 2)

출력
M개의 줄에 걸쳐서 각 구간에 대해서 출석이 되지 않은 학생들의 수를 출력하라.
'''
import sys

input = sys.stdin.readline

N, K, Q, M = map(int, input().split())
sleep = list(map(int, input().split())) # 자는 학색
start_s = list(map(int, input().split())) # 출석 코드 먼저 받은 학생

check_student = [0]*(N+3) # 출석한 학생은 1 안한 학생은 0
for s in start_s: 
    if s in sleep: # 만약 출석코드 시작하는 학생이 자는 경우 넘어감
        continue
    for i in range(s, N+3, s): # 자신의 번호의 배수이므로 자신 번호만큼 뛰어서 체크
        if i in sleep: # 자면 넘어감
            continue
        check_student[i] = 1 # 출석 체크

prefix_sum = [0]*(N+3) # 알고리즘 확인해보니 누적합이 있어서 누적합으로 계산
for j in range(3, N+3): # 3번부터 누적합 시작
    no_check = 0 # 초기값
    if check_student[j] == 0: # 만약 출석 안했다면
        no_check = 1 # 출석안함 1로 변경하고 밑에서 더해줌
    prefix_sum[j] = prefix_sum[j-1] + no_check

for _ in range(M):
    S, E = map(int, input().split())
    print(prefix_sum[E]-prefix_sum[S-1]) # 누적합 빼기로 구함


# 틀렸습니다.... 왜? 왜 틀린거지? 시간 초과 아닌가?
'''
cnt = 0
for p in part:
    for i in range(p[0], p[1]+1):
        if check_student[i] == 0:
            cnt += 1
print(cnt)
'''