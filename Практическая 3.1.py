def pluralize_hours(num):
    if num % 10 == 1 and num % 100 != 11:
        return f"{num} час"
    elif num % 10 >= 2 and num % 10 <= 4 and (num % 100 < 10 or num % 100 >= 20):
        return f"{num} часа"
    else:
        return f"{num} часов"

def pluralize_minutes(num):
    if num % 10 == 1 and num % 100 != 11:
        return f"{num} минута"
    elif num % 10 >= 2 and num % 10 <= 4 and (num % 100 < 10 or num % 100 >= 20):
        return f"{num} минуты"
    else:
        return f"{num} минут"

def task1(minutes_input):
    if minutes_input < 0:
        return "Количество минут не может быть отрицательным."

    hours = minutes_input // 60
    minutes = minutes_input % 60

    return f"{pluralize_hours(hours)} {pluralize_minutes(minutes)}"