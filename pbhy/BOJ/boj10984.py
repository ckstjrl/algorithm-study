# 10984. 내 학점을 구해줘
'''
[입력]
첫 번째 줄에 학기의 수 T가 주어진다.
두 번째 줄부터 T개 학기에 대한 정보가 주어진다.
각 학기에 대한 정보는 다음과 같이 구성되어 있다.
첫 번째 줄에 들었던 과목의 수 N이 주어지고, 다음 N개 줄에 걸쳐서 N개 과목들의 학점 C와 성적 G가 주어진다.
G는 {0, 0.7, 1, 1.3, 1.7, 2, 2.3, 2.7, 3, 3.3, 3.7, 4, 4.3} 중 하나이며 소수 부분은 최대 한 자리까지 주어진다.

[출력]
각 학기에 대해 근우의 총 학점과 평점(GPA)을 출력한다.

cnt = 학기 별 학점 더하기
gpa = 학기 별 (학점(c) * 성적(g)) / 학점 더한 수
'''
t = int(input())
for tc in range(t):
    n = int(input())
    cnt = 0
    score = 0
    for i in range(n):
        c, g = input().split()
        c = int(c)
        g = float(g)
        cnt += c
        score += c*g
    gpa = score / cnt
    print(f'{cnt} {gpa:.1f}')