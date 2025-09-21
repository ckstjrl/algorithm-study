'''
(BOJ1284 / D1): 집 주소
'''

while True:
    address = input()
    if address == '0':
        break

    len_plate = 1
    for i in range(len(address)):
        if address[i] == '0':
            len_plate += 4
        elif address[i] == '1':
            len_plate += 2
        else:
            len_plate += 3
        len_plate += 1

    print(len_plate)