# 3개의 연속된 문자열 입력받기
three_strings = [input() for _ in range(3)]

# 입력된 문자열을 '패턴'으로 변환하여 저장할 리스트
# "FizzBuzz" → 0, "Fizz" → 'F', "Buzz" → 'B', 숫자 → (숫자 mod 15)  (주기성이 15이므로 mod 15로 표현)
pattern = [None] * 3

for i in range(3):
    if three_strings[i] == 'FizzBuzz':              # 문자열이 "FizzBuzz"이면
        pattern[i] = 0                              # pattern에 0으로 저장
    elif three_strings[i] == 'Fizz':                # 문자열이 "Fizz"이면
        pattern[i] = 'F'                            # pattern에 'F'라고 저장
    elif three_strings[i] == 'Buzz':                # 문자열이 "Buzz"이면
        pattern[i] = 'B'                            # pattern에 'B'라고 저장
    else:                                           # 문자열이 숫자일 경우
        pattern[i] = int(three_strings[i]) % 15     # pattern에 mod 15 값으로 저장

# 출력(4번째 문자열)이 "FizzBuzz"인 패턴 1가지
if pattern == ['F', 13, 14]:
    print('FizzBuzz')

# 출력(4번째 문자열)이 "Fizz"인 패턴 4가지
elif pattern in [['F', 4, 'B'], ['F', 7 , 8], ['F', 'B', 11], [0, 1, 2]]:
    print('Fizz')

# 출력(4번째 문자열)이 "Buzz"인 패턴 2가지
elif pattern in [[2, 'F', 4], [7, 8, 'F']]:
    print('Buzz')

# 위 경우에 해당하지 않는다면 출력은 숫자로 나타나므로 → 패턴을 이용해 숫자 계산
else:
    # 패턴에서 숫자가 포함된 위치(idx)를 찾아서
    for i in range(3):
        if type(pattern[i]) == int:
            idx = i
            break
    # 입력된 숫자에서 몇 칸 뒤인지 계산해서 실제 정답 숫자 출력
    ans = int(three_strings[idx]) + (3 - idx)
    print(ans)

"""
 * 추가 설명
 
 * 출력(4번째 문자열)이 "FizzBuzz"인 패턴 1가지:
  ["Fizz", 13, 14] → 그 다음 수는 15이므로 "FizzBuzz"

 * 출력(4번째 문자열)이 "Fizz"인 패턴 4가지:
  ["Fizz", 4, "Buzz"] → 그 다음은 6 → "Fizz"
  ["Fizz", 7, 8]      → 그 다음은 9 → "Fizz"
  ["Fizz", "Buzz", 11]→ 그 다음은 12 → "Fizz"
  [0, 1, 2]           → (즉 15,16,17) 그 다음은 18이므로 → "Fizz"

 * 출력(4번째 문자열)이 "Buzz"인 패턴 2가지:
  [2, "Fizz", 4]   → 그 다음은 5 → "Buzz"
  [7, 8, "Fizz"]   → 그 다음은 10 → "Buzz"
"""