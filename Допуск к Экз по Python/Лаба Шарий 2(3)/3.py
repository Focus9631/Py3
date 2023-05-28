from pathlib import Path

path = Path(r'C:\Users\Артём-ПК\Desktop\Лаба Шарий 2(3)\jlob1')
mask = '*.mp3'
conf_file = Path(r'C:\Users\Артём-ПК\Desktop\Лаба Шарий 2(3)\jlob1\config.txt')

cfg = {}
with conf_file.open() as f:
    for line in f:
        s = line.split('[')[0]
        cfg[s.split('.')[1].strip()] = s.strip()
# print(cfg)

for f in path.glob(mask):
    name = f.name.replace(f.suffix, '')
    f.rename(str(f).replace(name, cfg.get(name)))

