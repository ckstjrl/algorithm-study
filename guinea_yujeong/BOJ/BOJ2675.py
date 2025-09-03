'''
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

입력
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다.
S의 길이는 적어도 1이며, 20글자를 넘지 않는다.

출력
각 테스트 케이스에 대해 P를 출력한다.

'''
T=int(input())
for tc in range(1, T+1):   # 테스트 케이스 반복
    R, S = input().split()  # Q1. R이랑 S 입력값 받기 근데 R은 숫자고 S는 문자열인데 한번에 map으로 받을 수 있나
    R = int(R)

    ans = ''
    for i in S: # for문 돌리기
        ans += i * R
    print(ans)

    '''
    memo 
    Q1. R이랑 S 입력값 받기 근데 R은 숫자고 S는 문자열인데 한번에 map으로 받을 수 있나
     -> 숫자와 글자는 한 번에 map으로 받을 수 없음. 따라서 그냥 input.split 만 받고 따로 int로 정리하기 
    
    for 문 '반복범위'를 자꾸 헷갈려 함 
    for i in S : -> for i in 'ABC' 
    i * R -> 'A' * R(숫자) / 'B' * R / 'C' * R   -> 따로 리스트화 할 필요 x
    for문의 결과를 ans에 입력하기  
    '''