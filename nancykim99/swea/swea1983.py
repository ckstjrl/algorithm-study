# 10개의 학점 : 
# 총점 = 중간고사 (35%) + 기말고사 (45%) + 과제 (20%)
# 각각의 평점은 같은 비율로 부여 가능
# K번째 학생의 학점을 출력
# N : 10의 배수 / 10 <= N <= 100
# K : 1<=K<=N

T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']


for tc in range(1, T+1):
    N, K = map(int, input().split())
    
    num_jump = N // 10

    idx = []
    students_score = []
    students_grade = []
    for i in range(N):
        mid, end, hw = map(int, input().split())
        score = (mid*0.35) + (end*0.45) + (hw*0.2)
        students_score.append((score, i+1)) # 튜플로 저장
        if i % num_jump == 0:
            idx.append(i)
    
    idx.append(N)
    students_score.sort(reverse=True, key=lambda x: x[0]) # 이렇게 하면 튜플의 값에 따라 sorting 가능

    students_per_grade = N // 10
    
    for i, (score, student_num) in enumerate(students_score): # 인덱스, 튜플 <- enumerate
        if student_num == K: # 학생 번호가 K일때
            grade_index = i // students_per_grade # i 나누기 학점별 학생 비율의 몫 == grade리스트의 인덱스 
            print(f'#{tc} {grade[grade_index]}')
            break