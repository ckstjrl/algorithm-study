# T = int(input())
# for test_case in range(1, T+1):
#     ls = []
#     arr = [input() for _ in range(5)]
#     for i in arr:
#         len_str = len(i)
#         while len_str < 15:
#             i += '!'
#             len_str += 1
#         ls.append(i)
#     ans = ''
#     for a,b,c,d,e in zip(*ls):
#         ans += a
#         ans += b
#         ans += c
#         ans += d
#         ans += e
#     ans = ans.replace('!','')
#     print(f"#{test_case} {ans}")

T = int(input())
for test_case in range(1, T+1):
    # input 문자열에 대해 15 길이로 패딩 진행
    arr = [input().ljust(15) for _ in range(5)]
    ans = ''
    # 각 문자열들에 대해 zip연산 -> 열 별로 문자 목록을 받음
    for chars in zip(*arr):
        ans += ''.join(chars)
    # str.ljust()로 엮은 문자열에는 공백이 포함되어 있어 공백 제거
    ans = ans.replace(' ','')
    print(f"#{test_case} {ans}")