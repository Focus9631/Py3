import string
import copy


s = open('file.txt').read()
text1= ''
result = dict()
voc = list()
for a in string.ascii_lowercase:
    voc.append([a, 0])
for words in s:
    if words not in string.ascii_letters:
        continue
    index = string.ascii_lowercase.index(words.lower())
    voc[index][1] += 1


res = list()
for val in voc:
    res.append(tuple(val))
result[2] = res


voc = result[2]
ordered_list = list()
for i in range(0, len(voc)):
    val = voc[i]
    new_val = (val[1], val[0])
    ordered_list.append(new_val)
ordered_list.sort(reverse=True)


res = list()
for i in range(0, len(ordered_list)):
    val = ordered_list[i]
    new_val = (val[1], val[0])
    res.append(new_val)

result[3] = res

print(result[3])
for i in result[3]:
    text1 += i[0]*i[1]

print(text1)
