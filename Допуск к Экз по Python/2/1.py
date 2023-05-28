from collections import Counter
with open(r'1\1.txt') as f:
    a=f.read().lower()
q=Counter(a).most_common()
for i in q:
    if i[0].isalpha():
        print(':'.join([str(w) for w in i]))
