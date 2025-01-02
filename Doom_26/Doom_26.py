import re 
# модуль re для работы с регулярными выражениями.  Регулярные выражения используются для проверки наличия цифр, заглавных и строчных букв, а также специальных символов в пароле.
def password_checker(func):
    # Это декоратор , В данном случае func — это функция register_user которую мы будем украшать
    def wrapper(password):
        #Эта функция будет выполнять фактическую проверку пароля.  Она принимает пароль password в качестве аргумента. Внутри данной функции идет проверка пароля.
        if len(password)<8:
            return "Ошибка: Пароль должен содержать минимум 8 символов. "
            #re.search() ищет соответствие регулярному выражению внутри строки.  Если хотя бы одно условие не выполняется, функция wrapper возвращает сообщение об ошибке.
        if not re.search("[0-9]", password):
            return "Ошибка: Пароль должен содержать хотя бы одну цифру."
        if not re.search("[A-Z]", password):
            return "Ошибка: Пароль должен содержать хотя бы одну заглавную букву."
        if not re.search("[a-z]", password):
            return "Ошибка: Пароль должен содержать хотя бы одну строчную букву."
        if not re.search("[^a-zA-Z0-9]", password):
            return "Ошибка: Пароль должен содержать хотя бы один специальный символ."
        return func(password) 
        # Если все условия выполнены, выполняем функцию register_user с этим паролем.
    return wrapper

@password_checker
def register_user(password):
    return "Регистрация успешна"

print(register_user("P@sswOrd1")) # Все условия соблюдены
print(register_user("Short"))  # Слишком короткий
print(register_user("12345678")) # Нет заглавных/строчных/спецсимволов
print(register_user("Password123")) # Нет спецсимволов

import csv
# Эта функция считывает данные из csv файла и возвращает список словарей, каждый из которых представляет собой строку csv файла.
def password_validator(length: int = 8, uppercase: int = 1, lowercase: int = 1, special_chars: int = 1):
    def decorador(func):
        def wrapper(username, password):
            if len(password) > length:
                raise ValueError(f"Пароль должен быть не короче {length} символов.")
            if sum(1 for char in password if char.isupper()) < uppercase:
                raise ValueError(f"Пароль должен содержать хотя бы {uppercase} заглавных букв.")
