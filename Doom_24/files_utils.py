import json
import csv
import yaml
# Функция для чтения JSON файлов

def read_json(file_path: str, encoding: str="utf-8"):
    """Читаем данные из JSON-файла"""
    with open(file_path, 'r', encoding=encoding) as file:
        return json.load(file)
    

# Функция для записи JSON файла
def write_json(data, file_path: str, encoding: str = "utf-8"):
    """Записываем данные в JSON-файл"""
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, indent=4)

# Функция для добавления JSON объекта в конец файла
def append_json(data: list[dict], file_path: str, encoding: str = "utf-8"):
    """Добавляем данные в JSON-файл"""
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []
    existing_data.extend(data)
    write_json(existing_data, file_path, encoding)
           






