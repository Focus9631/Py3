a=[1,2,3,4,5,6,7,8,9,10]
##for i in range(len(a)):
##    if i%2!=0:
##        print(a[i])
b = list(filter(lambda x:x%2==0, a))
##for i in range(len(b)):
##    if b[i]==True:
##        b[i]=a[i]
##for i in b:
##    if i==False:
##        b.remove(i)
print (b)
