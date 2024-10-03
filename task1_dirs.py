import shutil
from pathlib import Path
from sys import argv


"""Функція для копіювання файлів з однієї директорії 
та файлів з її піддиректорій до іншої"""
#Створення піддиректорій із назвами за розширенням файлів у директорії призначення


def copy_directory(src_path: Path, dst_path: Path = None):
    if not dst_path or not dst_path.exists():
        dst_path = Path('dist')
        dst_path.mkdir(exist_ok=True)
   
    if src_path.exists():
        for file in src_path.iterdir():
            if file.is_file():
                subdir = Path(dst_path, f"{file.suffix} files")
                subdir.mkdir(exist_ok=True)
                shutil.copy(file, Path(subdir))
            elif file.is_dir():
                copy_directory(file, dst_path)
    else:
        print("Невірно передано ім'я файлу для копіювання")


if __name__ == "__main__":

    """Скрипт для зчитування аргументів командного рядка"""
    if len(argv)<=1 or len(argv)>3:
        raise ValueError("Не вірно передані аргументи для копіювання")
    else:
        src = Path(argv[1]) if len(argv)>1 else None
        dst = Path(argv[2]) if len(argv)==3 else None

    copy_directory(src, dst)

