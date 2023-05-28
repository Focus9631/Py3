print('Введи свою строчку:')
Q = input()
for i in Q:
        if Q.index(i)%3!=0:
                print(i, end="")
