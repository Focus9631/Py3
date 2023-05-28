import re
a=input()
q=re.findall(r'[A-Z]\D*\d{2}\b| [A-Z]\D*\d{4}\b',a)
print(q)
