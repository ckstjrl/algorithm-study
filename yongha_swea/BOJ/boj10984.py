T = int(input())

for tc in range(T):
    total_credit = 0
    total_score = 0
    
    # 둘째줄: 각 학기의 과목 수
    N = int(input())
    
    for sub in range(N):
        # 학점, 성적
        C, G = map(float, input().split())
        total_credit += C
        total_score += C * G  # 학점 * 성적으로 가중평균 계산
    
    avg_score = total_score / total_credit
    
    print(f'{int(total_credit)} {avg_score:.1f}')