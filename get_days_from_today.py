from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d").date() # Спроба перевести задану дату у тип date
    except ValueError:
        return "Невірний формат"
    current_date = datetime.today().date() # Визначення поточної дати
    if date_obj == current_date: # Якщо задана дата = поточній...
        return 0 # ... то повернути 0
    else:
        delta_days = str(current_date - date_obj).split() # Якщо задана дата відрізняється від поточної...
        return int(delta_days[0]) # ... повернути к-сть днів до дати
    
# def main():
#     print(get_days_from_today('2024-02-29'))
    
# main()