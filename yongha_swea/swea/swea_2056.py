T = int(input())

for tc in range(1, T+1):
    calendar = []

    #날짜 배열 받아오기
    arr = str(input())

    #년 떼어오기
    year = arr[0:4]

    #월 떼어오기
    month = arr[4:6]

    #일 떼어오기
    days = arr[6:8]
    
    #날짜 제한을 걸어주기 위한 딕셔너리
    days_lim = {'00' : 0,
                '01' : 31,
                '02' : 28,
                '03' : 31,
                '04' : 30,
                '05' : 31,
                '06' : 30,
                '07' : 31,
                '08' : 31,
                '09' : 30,
                '10' : 31,
                '11' : 30,
                '12' : 31,}

    if int(days) > days_lim[month]:
        ans = -1
    else:
        ans_list = [year, month, days]
        ans = '/'.join(ans_list)

    print(f'#{tc} {ans}')