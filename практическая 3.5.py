def pluralize_programmer():
    try:
        n = int(input())
        if n < 0:
            print("не отрицательный")
            return
        last_digit = n % 10
        last_two_digits = n % 100
        if 11 <= last_two_digits <= 14:
            suffix = "ов"
        elif last_digit == 1:
            suffix = ""
        elif 2 <= last_digit <= 4:
            suffix = "а"
        else:
            suffix = "ов"
        print(f"{n} программист{suffix}")
    except ValueError:
        print("Ошибка ввода.")