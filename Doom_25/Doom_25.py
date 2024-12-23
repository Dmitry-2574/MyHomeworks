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