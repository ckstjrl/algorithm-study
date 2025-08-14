#swea 5356. 의석이의 세로로 말해요 (D3)
T = int(input())

#각 문자열 길이가 다른 테스트케이스 
# AABCDD
# afzz
# 09121
# a8EWg6
# P5h3kx

for tc in range(1, T+1):

    arr = [(input()) for _ in range(5)]
    strlist = [] #문자열을 요소로 할 예정인 빈 리스트 생성

    for j in range(15): # 문자열 한 줄의 최대 길이를 범위로 설정
        for i in range(5):
            if j < len(arr[i]): #j값 인덱스 오류가 나지 않도록 각 문자열의 길이로 조건 설정
                strlist.append(arr[i][j])

    print(f"#{tc} {''.join(strlist)}")
