#boj2755 이번학기 평점은 몇점?

subs = int(input())

sub_info = [list(map(str, input().split())) for _ in range(subs)]

#딕트를 통해서 평가에 따른 점수 받기
score_convert ={
    'A+' : 4.3,
    'A0' : 4.0,
    'A-' : 3.7,
    'B+' : 3.3,
    'B0' : 3.0,
    'B-' : 2.7,
    'C+' : 2.3,
    'C0' : 2.0,
    'C-' : 1.7,
    'D+' : 1.3,
    'D0' : 1.0,
    'D-' : 0.7,
    'F' : 0.0,
}

count = 0
score = 0

for sub in sub_info:
    count += int(sub[1])
    score = score + (int(sub[1]) * score_convert[sub[2]])

final_score = score / count

# 부동 소수점으로 인해 반올림이 정상 작동하지 않는걸 해결하기 위해 아래와 같이 추가
# 1e-9라는 매우 작은 수를 더해서 3.275가 근사값으로 인식되는 게 아니라 정상적으로 인식될 수 있도록 변환
print(f"{final_score + 1e-9:.2f}")

