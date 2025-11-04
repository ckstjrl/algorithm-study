# 5675 시침과 분침

#규칙성을 찾는 게 유효했던 문제, 6으로 나눠지느냐를 기준으로 나오는 각도인지 아닌지가 결정된다
#이 규칙만 찾으면 정말 간단했던 문제

while True:
    try:
        num = int(input())

        if num % 6 == 0:
            print('Y')
        else:
            print('N')

    except:
        break