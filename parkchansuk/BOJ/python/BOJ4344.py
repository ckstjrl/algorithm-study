# BOJ 4344. 평균은 넘겠지
'''
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
정답과 출력값의 절대/상대 오차는 10^-3이하이면 정답이다.
'''
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    arr = list(map(int, sys.stdin.readline().split())) # 전부다 list로 받음
    N = arr.pop(0) # N을 pop해서 아에 뽑아버림
    aver = sum(arr) / N # 점수 평균 구하기

    cnt = 0 # 평균 넘는 학생 수 계산
    for i in arr:
        if i > aver:
            cnt += 1

    print(f'{round((cnt/N)*100, 3)}%') # 평균넘는 학생수 비율 소숫점 3째자리까지 구하기

# round(숫자, 소숫점 자리수)를 사용하여 계산