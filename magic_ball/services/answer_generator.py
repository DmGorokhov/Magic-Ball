import random

ANSWERS: list[str] = [
    "Да",
    "Нет",
    "Возможно",
    "Вопрос не ясен",
    "Абсолютно точно",
    "Никогда",
    "Даже не думай",
    "Сконцентрируйся и спроси опять"
]


def get_answer() -> str:
    return random.choice(ANSWERS)
