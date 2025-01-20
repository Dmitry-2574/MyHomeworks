
import asyncio
from openai import AsyncOpenAI # pip install openai

API_KEY = "sk-or-vv-32acad84830483432df6bb1eb3114ede486fe620ba237c07f152b84c6a27e782"
BASE_URL = "https://api.vsegpt.ru/v1"
MAX_CHUNK_SIZE = 5000 # Максимальная длина текста для 1 запроса к API
SLEEP_TIME = 1 # Задержка между запросами
PROMPT_THEME = """
Привет!

Определи общую тему  текста. И постарайся максимально полно и точно описать её,
с использованием пунктов и подпунктов.

Не додумывай того, чего там небыло.
Исключи small talks.
"""

PROMPT_TIMESTAMPS = """
Привет!

Ты - ассистент по созданию таймкодов для видео.
Тебе будет предоставлен текст с таймкодами из видео.
Твоя задача - создать краткое описание каждого смыслового блока.
Ты не должен использовать полное цитирование. Создай краткое описание для блока.
Каждый блок должен начинаться с таймкода в формате чч:мм:сс.
Описание должно быть одним предложением, передающим суть начинающегося отрезка.
Игнорируй слишком короткие фрагменты или паузы.
Объединяй связанные по смыслу части в один большой блок.
Описания должны быть в стиле, как это обычно делают на youtube.



ВАЖНО.
СТРОГИЕ ПРАВИЛА:
1. Для видео длительностью:
   - до 30 минут: максимум 5 таймкодов
   - 30-60 минут: максимум 8 таймкодов
   - 1-2 часа: максимум 10 таймкодов
   - 2+ часа: максимум 15 таймкодов

2. Минимальный интервал между таймкодами:
   - для коротких видео (до 30 мин): 3-5 минут
   - для длинных видео: 10-15 минут

3. Объединяй близкие по смыслу темы в один таймкод

ВАЖНО: Если ты превысишь количество таймкодов - твой ответ будет отклонён!

В твоём ответе должны быть только таймкоды и описания.
Никаких других комментариев или пояснений.

КАК ПИСАТЬ?

Ты не пишешь описательные, длинные предложения. 
Вроде: "Пояснение адаптивного подхода к верстке на примере Visual Studio Code, где контент перестраивается в зависимости от размера экрана. "

Ты пишешь короткий, ёмкий вариант.
"Адаптивный подход к вёрстке. Пример в Visual Studio Code. Контент перестраивается в зависимости от размера экрана."
Или даже ещё немного короче.

Спасибо!
"""

PROMPT_CONSPECT_WRITER = """
Привет!
Ты опытный технический писатель. Ниже, я предоставляю тебе полный текст лекции а так же ту часть,
с которой ты будешь работать.

Ты великолепно знаешь русский язык и отлично владеешь этой темой.

Тема занятия: {topic}

Полный текст лекции:
{full_text}

Сейчас я дам тебе ту часть, с котороый ты будешь работать. Я попрошу тебя написать конспект лекции.
А так же блоки кода.

Ты пишешь в формате Markdown. Начни с заголовка 2го уровня.
В тексте используй заголовки 3го уровня.

Используй блоки кода по необходимости.

Отрезок текста с которым ты работаешь, с которого ты будешь работать:
{text_to_work}
"""

client = AsyncOpenAI(api_key=API_KEY, base_url=BASE_URL)

async def get_ai_request(prompt: str, max_retries: int = 3, temperature: float = 2.0):
    """
    Отправляем запрос к API  с механизмом повторных попыток

    """
    for attemp in range(max_retries):
        try:
            
            response = await client.chat.completions.create(
                model="openi/gpt-40-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=16000,
                temperature=0.7,
            )
            return response.choices[0].message.content

        except openai.RateLimitError:
            print(f"Error occurred during request: {e}")
            if attemp == max_retries - 1:
                raise
            delay = base_delay * (2 ** attemp)
            await asyncio.sleep(delay)


OUTPUT_FILE = "lecture_summary.md"   
            
