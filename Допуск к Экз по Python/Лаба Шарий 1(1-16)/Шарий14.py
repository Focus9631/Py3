def non_empty(x):
    def new():
        f=x()
        return [i for i in f if i!='None' and i!='']
    return new
@non_empty
def get_pages():
    return ['a', '', 'b', 'None', 'c']
print(get_pages())
