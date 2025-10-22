N = int(input())
bt = {}
for _ in range(N):
    p, l, r = input().split()  # {부모:(왼쪽자식, 오른쪽자식)}
    if l != '.' and r != '.':
        bt[p] = (l, r)
    elif l != '.':
        bt[p] = (l, 0)
    elif r != '.':
        bt[p] = (0, r)
    else:
        bt[p] = (0, 0)
def a(A):  # 전위순회 -> 부, 왼, 오
    if A == 0:
        return
    print(A, end='')
    a(bt[A][0])
    a(bt[A][1])
def b(A):  # 중위순회 -> 왼, 부, 오
    if A == 0:
        return
    b(bt[A][0])
    print(A, end='')
    b(bt[A][1])
def c(A):  # 후위순회 -> 왼, 오, 부
    if A == 0:
        return
    c(bt[A][0])
    c(bt[A][1])
    print(A, end='')

a('A')
print()
b('A')
print()
c('A')