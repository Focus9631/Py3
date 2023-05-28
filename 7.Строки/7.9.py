a=input()
num=0
for i in range(len(a)):
    if a[i]=="f":
        num+=1
        if num==2:
            print(i)     
if num==1:
        print('-1')
elif "f" not in a:
    print('-2')
