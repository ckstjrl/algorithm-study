T = int(input())
a = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
for tc in range(1, T+1):
    N = str(input())
    yy = N[0:4]   #연도만 뽑아오기
    mm = N[4:6]
    dd = N[6:8]


    if 0 < int(mm) < 13 and 0 < int(dd) <= a[int(mm)]:
        ans = yy + '/' + mm + '/' + dd  #'/' 문자열로 구분
    else:      #날짜가 유효하지 않은 경우 -1을 출력 
        ans = '-1'
    
    print(f'#{tc} {ans}')