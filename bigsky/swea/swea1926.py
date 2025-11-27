N = int(input())

for num in range(1, N + 1):
    if num // 10 == 0:
        if num % 3 == 0:
            print('-', end=' ')
        else:
            print(num, end=' ')
    elif num // 100 == 0:
        clap = ''
        if num % 10 != 0:
            if num % 10 % 3 == 0:
                clap = clap + '-'
        if (num // 10) % 3 == 0:
            clap = clap + '-'
        if clap:
            print(clap, end=' ')
        else:
            print(num, end=' ')
    else:
        clap = ''
        if num % 10 != 0:
            if num % 10 % 3 == 0:
                clap = clap + '-'
        if (num // 10) % 10 != 0:
            if (num // 10) % 10 % 3 == 0:
                clap = clap + '-'
        if (num // 100) % 3 == 0:
            clap = clap + '-'
        if clap:
            print(clap, end=' ')
        else:
            print(num, end=' ')