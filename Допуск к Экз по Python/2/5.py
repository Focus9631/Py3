import re
a=input()
s=re.findall('[A-Z][a-z]+\d{2,4}',a)
print(' '.join(s))

