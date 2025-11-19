'''boj5052 전화번호 목록

전화번호 목록이 주어진다. 
이때, 이 목록이 일관성이 있는지 없는지를 구하는 프로그램을 작성하시오.

전화번호 목록이 일관성을 유지하려면, 한 번호가 다른 번호의 접두어인 경우가 없어야 한다.

예를 들어, 전화번호 목록이 아래와 같은 경우를 생각해보자

긴급전화: 911
상근: 97 625 999
선영: 91 12 54 26
이 경우에 선영이에게 전화를 걸 수 있는 방법이 없다. 
전화기를 들고 선영이 번호의 처음 세 자리를 누르는 순간 바로 긴급전화가 걸리기 때문이다. 
따라서, 이 목록은 일관성이 없는 목록이다.

입력
첫째 줄에 테스트 케이스의 개수 t가 주어진다. 
(1 ≤ t ≤ 50) 각 테스트 케이스의 첫째 줄에는 전화번호의 수 n이 주어진다. 
(1 ≤ n ≤ 10000) 다음 n개의 줄에는 목록에 포함되어 있는 전화번호가 하나씩 주어진다. 전화번호의 길이는 길어야 10자리이며, 목록에 있는 두 전화번호가 같은 경우는 없다.
'''
# 문자열로 받아서 리스트 슬라이싱으로 비교하기
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    N = int(input()) #전화번호의 수 N

    number = [input().strip() for _ in range(N)]
    # print(number)

    ans = 'YES'

    for i in range(N-1):
        for j in range(i+1, N):
            #첫 글자 다르면 스킵
            #이 부분 없으면 시간초과남
            if number[i][0] != number[j][0]:
                continue

            # 두 전화번호 중 더 긴 쪽
            if len(number[i]) <= len(number[j]):
                # 첫부분이 같은지 확인
                if number[j][:len(number[i])] == number[i]:
                    ans = 'NO'
                    break

            if len(number[i]) >= len(number[j]):
                if number[i][:len(number[j])] == number[j]:
                    ans = 'NO'
                    break
        
        if ans == 'NO':
            break
            
    print(ans)