
a = [1,2,3,4,5]
"""8.1"""
##for i in range(len(a)):
##    if i%2==0:
##        print(a[i])
##gen = [a[i]  for i in range(len(a)) if i%2==0]
##print (gen)
##fals=list(zip(filter(lambda x:x%2==0, range(len(a))),a[::2]))
##print(fals)


"""8.2"""
##for i in range(len(a)):
##    if a[i]%2==0:
##        print(a[i])
##gen = [a[i]  for i in range(len(a)) if a[i]%2==0]
##print(gen)
##fals=list(filter(lambda x:x%2==0,a))
##print(fals)

"""8.3"""
for i in range(len(a)):
    if a[i-1]<a[i]:
        print(a[i])
text = [a[i] for i in range(len(a)) if a[i-1]<a[i]]
print (text)
##text1 = list(filter(lambda))
