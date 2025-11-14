# BOJ 1094. 막대기 (D1 / S5)

#---------------------------2회차 풀이
x = int(input())

ans = bin(x).count('1')
print(ans)

# #-------------------------1회차 풀이
# x = int(input())
# arr = [64]

# def cut(n):
#     sum_arr = sum(arr) 
#     if sum_arr == x:
#         return len(arr)

#     arr.sort(reverse=True)
#     small = arr.pop()
#     a = b = small//2
#     if sum_arr -small + a >= n:
#         arr.append(a)
#     else:
#          arr.append(a)
#          arr.append(b)
#     return cut(n)

# ans = cut(x)
# print(ans)