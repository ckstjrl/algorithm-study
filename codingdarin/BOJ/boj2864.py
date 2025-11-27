# BOJ 2864. 5와 6의 차이 (D1/B2)

#-------------------------------2회차 풀이

A, B = input().split()
min_ans = int(A.replace('6', '5')) + int(B.replace('6', '5'))
max_ans = int(A.replace('5', '6')) + int(B.replace('5', '6'))
print(min_ans, max_ans)

#-------------------------------1회차 풀이
# A, B = input().split()
# min_A = min_B = ''
# max_A = max_B = '' 

# for c in A:
#     if c == '5':
#         min_A += '5'
#         max_A += '6'
#         continue
#     if c == '6':
#         min_A += '5'
#         max_A += '6'

#         continue
#     max_A += c
#     min_A += c
    
# for c in B:
#     if c == '5':
#         min_B += '5'
#         max_B += '6'
#         continue
#     if c == '6':
#         min_B += '5'
#         max_B += '6'
#         continue
#     max_B += c
#     min_B += c

# max_ans = int(max_A) + int(max_B)
# min_ans = int(min_A) + int(min_B)

# print(min_ans, max_ans)