def split_text_to_chunks(data: list) -> list:
    chunks = []
    current_chunk = ""
    for item in data:
        text = item['text']
        if len(current_chunk) + len(text) <= MAX_CHUNK_SIZE:
            current_chunk += text
        else:
            if current_chunk:
                chunks.append(current_chunk)
            current_chunk = text

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def save_to_markdown(timestamps: str, theme: str, chunks: list):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("# Таймкоды\n\n")
        f.write(timestamps)
        f.write("\n\n---\n\n")

        f.write("# Краткое содержание\n\n")
        f.write(theme)
        f.write("\n\n---\n\n")

        f.write("# Конспект\n\n")
        for chunk in chunks:
            f.write(chunk)
            f.write("\n---\n\n")

async def main():
    try:
        # Получаем текст лекции
        full_text = " ".join([item['text'] for item in DATA])
        tasks = [
            get_ai_request(PROMPT_TIMESTAMPS + full_text),
            get_ai_request(PROMPT_THEME + full_text)
        ]
        timestamps, theme = await asyncio.gather(*tasks)
        await asyncio.slepp(SLEEP_TIME)

        # Разбиваем текст на части
        chunks = split_text_to_chunks(DATA)

        















# Тест запросов
async def main():
    prompt_cow = "Как кричит корова?"
    prompt_cat = "Как кричит кошка?"
    prompt_monkey = "Как кричит обезьяна?"

    prompts = [prompt_cow, prompt_cat, prompt_monkey]
    results = await asyncio.gather(*[get_ai_request(prompt) for prompt in prompts])

    print(results)


asyncio.run(main())

"""
['Корова кричит "му".', 'Кошка обычно издает звуки, которые можно описать как "мяу". В зависимости от настроения и ситуации, кошка может мяукать по-разному: мягко, настойчиво, громко или тихо. Кроме того, кошки могут издавать и другие звуки, такие как шипение, ворчание или урчание.', 'Обезьяны издают множество звуков, чтобы общаться друг с другом, включая крики, крики, визги и другие звуки. Например, некоторые виды обезьян могут издавать громкие крики, которые могут звучать как "уа-уа" или "га-га". Каждый вид имеет свои особенности звучания, поэтому точное "крик" может варьироваться.']
"""
```


## Пример выходных данных

00:00:00 -  Обзор сетки Bootstrap: как блоки располагаются на разных размерах экрана.
00:01:13 -  Контейнеры в Bootstrap: фиксированные и резиновые, их свойства и различия.
00:04:20 -  Сетка Bootstrap: класс row, колонки и их автоматическое позиционирование.
00:08:50 -  Опции сетки: префиксы размеров, управление колонками и вложенность.
00:11:27 -  Настройка ширины колонок: использование call с цифрами и автоматическое распределение.
00:13:11 -  Комбинирование классов: call, call-lg, call-md-auto для адаптивной верстки.
00:23:54 -  Gatters: добавление отступов на контейнеры и ряды.
00:25:36 -  Порядок элементов: использование order и изменение порядка на разных экранах.
00:30:39 -  Утилиты: скрытие и отображение элементов на разных размерах экрана.

А так же описание темы занятия + файл с конспектом!
## Пример входных данных

```python
DATA = [
    {
        "timestamp": [
            0.0,
            27.7
        ],
        "text": " Разберемся, как работает сетка Bootstrap. Сетка Bootstrap позволяет делать многие вещи достаточно гибко. Мы можем сразу заглянуть в Bootstrap примеры и, допустим, на примере вот этой истории посмотреть, что на с каких-то других размеров, эти блоки располагаются просто друг подружкой."
    },
    {
        "timestamp": [
            28.58,
            34.78
        ],
        "text": " И сделано это в данном случае просто за счет использования сетки Bootstrap, то есть уже готовых для нас классов."
    },
    {
        "timestamp": [
            35.12,
            40.24
        ],
        "text": " В этих примерах используется только Bootstrap стиле, ничего более дополнительного нет."
    }............. # ПОЛНЫЙ НАБОР БУДЕТ В ОТДЕЛЬНОМ ФАЙЛЕ