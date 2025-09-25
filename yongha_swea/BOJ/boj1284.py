# 각 숫자 사이 여백 1cm
# 1: 2cm 너비 차지, 0: 4cm 너비 차지, 나머지: 모두 3cm 너비 차지
# 호수판의 경계와 숫자 사이 여백 1cm

#호수 경계, 숫자 여백은 반드시 2cm가 된다 (첫번째 숫자 왼쪽 1cm, 마지막 숫자 오른쪽 1cm)

#숫자 사이 여백: len(num) - 1 , 숫자가 3개라면 숫자 사이 여백은 2cm

num = 10000

dist = 0

while num != [0]:
    dist = 0

    num = list(map(int, input().rstrip()))

    #숫자에 따른 값 더해주기
    for i in num:
        if i == 1:
            dist += 2
        elif i == 0:
            dist += 4
        else:
            dist += 3

    #양 옆 거리 2 + 수 사이 거리 (len(num) - 1) == len(num) + 1
    dist = dist + 2 + (len(num) - 1)
    
    if num != [0]:
        print(dist)