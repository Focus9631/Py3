print('Введи свою строчку:')
Q = input()
H1 = Q.find('h')
H2 = Q.rfind('h')
if H1 >= 0 and H2 >= 0 and H1 < H2:
    print(Q[:H1 + 1] + Q[H1 + 1:H2].replace('h', 'H') + Q[H2:])
else:
    print(Q)
