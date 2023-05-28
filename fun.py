n=2
eps=5e-10
an_1=-1
an=0.25
summa=-0.75
while abs(an-an_1)>eps:
    an_1=an
    an=1/((3*n-2)*(3*n+1))
    summa+=an
    n=n+1     
    print('n= ', n ,'an= ', an,'   ','an_1= ', an_1) 

