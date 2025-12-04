def variant2_task3():
    try:
        r = int(input())
        g = int(input())
        b = int(input())
        if r == 0 and g == 0 and b == 0:
            print("Чёрный цвет")
        elif r == 255 and g == 255 and b == 255:
            print("Белый цвет")
        elif r == 255 and g == 0 and b == 0:
            print("Красный цвет")
        elif r == 0 and g == 255 and b == 0:
            print("Зелёный цвет")
        elif r == 0 and g == 0 and b == 255:
            print("Синий цвет")
        else:
            print("Нет цвета")
    except ValueError:
        print("Ошибка ввода.")