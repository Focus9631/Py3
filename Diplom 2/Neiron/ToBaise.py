import os
import numpy as np
from PIL import Image

# пути к папкам с изображениями
train_path = 'path/to/train/folder'
valid_path = 'path/to/valid/folder'
test_path = 'path/to/test/folder'

# список имен файлов в каждой папке
train_file_list = os.listdir(train_path)
valid_file_list = os.listdir(valid_path)
test_file_list = os.listdir(test_path)

# функция для конвертации изображений в массив
def convert_images_to_array(path, file_list):
    data = np.zeros((len(file_list), 1, 256, 256), dtype=np.float32)
    for i, filename in enumerate(file_list):
        # загрузка изображения и конвертация в ч/б
        image = Image.open(os.path.join(path, filename)).convert('L')
        # изменение размера до 256х256
        image = image.resize((256, 256))
        # нормализация значений пикселей
        data[i, 0, :, :] = np.array(image, dtype=np.float32) / 255.0
    return data

# конвертация изображений в массивы
train_data = convert_images_to_array(train_path, train_file_list)
valid_data = convert_images_to_array(valid_path, valid_file_list)
test_data = convert_images_to_array(test_path, test_file_list)

# сохранение массивов в файлы
np.save('train_data.npy', train_data)
np.save('valid_data.npy', valid_data)
np.save('test_data.npy', test_data)