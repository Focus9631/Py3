import os
import shutil
import random

# Путь к исходной папке с фотографиями
src_folder = r'E:\MIPT\Diplom\database\BlackWhiteNoise'

# Пути к папкам, в которые будут разбиты фотографии
train_folder = '/path/to/train/folder'
val_folder = '/path/to/validation/folder'

# Процентное соотношение фотографий в обучающей и валидационной выборках
train_ratio = 0.8
val_ratio = 0.2

# Создание папок, если они еще не существуют
if not os.path.exists(train_folder):
    os.makedirs(train_folder)
if not os.path.exists(val_folder):
    os.makedirs(val_folder)

# Получение списка имен файлов в исходной папке
files = os.listdir(src_folder)

# Перемешивание списка файлов
random.shuffle(files)

# Разбиение списка файлов на обучающую и валидационную выборки
train_files = files[:int(train_ratio*len(files))]
val_files = files[int(train_ratio*len(files)):]

# Копирование файлов из исходной папки в папки обучающей и валидационной выборки
for file in train_files:
    src_path = os.path.join(src_folder, file)
    dst_path = os.path.join(train_folder, file)
    shutil.copyfile(src_path, dst_path)

for file in val_files:
    src_path = os.path.join(src_folder, file)
    dst_path = os.path.join(val_folder, file)
    shutil.copyfile(src_path, dst_path)
