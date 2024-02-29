import re

def normalize_phone(phone_number: str) -> str:
    stripped_phone_number = phone_number.strip() # з обох боків прибираємо зайві пробіли
    pattern = r"\D" # свторюємо шаблон, що відповідає будь-якому символу окрім цифр 0-9
    replacement = ""
    correct_phone_number = re.sub(pattern, replacement, stripped_phone_number) # прибираємо усі нецифрові символи
    if correct_phone_number.startswith("0"): # якщо рядок починається з 0, то додаємо спереду "+38"
        correct_phone_number = "+38" + correct_phone_number
    elif correct_phone_number.startswith("38"): # якщо рядок починається з "38", то спереду додаємо "+"
        correct_phone_number = "+" + correct_phone_number
    return correct_phone_number # повертаємо відредагований телефонний номер

# raw_numbers = [
#     "067\\t123 4567",
#     "(095) 234-5678\\n",
#     "+380 44 123 4567",
#     "380501234567",
#     "    +38(050)123-32-34",
#     "     0503451234",
#     "(050)8889900",
#     "38050-111-22-22",
#     "38050 111 22 11   ",
# ]

# sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
# print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)