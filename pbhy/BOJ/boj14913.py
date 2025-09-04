# 14913. 등차수열에서 항 번호 찾기
'''
등차수열에서 인접한 두 수의 차이를 공차라고 한다.
첫 항 a와 공차 d로 만든 등차수열에서 주어진 k가 몇 번째 항인지 찾아서 출력하는 프로그램을 작성하시오

a+(n-1)d == k일 때 n을 구하기.
d = 0인 경우 / 아닌 경우 나누기
'''
a, d, k = map(int, input().split())

if d == 0:  # d == 0인 경우
    if k == a:
        print(1)
    else:
        print('X')
else:
    if (k - a) % d == 0:
        n = (k - a) // d + 1
        if n >= 1:
            print(n)
        else:
            print('X')  # n은 1 이상이어야 함
    else:
        print('X')