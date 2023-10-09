import os
import random
import string

def generate_random_letters(length):
    letters = string.ascii_lowercase
    return ''.join(random.choices(letters, k=length))

def group_rename_files(num_digits, source_extension, target_extension, name_range, directory='.', counter = 1):
    files = os.listdir(directory)

    for file in files:
        if file.endswith(source_extension):
            # Получаем оригинальное имя файла без расширения
            original_name = os.path.splitext(file)[0]

            # Обрезаем оригинальное имя файла согласно указанному диапазону
            original_name = original_name[name_range[0] - 1:name_range[1]]

            # Генерируем рандомные буквы для имени файла
            random_letters = generate_random_letters(3)  # Указать необходимую длину рандомных букв

            # Форматируем порядковый номер файла с заданным количеством цифр
            num = str(counter).zfill(num_digits)
            counter += 1

            # Формируем новое имя файла
            new_name = random_letters + original_name + '_' + num + target_extension

            # Переименовываем файл
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))

            print(f"Файл {file} переименован в {new_name}")
        else:
            print(f"Файл {file} не является файлом с расширением {source_extension} и будет игнорирован")


# Пример использования
group_rename_files(5, '.txt', '.doc', [1, 3])


