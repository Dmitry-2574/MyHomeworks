import re # модуль re для работы с регулярными выражениями.  Регулярные выражения используются для проверки наличия цифр, заглавных и строчных букв, а также специальных символов в пароле.
def password_checker(func):# Это декоратор , В данном случае func — это функция register_user которую мы будем украшать
    def wrapper(password):#Эта функция будет выполнять фактическую проверку пароля.  Она принимает пароль password в качестве аргумента. Внутри данной функции идет проверка пароля.
        if len(password)>8:
            return "Ошибка: Пароль должен содержать минимум 8 символов. "
        if not re.search()