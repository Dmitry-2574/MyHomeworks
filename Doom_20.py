import os
os.system('cls')
from marvel import small_dict as sd
from pprint import pprint
# 2.1 Попробуйте их просто распечатать
# 2.2 Попробуйте собрать список названий

# new_sd = {}
# new_sd = {key:value for key,value in sd.items()}
# print(f'\nСобранный словарь:\n{new_sd}')


# films = []
# for key, value in sd.items():

#     if value is not None and value > 2024:
        
#             films.append(key)
# print(f'\nПросто распечатываем названия фильмов:\n{films}\n')


# # 2.3 Попробуйте собрать словарь (как исходный, но фильтрованный по году)
# from pprint import pprint

# pprint(f'Собранный словарь фильтрованный по годам:\n{sd}', sort_dicts=False)


# # 2.4 Попробуйте собрать список словарей [{'Человек-хрюк': 2024}, ...]
# # Вариант 1 - однострочник
# # filtered_dict = {title: year for title, year in small_dict.items() if year is not None and year > 2016}

# # Вариант 2
# filtered_dict = []
# for title, year in sd.items():
#         if year is not None and year > 2016:
#                 filtered_dict.append({title:year})
# print(f'\nСобираем список словарей:\n{filtered_dict}')

# user_film = input('Введите названия фильма или его часть: ')

# user_film_dict = {key:value for key,value in sd.items() if user_film.lower() in key.lower()}
# pprint(user_film_dict, sort_dicts=False)

# films = []
# for key, value in sd.items():

#     if value is not None and value == 2024:
        
#         films.append(key)
# print(f'\nПросто распечатываем названия фильмов, определенных годов:\n{films}\n')
# user_year = 2025
# user_film_dict = {key:value for key,value in sd.items() if value is not None and value == user_year}
# pprint(user_film_dict, sort_dicts=False)


# user_film_dict = {key:value for key,value in sd.items() if value is not None and value <= user_year}
# pprint(user_film_dict, sort_dicts=False)


filtered_dict = {title.lower(): year for title, year in sd.items() if year is not None and year > 2016}
print(f'\nСобираем список словарей:\n{filtered_dict}')



