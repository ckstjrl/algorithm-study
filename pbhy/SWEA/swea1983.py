# 1983. 조교의 성적 매기기

'''
총점 : 중간(35)+기말(45)+과제(20)
총점 높은 순서대로 평점 부여
N/10에게 동일한 평점 부여 -> 10명이면 각 평점 당 1명씩, 20명이면 2명씩
K번째 학생의 학점을 출력하자
총점이 동일한 경우는 입력으로 주어지지 않는다 -> 총점 동점이 없다
'''

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    score_total = []

    for i in range(N):
        mid, fin, hw = map(int, input().split())
        score = (mid * 0.35) + (fin * 0.45) + (hw * 0.2)
        score_total.append(score)

    # K번째의 점수
    score_k = score_total[K - 1]

    # K보다 높은 점수의 학생 수 세기
    higher_cnt = 0
    for j in score_total:
        if j > score_k:
            higher_cnt += 1
    # score.sort(reverse=True)

    # 등수 -> 학점
    rank = higher_cnt  # 0등부터 시작
    grades_inx = rank // (N // 10)  # 등급의 구간사이즈를 나눠서 구간 별 숫서를 함
    result = grades[grades_inx]

    print(f'#{tc} {result}')