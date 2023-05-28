import os
import cv2
from tqdm import tqdm

#Путь к файлам исходным и обработаным
input_folder = input("Введите путь к папке с фото: ")
if input_folder == "":
    input_folder = r"E:\MIPT\Diplom\database\Database"
output_folder = input("Введите путь к папке сохранение фото: ")
if output_folder == "":
    output_folder = r"E:\MIPT\Diplom\database\train"
file_extension = input("Введите расширение фото: ")
if file_extension == "":
    file_extension = ".jpg"  # Добавлен параметр расширения файла


# Создаем выходную папку, если она не существует
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Получаем список файлов с заданным расширением в папке входных данных
files = [f for f in os.listdir(input_folder) if f.endswith(file_extension)]

# Инициализируем индикатор прогресса
pbar = tqdm(total=len(files))

# Проходимся по всем файлам
for file_name in files:
    try:
        # Загружаем изображение
        img = cv2.imread(os.path.join(input_folder, file_name))
        # Проверяем, что изображение загружено
        if img is None:
            print(f"Ошибка загрузки файла {file_name}")
            continue
        # Применяем фильтры и стандартизируем изображение
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.equalizeHist(img)
        # Сохраняем изображение в выходную папку
        output_file_name = os.path.splitext(file_name)[0] + file_extension  # Исправлено сохранение имени файла
        cv2.imwrite(os.path.join(output_folder, output_file_name), img)
    except Exception as e:
        print(f"Ошибка при обработке файла {file_name}: {str(e)}")
        continue
    # Обновляем индикатор прогресса
    pbar.update(1)

# Заканчиваем работу индикатора прогресса
pbar.close()

# Выводим сообщение о завершении работы
print("Скрипт успешно завершил работу!")
