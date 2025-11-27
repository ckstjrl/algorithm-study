"""
BOJ1759. 암호 만들기

[문제]
바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은, 702호에 새로운 보안 시스템을 설치하기로 하였다. 이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.
암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다. 또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다. 즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.
새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 이 알파벳을 입수한 민식, 영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 두 정수 L, C가 주어진다. (3 ≤ L ≤ C ≤ 15) 다음 줄에는 C개의 문자들이 공백으로 구분되어 주어진다. 주어지는 문자들은 알파벳 소문자이며, 중복되는 것은 없다.

[출력]
각 줄에 하나씩, 사전식으로 가능성 있는 암호를 모두 출력한다.
"""
# 내가 작성한 코드
import sys
input = lambda: sys.stdin.readline().rstrip()

def combination(i, start, n, k):    # 조합 nCk를 생성하는 재귀함수(수업시간에 배웠던거)

    # 현재 조합이 원하는 길이 k와 같다면 조건 체크
    if i == k:
        if check_condition(selected):  # 조건(모음 1개 이상, 자음 2개 이상)을 만족하는지 확인
            print("".join(selected))   # 조건 만족하면 암호 출력
        return

    # start부터 n까지 반복하면서 조합 생성
    for j in range(start, n):
        selected.append(chars[j])         # 문자 선택
        combination(i + 1, j + 1, n, k)  # 다음 문자 선택 (재귀 호출)
        selected.pop()                    # 선택 취소 (백트래킹)

def check_condition(selected):  # 조합이 조건을 만족하는지를 확인하는 함수
    vowel_cnt = sum(ch in vowels for ch in selected)  # 모음 개수 세기
    consonant_cnt = len(selected) - vowel_cnt         # 자음 개수는 selected 문자 개수에서 모음 개수를 빼서 계산
    return vowel_cnt >= 1 and consonant_cnt >= 2      # 조건: 모음 ≥1, 자음 ≥2

# main
L, C = map(int, input().split())    # L: 암호 길이, C: 주어진 문자 수
chars = sorted(list(input().split()))   # 입력 문자 정렬 (사전 순 출력 위해)
vowels = 'aeiou'
selected = []   # 현재 선택된 문자를 저장할 리스트
combination(0, 0, C, L) # 조합 생성 시작

"""
# 추가 학습 : 가지치기 조건을 추가한 version
# can_satisfy_condition 함수를 추가해서 가능성이 없는 조합은 가지치기로 연산량을 줄였다.(오히려 늘은거 같기도...)
# 미래에 조건 만족하는지 안하는지 미리 체크해서 가지치기하는 내용을 수업시간에 들었던 기억이 나서 어렴풋한 기억으로 따라해봄
# 지금은 시간이 오히려 88ms로 길게 나오지만...입력이 커질수록 연산량 줄이는데 도움 될듯?

import sys
input = lambda: sys.stdin.readline().rstrip()

def combination(i, start, n, k):
    if i == k:
        if check_condition(selected):
            print("".join(selected))
        return

    # 현재 상태에서 조건을 만족할 수 있는지 미리 확인 (가지치기)
    if not can_satisfy_condition(selected, k - i, chars[start:]):   # k - i : 더 뽑아야 할 문자 개수, chars[start:] : 앞으로 선택할 후보 문자들
        return

    for j in range(start, n):
        selected.append(chars[j])         
        combination(i + 1, j + 1, n, k)  
        selected.pop()
        
def check_condition(selected):
    vowel_cnt = sum(ch in vowels for ch in selected)
    consonant_cnt = len(selected) - vowel_cnt
    return vowel_cnt >= 1 and consonant_cnt >= 2

def can_satisfy_condition(selected, remaining, future_chars):    # 남은 문자들을 체크하여 앞으로 조건을 만족시킬 수 있는 가능성이 있는지 검사하는 함수

    vowel_cnt = sum(ch in vowels for ch in selected) # 현재까지 selected의 모음 개수
    consonant_cnt = len(selected) - vowel_cnt    # 현재까지의 selected의 자음 개수

    future_vowels = vowel_cnt + sum(ch in vowels for ch in future_chars)    # future_vowels = 앞으로 확보 가능한 최대 모음 수
    future_consonants = consonant_cnt + (len(future_chars) - sum(ch in vowels for ch in future_chars))  # future_consonants = 앞으로 확보 가능한 최대 자음 수

    # 미래에도 조건 만족 불가능하면 중단
    if future_vowels < 1:      # 모음을 하나도 못 채우는 경우
        return False
    if future_consonants < 2:  # 자음을 두 개 못 채우는 경우
        return False

    # 미래에도 조건 만족 가능하면 탐색
    return True

# main
L, C = map(int, input().split())
chars = sorted(list(input().split()))
vowels = 'aeiou'
selected = []
combination(0, 0, C, L)
"""