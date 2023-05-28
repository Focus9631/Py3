def get_frames(signal,size=1024,overlap=1):
    a=0
    for i in range(len(signal)//(size-overlap)):
        yield signal[a:a+size]
        a+=size-overlap
signal=list(range(0,100))
for frame in get_frames(signal, size=10, overlap=5):
    print(frame)
