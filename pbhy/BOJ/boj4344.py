# 4344. 평균은 넘겠지
'''
첫 줄에 테스트 케이스 개수 C
둘쨰 줄에 학생 수 N, N명의 점수
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력
'''
C = int(input())
for tc in range(C):
    arr = list(map(int, input().split()))
    sum_v = 0
    avg_v = 0
    cnt = 0
    for i in arr[1:]:
        sum_v += i
    avg_v = sum_v / arr[0]

    for score in arr[1:]:
        if avg_v < score:
            cnt += 1    # 평균 이상인 학생의 수
    rate = (cnt/arr[0]) * 100 # 평균 이상인 학생의 비율
    print(f'{rate:.3f}%')