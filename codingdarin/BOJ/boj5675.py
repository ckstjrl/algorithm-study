# BOJ5675. 시침과 분침 (D1 / B1)

'''
분침은 분당 3도씩 갈 것이고, 
시침은 시간당 15도씩 갈 것임
'''
import sys
txt = sys.stdin

# 가능한 모든 앵글 넣기 위한 set
angles = set()
angles.add(180)  # 180도는 항상 가능

# 모든 앵글 경우의 수 구하기
for h in range(12):
    for m in range(60):
        cur_angle_diff = (abs(30*h - 6*m)) % 180
        angles.add(cur_angle_diff)

# 입력받은 앵글이 가능한 앵글인지 확인
for each in txt:    
    if int(each) in angles:
        print("Y")
    else:
        print("N")

    