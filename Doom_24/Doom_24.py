import json
# Функция для чтения JSON файлов

def read_json(file_path: str, encoding: str="utf-8"):
    with open(file_path, 'r', encoding=encoding) as file:
        text = file.read()
        return text
    

# Функция для записи JSON файла
def write_json(data, file_path: str, encoding: str = "utf-8"):
    with open(file_path, mode, encoding=encoding) as file:
        file.write(text + "\n")

TXT_FILE = r"./Doom_24/Doom_24_test.txt"
with open(TXT_FILE, "r", encoding="utf-8") as file:
    text = file.read()


print(text)

JSON_STRING = """

{"coord":{"lon":30.2642,"lat":59.8944},"weather":[{"id":804,"main":"Clouds","description":"пасмурно","icon":"04n"}],"base":"stations","main":{"temp":3.36,"feels_like":-1.6,"temp_min":2.08,"temp_max":3.36,"pressure":1020,"humidity":90,"sea_level":1020,"grnd_level":1018},"visibility":10000,"wind":{"speed":7,"deg":260},"clouds":{"all":100},"dt":1733851619,"sys":{"type":2,"id":197864,"country":"RU","sunrise":1733813355,"sunset":1733835282},"timezone":10800,"id":498817,"name":"Санкт-Петербург","cod":200}

"""

# Сохраним данные в JSON файл
with open("lesson_17/test.json", "w", encoding="utf-8") as file:
    json.dump(python_data, file, indent=4, ensure_ascii=False)

# Загрузка данных из JSON файла
with open("lesson_17/test.json", "r", encoding="utf-8") as file:
    data = json.load(file)

from pprint import pprint

pprint(data, sort_dicts=False, indent=2)


