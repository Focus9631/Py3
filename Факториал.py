from functools import reduce
a=int(input())
print (1 if a==0 else reduce(lambda x,y: x*y, range(1,a+1)))
