def reverse_num (num):
    result = (num % 10) * 100
    num //= 10
    result += (num % 10) * 10
    num //= 10
    result += num
    return result

A, B = map(int, input().split())
if reverse_num(A) > reverse_num(B):
    print(reverse_num(A))
else:
    print(reverse_num(B))