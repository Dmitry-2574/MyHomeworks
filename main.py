import os
os.system('cls')
from cities import cities_list as sd
import random

cities = set()

for keys in sd:
    cities.add(keys['name'].lower())

last_letter = ''
user_turn = True

while cities:
    if user_turn:
        city = input(f"Ваш ход. Последняя буква - '{last_letter}'. Назовите город: ").lower()
        if city == 'cтоп':
            print("ВЫ ПРОИГРАЛИ, машина победила!")
            break
        if city in cities:
            print(f"Вы угадали город, есть такой город {city}")
            cities.remove(city)
            last_letter = city[-1]
            user_turn = False
        else:
            print("Такого города нет в списке или вы уже его назвали. Машина победила!")
            break
    else:
        possible_cities = {c for c in cities if c.startswith(last_letter)}
        if possible_cities:
            computer_city = random.choice(list(possible_cities))
            print(f"Ход машины: {computer_city}")
            cities.remove(computer_city)
            last_letter = computer_city[-1]
            user_turn = True
        else:
            print("Машина не нашла подходящего города. Вы победили!")
            break
if not cities and not user_turn:
    print("Список городов закончился. Ничья!")

