def pre_process(a):
    def decorator(f):
        def new(s):
            x=[s[i]-a*s[i-1] for i in range(1,len(s))]
            return f(x)
        return new
    return decorator
@pre_process(a=0.97)
def plot_signal(s):
    for sample in s:
        print(sample)
plot_signal([1,2,3,4])
