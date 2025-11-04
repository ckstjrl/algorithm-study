#BOJ2160 그림 비교

#입력 받을 그림의 수
num = int(input())

# 그림 크기: ver = 5, hor = 7
picture = []

# 5줄, 그림 1개,에 맞춰서 input 받고 각각을 그림으로 두기
# 기존의 사용한 맵 방법은 작동을 하지 않아서 다른 방법을 찾아볼 필요가 있었음
for i in range(num):
    picture.append([input().strip() for _ in range(5)])

# 그림끼리 비교, 그림 수가 몇 개 나올지 모르기 때문에 함수화

def check_diff(pic1, pic2):

    #변수 생성 및 초기화
    diff = 0

    # 세로 받기
    for i in range(5):
        # 가로 받기
        for j in range(7):
            if pic1[i][j] != pic2[i][j]:
                diff += 1
    return diff

# 최소 차이가 될 때 그 값을 받을 변수 찾기
min_diff = 1000000
min_diff_i = 0 
min_diff_j = 0

# 입력 받은 그림을 모두 비교하기
for i in range(num):
    for j in range(i + 1, num):
        #그림 비교
        diff = check_diff(picture[i], picture[j])
        
        if diff < min_diff:
            min_diff = diff
            #그림은 1번부터 시작이기 때문에 index넘버에 +1
            min_diff_i = i + 1
            min_diff_j = j + 1

print(min_diff_i, min_diff_j)