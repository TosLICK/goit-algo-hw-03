import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int): # чи усі атрибути типу int
        if min >= 1 and max <= 1000 and min < max: # чи задовольняють атрибути числовим обмеженням
            numbers = [] 
            while quantity > 0:
                number = random.randint(min, max) # генерується випадкове число у межах min і max
                if number in numbers: # якщо згенероване число вже у списку, тоді ігноруємо і генеруємо нове число
                    continue
                else:
                    numbers.append(number) # якщо згенероване число відсутнє у списку, то воно додається до списку
                    quantity -= 1
            return sorted(numbers) # сортуємо отриманий список
        else:
            return []
    else:
        return []

# Ще варіант зробити список від min до max і використати random.sample(list, quantity): 
# def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
#     if isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int): # чи усі атрибути типу int
#         if min >= 1 and max <= 1000 and min < max: # чи задовольняють атрибути числовим обмеженням
#             numbers = [x for x in range(max+1)] # створюється список від min до max включно
#             return sorted(random.sample(numbers, quantity)) # повертаємо відсортований список з отриманих чисел
#         else:
#             return []
#     else:
#         return []    
# print(get_numbers_ticket(1, 49, 6))