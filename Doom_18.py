

text = input("Введите текст: ")
shift = int(input("Введите сдвиг: "))
encrypted_text = ""


for char in text: # Проходим по каждому символу текста
    if char == " ": # Если символ - пробел, оставляем его без изменений
      encrypted_text += " "
    else:
      code = ord(char) # Получаем числовой код символа
      new_code = code + shift # Добавляем сдвиг
        
    if char.isalpha(): # Если символ - буква, обрабатываем его циклически
      if char.isupper():
        start_code = ord('A')
        end_code = ord('Z') + 1
      else:
        start_code = ord('a')
        end_code = ord('z') + 1
      if new_code < start_code:
        new_code += end_code - start_code
      elif new_code >= end_code:
        new_code -= end_code - start_code
    
    encrypted_char = chr(new_code) # Получаем зашифрованный символ
    encrypted_text += encrypted_char

print("Результат:", encrypted_text)