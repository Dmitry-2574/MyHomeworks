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
            if len(password) < length:
                raise ValueError(f"Пароль должен быть не короче {length} символов.")
            if sum(1 for char in password if char.isupper()) < uppercase:
                raise ValueError(f"Пароль должен содержать не менее {uppercase} заглавных букв")
            if sum(1 for char in password if char.islower()) < lowercase:
                raise ValueError(f"Пароль должен содержать не менее {lowercase} строчных букв")
            if sum(1 for char in password if not char.isalnum()) < special_chars:
                raise ValueError(f"Пароль должен содержать не менее {special_chars} специальных символов")
            return func(username, password)
        return wrapper
    return decorador
#Это фабрика декораторов.  Она принимает параметры для настройки проверки пароля (минимальная длина, количество заглавных и строчных букв, специальных символов).  Внутри нее определяется декоратор, который, в свою очередь, создает обертку (wrapper) вокруг функции регистрации.  Обертка выполняет проверки пароля на соответствие заданным критериям. Если проверка не пройдена, выбрасывается исключение ValueError с описанием проблемы.

def username_validator(func):
    def wrapper(username, password):
        if " " in username:
            raise ValueError("Имя пользователя не может содержать пробелы.")
        return func(username, password)
    return wrapper
#Декоратор - Он проверяет, нет ли пробелов в имени пользователя.  Если пробелы есть, выбрасывается исключение ValueError. 

@username_validator
# `@username_validator` перед `register_user` означает, что `register_user` обертывается функцией `wrapper` из `username_validator`. 

@password_validator(length=10, uppercase=2, lowercase=2, special_chars=2)
#перед register_user  означает, что результат username_validator (уже обернутая функция register_user)  обертывается функцией wrapper из  password_validator.

def register_user(username: str, password: str):
    #Это функция регистрации пользователя. Она принимает имя пользователя и пароль.  Она декорирована как username_validator, так и password_validator.  Это означает, что перед выполнением register_user выполняются проверки из обоих декораторов. Если проверки пройдены успешно, функция записывает имя пользователя и пароль в CSV-файл users.csv.
    with open("users.csv", "a", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([username, password])
    return "Пользователь успешно зарегистрирован!"

# Тестирование успешного случая
try:
    register_user("JohnDoe123", "PassWord123!!")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

# Тестирование неудачного случая по паролю
try:
    register_user("JaneDoe", "Short")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

# Тестирование неудачного случая по юзернейму
try:
    register_user("Jane Doe", "StrongPassword123!!")
    print("Регистрация прошла успешно!")
except ValueError as e:
    print(f"Ошибка: {e}")

