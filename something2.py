##a=[1,2,3,1,2,2,1,1,12,3,4,1,1,1,2,3,6,5,6,7,8,9]
##N=len(a)
##top=a[0]
##for k in range(N//2):
##    a[k],a[N-1-k]=a[N-1-k],a[k]\

##top=a[N-1]
##for i in range(N-2,-1,-1):
##    a[i+1]=a[i]
##a[0]=top

##for i in range(N,0,-1):
##    for j in range(1,i):
##        if a[j-1] > a[j]:
##            a[j],a[j-1]=a[j-1],a[j]
##        
#print(a)

A=[True]*20
n=len(A)
A[0]=A[1]=False
for i in range (2,n):
    if A[i]:
        for i in range (2*i,n,i):
            A[i]=False
for m in range(n):
    print(m,'-','простое' if A[m] else 'составное')
