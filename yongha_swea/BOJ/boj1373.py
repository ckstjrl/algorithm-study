# BOJ1373 2진수 8진수

# 2진수 -> 10진수 -> 8진수로 하는 Python 내장 함수 사용 방식
binary_num = input().strip()
print(oct(int(binary_num, 2))[2:])

# # 이진수를 팔진수로 변환하는 dict
# bin_oct = {
#     '000': '0',
#     '001': '1',
#     '010': '2',
#     '011': '3',
#     '100': '4',
#     '101': '5',
#     '110': '6',
#     '111': '7',
# }
#
# # 처음 input으로 들어오는 이진수
# binary_num = input().strip()
#
# while True:
#     # 3자리 단위로 묶음이 맞아떨어지면 loop 탈출
#     if len(binary_num) % 3 == 0:
#         break
#     else:
#         # 앞에다가 0을 더해서 이진수를 팔진수에 맞춰서 묶어주기
#         binary_num = '0' + binary_num
#
# # 팔진수를 받을 변수
# oct_num = ''
#
# for i in range(0, len(binary_num), 3):
#     # 세자리수 단위로 묶기
#     pairing = binary_num[i:i+3]
#
#     # 해당 묶음을 dict에서 찾아서 팔진수로 변환 후 더해주기
#     oct_num = oct_num + bin_oct[pairing]
#
# print(oct_num)


