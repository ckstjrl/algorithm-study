"""
2056. 연월일 달력 D1

"YYYY/MM/DD"형식으로 출력하고,

날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며

일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.

"""



T = int(input())
for tc in range(1, T+1) :
    result = ''
    date = input()
    # 출력할 형식 맞추기
    result = date[:4] + '/' + date[4:6] + '/' + date[6:]
    # 조건을 넣을 dictionary 만들기
    condition = {}
    # month 리스트 만들기
    month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    # update dictionary
    for key in month :
        if int(key) % 2 == 1 :                  # 홀수 달일 때, 1~31
            condition.update({key: range(1, 32)}) 
        elif key == '02' :                      # 2월은 1~28
            condition.update({key: range(1, 29)})
        else :                                  # 짝수 달일 때, 1~30
            condition.update({key: range(1, 31)})
    if  (date[4:6] not in month)  or (int(date[6:]) not in condition[date[4:6]]) : # 조건에 해당하지 않을 때는
        result = -1                                                                # result에 -1 할당
    print(f'#{tc} {result}')



