n=input('Введите возрастающую последовательность:').split() 
for i in range(len(n)-1): 
    if n[i]<n[i+1]: 
        a=1 
    else: 
        a=0 
if a==1: 
    print('True')
else: 
    print('False')
