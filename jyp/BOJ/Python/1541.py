eq = input()

result = 0

if '-' in eq:
    arr = list(eq.split('-'))
    if '+' in arr[0]:
        result += sum(map(int, arr[0].split('+')))
    else:
        result += int(arr[0])

    for i in arr[1:]:
        if '+' in i:
            result -= sum(map(int, i.split('+')))
        else:
            result -= int(i)


else:
    result = sum(map(int, eq.split('+')))

print(result)