def tyu (sleep_hours) -> str:
    if sleep_hours == 8:
        return "Это нормально."
    elif sleep_hours < 8:
        return "Недосып"
    else:
        return "Пересып"
