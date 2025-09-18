"""
BOJ5052. 전화번호 목록

[문제]
전화번호 목록이 주어진다. 이때, 이 목록이 일관성이 있는지 없는지를 구하는 프로그램을 작성하시오.
전화번호 목록이 일관성을 유지하려면, 한 번호가 다른 번호의 접두어인 경우가 없어야 한다.
예를 들어, 전화번호 목록이 아래와 같은 경우를 생각해보자

긴급전화: 911
상근: 97 625 999
선영: 91 12 54 26
이 경우에 선영이에게 전화를 걸 수 있는 방법이 없다. 전화기를 들고 선영이 번호의 처음 세 자리를 누르는 순간 바로 긴급전화가 걸리기 때문이다. 따라서, 이 목록은 일관성이 없는 목록이다.

[입력]
첫째 줄에 테스트 케이스의 개수 t가 주어진다. (1 ≤ t ≤ 50) 각 테스트 케이스의 첫째 줄에는 전화번호의 수 n이 주어진다. (1 ≤ n ≤ 10000) 다음 n개의 줄에는 목록에 포함되어 있는 전화번호가 하나씩 주어진다. 전화번호의 길이는 길어야 10자리이며, 목록에 있는 두 전화번호가 같은 경우는 없다.

[출력]
각 테스트 케이스에 대해서, 일관성 있는 목록인 경우에는 YES, 아닌 경우에는 NO를 출력한다.
"""
import sys
input = sys.stdin.readline

def is_consistent(phone_numbers):   # 전화번호부 목록이 일관성 있는지 검사하는 함수
    phone_numbers.sort()    # .sort()를 이용하여 전화번호부 목록을 사전순 정렬
    for i in range(len(phone_numbers) - 1): # 전화번호부를 순회하면서, 사전순으로 가장 앞인 전화번호 하나부터 사전 순서상 그 다음인 전화번호랑 비교
        if phone_numbers[i] == phone_numbers[i+1][:len(phone_numbers[i])]:  # 앞의 전화번호의 길이만큼만 뒤의 전화번호 길이랑 비교해서 둘이 같으면, 앞의 전화번호가 뒤의 전화번호의 접두어가 되니까
            return False    # False 반환하고 검사 종료
    return True # 검사를 전부 통과하면 True

# main
t = int(input())    # 테스트 케이스 개수
for tc in range(1, t + 1):
    n = int(input())    # 전화번호의 수 n
    phone_numbers = [input().strip() for _ in range(n)] # 개행 문자 제거하고 문자열 형태로 숫자 저장
    print("YES" if is_consistent(phone_numbers) else "NO")  # 전화번호부 목록이 일관성 있으면 YES, 없으면 NO 출력

"""
# 실패 코드(시간 초과)
# 이 코드는 모든 전화번호 쌍을 길이순 정렬한 다음, 길이가 짧은 것부터 그 이후 전화번호들이랑 하나하나 쭉 비교하는 구조라서,
# 최악의 경우 시간복잡도가 n * n * L = 10000 * 10000 * 10 = 10^8 -> 이렇게 나오기 때문에 TLE
# 시간복잡도를 줄이기 위한 힌트를 얻었더니 -> 사전순 정렬하라는 게 힌트였음
# '진짜 사전순 정렬하면 어떻게 되지?' -> '생각해보니 숫자가 안겹치면 자동으로 일관성이 없어서 그냥 다음꺼랑만 비교하면 됨'을 확인하고 풀어냄
# 직관에 의존하지 말고, 언제 일관성이 없어지는지 문제를 일고 잘 판단하자
# 그리고 아직 초보라 연산량 줄이는 사고가 어렵긴하다. 스스로 연산량 줄이는 연습을 해봐야할듯

import sys
input = sys.stdin.readline

def is_consistent(phone_numbers):

    phone_numbers.sort(key=lambda x: len(x))

    for i in range(n):
        for j in range(i + 1, n):
            length = len(phone_numbers[i])
            if phone_numbers[i] == phone_numbers[j][:length]:
                return False

    return True

# main
t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    phone_numbers = []
    for _ in range(n):
        phone_number = input().rstrip()
        phone_numbers.append(phone_number)
    print('YES' if is_consistent(phone_numbers) else 'NO')
"""
