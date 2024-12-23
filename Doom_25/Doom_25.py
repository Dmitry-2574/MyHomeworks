from marvel import full_dict
from pprint import pprint



    
# 2. Реализуйте ввод от пользователя, который будет принимать цифры через пробел. Разбейте введённую строку на список и примените к каждому элементу `int`, заменяя нечисловые элементы на `None` с помощью `map`.
number_input = input("Введите числа через пробел: ")
numbers = list(map(lambda x: int(x) if x.isdigit() else None, number_input.split()))
print(f"Обработанный список: {numbers}")

# 3. Используйте `filter`, чтобы создать словарь, содержащий исходные `id` и другие ключи, но только для тех фильмов, `id` которых присутствуют в списке, полученном на предыдущем шаге.
filtered_movies = dict(filter(lambda item: item[0] in numbers and item[0] is not None, full_dict.items()))
pprint(filtered_movies)

# 4. Создайте множество с помощью `set comprehension`, собрав уникальные значения ключа `director` из словаря.
unique_directors = {movie["director"] for movie in full_dict.values() if "director" in movie}
pprint(f'Уникальные режиссеры: {unique_directors}')

# 5. С помощью `dict comprehension` создайте копию исходного словаря `full_dict`, преобразовав каждое значение `'year'` в строку.

copied_dict = {key: {k: (str(v) if k == 'year' else v) for k, v in value.items()} for key, value in full_dict.items() if isinstance(value, dict)}
pprint(f'Копия словаря: {copied_dict}')

# 6. Используйте `filter`, чтобы получить словарь, содержащий только те фильмы, которые начинаются на букву `Ч`.
# Для  решения п.6,  нужно добавить проверку на None  внутри функции safe_get,  и также обработать случай, когда item[1] может быть  не словарем.
def safe_get(d, key, default=""):
    if isinstance(d, dict):
        value = d.get(key)
        return value if value is not None else default
    return default
filtered_titles = [title for title in [safe_get(item[1], 'title') for item in full_dict.items()] if title.lower().startswith('ч') and len(title) > 1]
print(f'Фильмы, названия которых начинаются с буквы "Ч": {filtered_titles}\n')

# 7. Отсортируйте словарь `full_dict` по одному параметру с использованием `lambda`, создавая аналогичный по структуре словарь. Обязательно укажите, по какому параметру вы производите сортировку.

def get_sortable_year(item):
    year = item[1].get('year')
    try:
        return int(year)
    except (ValueError, TypeError):
        return float('inf')

sorted_dict = dict(sorted(full_dict.items(), key=get_sortable_year))

pprint(f'Словарь, отсортированный по году выпуска: {sorted_dict}')


# 8. Отсортируйте словарь `full_dict` по двум параметрам с использованием `lambda`, создавая аналогичный по структуре словарь. Обязательно укажите, по каким параметрам вы производите сортировку.
def get_sortable_year_2(item):
    year = item[1].get('year')
    try:
        return int(year)
    except (ValueError, TypeError):
        return float('inf')

sorted_dict = dict(sorted(full_dict.items(), key=lambda item: (get_sortable_year_2(item), safe_get(item[1], 'title'))))

pprint(f'Словарь, отсортированный по году выпуска, затем по названию: \n{sorted_dict}\n')

