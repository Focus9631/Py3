Capitals = {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}
Capitals = dict(Russia = 'Moscow', Ukraine = 'Kiev', USA = 'Washington')
Capitals = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])
Capitals = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))
Capitals['Belarus']='Minsk'
##key='Kiev'
##if key in Capitals:
##    print(Capitals.pop(key))
##try:
##    del Capitals['Kiev']
##except KeyError:
##    print('Net elementa s takim klyuchom "'+key+'" v slovare')
print(Capitals)

for a,b in Capitals.items():
    print(a, b)
