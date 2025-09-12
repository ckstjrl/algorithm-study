#boj2527 직사각형

T = 4

for tc in range(T):
    arr = list(map(int, input().split()))

    ans = ''

    #받은 배열을 기반으로 사각형 두 개 나눠주기
    square1 = arr[4:]
    square2 = arr[:4]

    #square1: left_bottom, left_top, right_bottom, right_top
    x1_l, y1_bot, x1_r, y1_top = square1

    # square2: left_bottom, left_top, right_bottom, right_top
    x2_l, y2_bot, x2_r, y2_top = square2

    # 관계는 접점 x, 점 접함, 변 접함, 일부 포함(겹침의 4가지 가능성)

    #접점 x 조건
    if x2_r < x1_l or x1_r < x2_l or y1_top < y2_bot or y2_top < y1_bot:
        ans = 'd'

    #접점 조건
    elif (x1_r == x2_l or x1_l == x2_r) and (y1_top == y2_bot or y2_top == y1_bot):
        ans = 'c'

    #변끼리 접하는 조건
    elif (x1_r == x2_l or x1_l == x2_r) and (y1_bot < y2_top and y1_top > y2_bot) or (y1_top == y2_bot or y1_bot == y2_top) and (x1_l < x2_r and x1_r > x2_l):
        ans = 'b'

    #일부가 포함되는 조건
    else:
        ans = 'a'

    print(ans)