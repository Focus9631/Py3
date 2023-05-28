def same_number(fn):
    def wrapped(list_a):
        for i in range(len(list_a)):
            for j in range(i + 1, len(list_a)):
                if list_a[i] == list_a[j]:
                    print("duplicate:", list_a[i])
    return wrapped

@same_number
def direct_list():
    return 0

a = [1, 2, 3, 8, 10, 11, 11]
direct_list(a)
