"""
BOJ20438. 출석체크

[문제]
코로나 바이러스로 인해 H 대학은 비대면 강의를 실시하고 있다. 조교를 담당하게 된 지환이는 출석체크 방식을 바꾸려고 한다.
학생들은 접속 순서대로 3번부터 N + 2번까지 입장 번호를 받게 된다.
지환이가 한 학생에게 출석 코드를 보내게 되면, 해당 학생은 본인의 입장 번호의 배수인 학생들에게 출석 코드를 보내어 해당 강의의 출석을 할 수 있게끔 한다.
하지만, K명의 졸고 있는 학생들은 출석 코드를 제출하지 않고, 다른 학생들에게 보내지 않는다.
지환이는 무작위로 한 명의 학생에게 출석 코드를 보내는 행위를 Q번 반복한 뒤, 출석부 정리를 위해 특정 구간의 입장 번호를 받은 학생들 중에서 출석이 되지 않은 학생들의 수를 구하고 싶다.
많은 인원을 담당해서 바쁜 지환이를 위해 프로그램을 만들어주자!

[입력]
1번째 줄에 학생의 수 N, 졸고 있는 학생의 수 K, 지환이가 출석 코드를 보낼 학생의 수 Q, 주어질 구간의 수 M이 주어진다. (1 ≤ K, Q ≤ N ≤ 5,000, 1 ≤ M ≤ 50,000)
2번째 줄과 3번째 줄에 각각 K명의 졸고 있는 학생의 입장 번호들과 Q명의 출석 코드를 받을 학생의 입장 번호들이 주어진다.
4번째 줄부터 M개의 줄 동안 구간의 범위 S, E가 공백을 사이에 두고 주어진다. (3 ≤ S < E ≤ N + 2)

[출력]
M개의 줄에 걸쳐서 각 구간에 대해서 출석이 되지 않은 학생들의 수를 출력하라.
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

# 입장 번호가 s_num인 학생이 출석체크 방식에 따라 출석 코드를 보내는 함수
def send_attend_code(s_num, max_num):

    # 코드를 받은 학생이 졸고 있으면, 해당 학생은 코드를 보내지 않으므로 종료
    if s_num in dozing_offs:
        return
    
    # 코드를 받은 학생이 졸고 있지 않다면:
    k = 1   # k 1배부터 시작
    while True:     # 다음 과정을 반복한다.

        # 코드를 받은 학생 번호의 k배 번호를 가진 사람이 졸고 있다면, k를 1 증가시키고 pass
        if s_num * k in dozing_offs:
            k += 1
            continue

        # 코드를 받은 학생 번호의 k배 번호를 가진 사람은 모두 출석으로 표시
        if s_num * k <= max_num:
            not_attended[s_num * k] = False

        # k배 번호가 최대 숫자(N + 2)를 넘어가면 종료
        else:
            break

        # k 1 증가
        k += 1

# main
N, K, Q, M = map(int, input().split())  # N: 학생 수, K: 졸고 있는 학생 수, Q: 출석 코드를 보낼 학생 수, M: 구간의 수
dozing_offs = set(map(int, input().split()))    # 졸고 있는 학생들 K명의 번호를 'set'로 저장
attend_code_receivers = list(map(int, input().split())) # 출석 코드를 받을 학생들 Q명의 번호
not_attended = [True] * (N + 3) # 결석 여부 체크용 배열

# 출석 코드를 받은 학생들은 출석체크 방식에 따라 출석 코드를 보냄
for receiver in attend_code_receivers:
    send_attend_code(receiver, N + 2)

# 결석한 학생의 수를 누적합 배열 prefix_sum에 저장
# 누적합 배열에 저장하는 이유: 시간복잡도 감소!
not_attended_sum = 0
prefix_sum = [0] * (N + 3)
for s_num in range(3, N + 3):
    if not_attended[s_num]:
        not_attended_sum += 1
    prefix_sum[s_num] = not_attended_sum

# M개의 구간 입력을 받고, 각 구간에 존재하는 결석자 수를 누적합 배열을 통해 반환
for _ in range(M):
    S, E = map(int, input().split())
    print(prefix_sum[E] - prefix_sum[S - 1])
    