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
            if not isinstance(existing_data, list):
                existing_data = [existing_data]
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []
    existing_data.extend(data)
    with open(file_path, 'w') as file:
        json.dump(existing_data, file, indent=4)

# Функция для чтения CSV файла

def read_csv(file_path, delimiter=';', encoding: str ='windows-1251'):
    """Читаем данные из CSV-файла"""
    data = []
    with open(file_path, 'r', encoding=encoding, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=delimiter)
            for row in reader:
                data.append(row)
    return data
    
# Функция для записи CSV файла

def write_csv(data, file_path, delimiter=';', encoding: str ='windows-1251'):
    """Записываем данные в CSV-файл"""
    with open(file_path, 'w', encoding=encoding, newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        writer.writerows(data)

# Функция для добавления CSV в существующей файл

def append_csv(data, file_path, delimiter=';', encoding: str ='windows-1251'):
    """Добавляет данные в существующий CSV-файл."""
    with open(file_path, 'a', encoding=encoding, newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        writer.writerows(data)

# Функция для чтения txt файла

def read_txt(file_path, encoding: str = "utf-8"):
    """Читает данные из текстового файла."""
    with open(file_path, 'r', encoding=encoding) as file:
        return file.read()

# Функция для записи txt файла
def write_txt(data, file_path, encoding: str = "utf-8"):
    """Записывает данные в текстовый файл."""
    with open(file_path, 'w', encoding=encoding) as file:
        file.write(data)

# Функция для добавления txt в  файл
def append_txt(data, file_path, encoding: str = "utf-8"):
    """Добавляет данные в конец текстового файла."""
    with open(file_path, 'a', encoding=encoding) as file:
        file.write(data)

# Функция для чтения YAML файла
def read_yaml(file_path):
    """Читает данные из YAML-файла."""
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)



