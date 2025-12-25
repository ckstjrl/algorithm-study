A, B = input().split()

min_A = int(A)
min_B = int(B)
max_A = int(A)
max_B = int(B)
for i in range(len(A)):
    if A[i] == '6':
        min_A -= 10 ** (len(A) - 1 - i)
    elif A[i] == '5':
        max_A += 10 ** (len(A) - 1 - i)
for i in range(len(B)):
    if B[i] == '6':
        min_B -= 10 ** (len(B) - 1 - i)
    elif B[i] == '5':
        max_B += 10 ** (len(B) - 1 - i)

print(min_A + min_B, max_A + max_B)