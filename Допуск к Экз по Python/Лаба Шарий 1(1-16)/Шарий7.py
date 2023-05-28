x=input('')
x=x.split()
b = ['http://'+i+'.com' if i[-4:]!='.com' else 'http://'+i for i in x if i[:3]=='www']
print(' '.join(b))
