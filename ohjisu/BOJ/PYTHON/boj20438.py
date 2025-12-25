'''
# [Silver II] 출석체크 - 20438

[문제 링크](https://www.acmicpc.net/problem/20438)

### 성능 요약

메모리: 118196 KB, 시간: 512 ms

### 분류

누적 합

### 제출 일자

2025년 11월 18일 23:59:56

### 문제 설명

<p>코로나 바이러스로 인해 H 대학은 비대면 강의를 실시하고 있다. 조교를 담당하게 된 지환이는 출석체크 방식을 바꾸려고 한다.</p>

<p>학생들은 접속 순서대로 3번부터 N + 2번까지 입장 번호를 받게 된다.</p>

<p>지환이가 한 학생에게 출석 코드를 보내게 되면, 해당 학생은 본인의 입장 번호의 배수인 학생들에게 출석 코드를 보내어 해당 강의의 출석을 할 수 있게끔 한다.</p>

<p>하지만, K명의 졸고 있는 학생들은 출석 코드를 제출하지 않고, 다른 학생들에게 보내지 않는다.</p>

<p>지환이는 무작위로 한 명의 학생에게 출석 코드를 보내는 행위를 Q번 반복한 뒤, 출석부 정리를 위해 특정 구간의 입장 번호를 받은 학생들 중에서 출석이 되지 않은 학생들의 수를 구하고 싶다.</p>

<p>많은 인원을 담당해서 바쁜 지환이를 위해 프로그램을 만들어주자!</p>

### 입력

 <p>1번째 줄에 학생의 수 N, 졸고 있는 학생의 수 K, 지환이가 출석 코드를 보낼 학생의 수 Q, 주어질 구간의 수 M이 주어진다. (1 ≤ K, Q ≤ N ≤ 5,000, 1 ≤ M ≤ 50,000)</p>

<p>2번째 줄과 3번째 줄에 각각 K명의 졸고 있는 학생의 입장 번호들과 Q명의 출석 코드를 받을 학생의 입장 번호들이 주어진다.</p>

<p>4번째 줄부터 M개의 줄 동안 구간의 범위 S, E가 공백을 사이에 두고 주어진다. (3 ≤ S < E ≤ N + 2)</p>

### 출력

 <p>M개의 줄에 걸쳐서 각 구간에 대해서 출석이 되지 않은 학생들의 수를 출력하라.</p>

'''
# 초기설정
import sys
input = lambda :sys.stdin.readline().rstrip()

N, K, Q, M = map(int, input().split())
sleep_students = set(map(int, input().split()))
code_students = set(map(int, input().split()))

# 출석표 - 일단 출석했다 치고 시작
checked = [1] * (N + 3)

for code_student in code_students:
    # 코드 받은 애가 조는 애 중에 있으면 넘어가기
    if code_student in sleep_students:
        continue
    # 안졸면 자기 배수에 해당하는 데에 체크
    for i in range(code_student, N + 3, code_student):
        # 배수가 조는지 확인
        if i in sleep_students:
            continue
        checked[i] = 0

for _ in range(M):
    S, E = map(int, input().split())
    print(sum(checked[S:E + 1]))