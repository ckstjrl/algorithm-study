# boj1759 암호 만들기
#트리? 완전 탐색?

#조건: 최소 한 개의 모음(a,e , i, o, u)와 최소 두 개의 자음 (b, c, d...)

# L, C : 암호의 자릿수, 가능한 알파벳의 종류수

# 2차 시도

# 모음 1개와 자음 2개 조건 충족하는지를 확인하는 함수
def requirement_fit(password):
    #코딩 참조: 단순 리스트 대신 set를 사용, 중복 불필요, 속도 향상
    vowel_list = set('aeiou')

    #모음(vowel) 초기값
    vowel_count = 0

    #모음(consonant) 초기값
    consonant_count = 0

    #기존에 이중 리스트 형식으로 만드는 대신 해당 형식으로 input값을 바로 판단, 모음, 자음, 구분
    for letter in password:
        if letter in vowel_list:
            vowel_count += 1
        else:
            consonant_count += 1

    return vowel_count >= 1 and consonant_count >= 2

#위 조건을 충족하는 조합을 직접적으로 만들기
def make_combination(arr, L, start = 0, cur_list = []):
    if len(cur_list) == L:
        password = ''.join(cur_list)

        #위에서 만든 함수를 통해서 조건 충족 여부 확인
        if requirement_fit(password):
            print(password)
        return
    
    for i in range(start, len(arr)):
        cur_list.append(arr[i])
        make_combination(arr, L, i+1, cur_list)
        cur_list.pop()

# 아래부터는 입력 및 함수 사용
L, C = map(int, input().split())

# map 에 너무 집착하지 말기, arr를 받아올때 단순히 띄워쓰기를 기준으로 끊고 싶은 거라면 split으로 충분하다
arr = input().split()

arr.sort()

# 함수를 통한 생성
make_combination(arr, L)



# # 아래 코드는 출력 시점 오류 및 조건 검사 진행하지 않음 이슈로 다시 코드 짜 봄
# def gen_combination(letters, L):
#     global result

#     if L == 0:
#         return [[]]

#     for i in range(0, len(letters)):
#         letter = letters[i]
#         next_let = letters[i + 1:]

#         for com in gen_combination(next_let, L - 1):
#             result.append([letter] + com)

#     print(''.join(result))

#     return result

# result = []

# L, C = map(int, input().split())

# letters = list(map(str, input().split()))

# letters.sort()

# gen_combination(letters, L)
