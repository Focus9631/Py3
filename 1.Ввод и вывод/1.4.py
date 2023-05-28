a=int(input())
b=int(input())
print(a,'+',b,'=',a+b)
print(a,'-',b,'=',a-b)
print(a,'*',b,'=',a*b)
if b!=0:
    print(a,'/',b,'=',a/b)
else:
    print('На 0 делить нельзя!')
print(a,'^2','=',a**2)
print(b,'^2','=',b**2)
print('(',a,'+',b,')^2=',(a+b)**2)
print('(',a,'-',b,')^2=',(a-b)**2)
print('(',a,'*',b,')^2=',(a*b)**2)
if b!=0:
    print('(',a,'/',b,')^2=',(a/b)**2)
else:
    print('На 0 делить нельзя!')
print('(',a,'+',b,')^3=',(a+b)**3)
print('(',a,'-',b,')^3=',(a-b)**3)
print('(',a,'*',b,')^3=',(a*b)**3)
if b!=0:
    print('(',a,'/',b,')^3=',(a/b)**3)
else:
    print('На 0 делить нельзя!')
