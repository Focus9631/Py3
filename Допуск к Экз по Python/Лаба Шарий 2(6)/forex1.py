import os
import shutil
import sys
import argparse
import datetime


def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, help='Директория(Путь к файлам)')
    parser.add_argument('--days', type=int, help='Количество прошедших дней после последнего изменения файла')
    parser.add_argument('--size', type=int, help='Максимальный размер')
    return parser


def datem(filename):
    Q = os.path.getmtime(filename)
    return datetime.datetime.fromtimestamp(Q)


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    kat = [f for f in os.listdir(namespace.source) if os.path.isfile(os.path.join(namespace.source, f))]
    r1 = namespace.source+'Archive/'
    r2 = namespace.source+'Small/'
    dtf = '%Y-%m-%d %H:%M:%S.%f'
    now = datetime.datetime.now()
    print('------------Это в Archive------------')
    for file in kat:
        t = datem(file)
        timedelta = datetime.datetime.strptime(str(now), dtf)-datetime.datetime.strptime(str(t), dtf)
        if timedelta.days > namespace.days:
            print(file)
            arch = os.path.dirname(r1)
            try:
                os.stat(arch)
            except:
                os.mkdir(arch)
            shutil.move(file, r1)
    kat = [f for f in os.listdir(namespace.source) if os.path.isfile(os.path.join(namespace.source, f))]
    print('------------Это в Small------------')
    for file in kat:
        sz = os.path.getsize(file)
        if sz < namespace.size:
            print(file)
            sm = os.path.dirname(r2)
            try:
                os.stat(sm)
            except:
                os.mkdir(sm)
            shutil.move(file, r2)
