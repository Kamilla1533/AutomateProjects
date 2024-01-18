import os
import shutil

path = input("Enter path: ")
files = os.listdir(path)

for x in files:
    filename, extension = os.path.splitext(x)
    extension = extension[1:]

    # Проверка
    if os.path.exists(path + "/" + extension):
        shutil.move(path + "/" + x, path + "/" + extension + "/" + x)
    else:
        os.makedirs(path + "/" + extension)
        shutil.move(path + "/" + x, path + "/" + extension + "/" + x)
