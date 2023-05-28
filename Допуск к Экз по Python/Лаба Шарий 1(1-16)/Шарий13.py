x=[10,30,64,21]
def extra_enumerate(x):
    cum=0
    for elem in x:
        cum+=elem
        frac=cum/sum(x)
        yield(elem,cum,frac)
for elem, cum, frac in extra_enumerate(x):
    print(elem, cum, frac) 

