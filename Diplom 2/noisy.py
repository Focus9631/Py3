import os
import numpy as np
from PIL import Image
from tqdm import tqdm

# каталог, содержащий изображения для обработки
img_dir = input("Введите путь к папке с фото: ") or "E:\\MIPT\\Diplom\\archive\\test"
# директория для сохранения обработанных изображений
output_dir = input("Введите путь к папке сохранения фото: ") or "E:\\MIPT\\Diplom\\archive\\final"
# расширение изображений
file_extension = input("Введите расширение фото: ") or ".jpg"
# получить список всех файлов в каталоге
files = os.listdir(img_dir)
jpeg_quality = 100  # Качество сохранения JPEG
# Проверяем наличие выходной папки, и если ее нет, создаем
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# цикл по каждому файлу
for file in tqdm(files):
    # проверяем, имеет ли файл расширение .jpg
    if file.endswith(file_extension):
        # построить полный путь к файлу изображения
        img_path = os.path.join(img_dir, file)
        # открыть изображение
        img1 = Image.open(img_path)
        # обработать изображение
        # преобразование в ч/б и плавающую запятую
        img1 = np.array(img1.convert('L'), dtype=float)
        # обнаружение значение максимума яркости
        max_im = img1.max()
        # нормировка матрицы
        img1 /= max_im
        # динамический диапазон конечной картинки в дБ, целесообразны значения от 10 до 80 дБ
        dd = 60
        # преобразование яркостей в дБ
        img1 *= dd / 10
        # получение картинки с экспоненциальным распределением яркостей
        img2 = 10 ** img1
        # получение экспоненциального распределения плотности вероятности для спекл-шума
        im_rnd = -np.log10(np.random.rand(*img2.shape))
        img2 = img2 * im_rnd
        # нормировка на новый максимум (после рандомизации)
        img_out = img2 / img2.max()
        # отрезание нижней (шумовой) части картинки по порогу 0.005 от максимума - порог может быть переменным
        img_out = np.interp(img_out, (0.005, img_out.max()), (0, 2))

        # построить выходной путь для обработанного изображения без преобразования динамического диапазона
        output_path_lin = os.path.join(output_dir, f'{os.path.splitext(file)[0]}_{dd}_lin1.jpg')

        # # сохранить обработанное изображение как объект PIL Image, а затем сохранить его на диск.
        # Image.fromarray((img_out * 255).astype(np.uint8)).save(output_path_lin)

        # логарифмическое преобразование динамического диапазона
        img3 = 10 / dd * np.log10(img2)
        img_out2 = img3 / img3.max()
        img_out3 = np.where(img_out2 < 0, 0, img_out2)

        # построить выходной путь для обработанного изображения с логарифмическим преобразованием динамического диапазона
        output_path_db = os.path.join(output_dir, f'{os.path.splitext(file)[0]}_{dd}_db1.jpg')

        # сохранить обработанное изображение с логарифмическим преобразованием динамического диапазона как объект PIL Image, а затем сохранить его на диск.
        Image.fromarray((img_out3 * 255).astype(np.uint8)).save(output_path_db)

print("Обработка изображений завершена!")