print(">")
def variant1_task1():
    try:
        num = int(input())
        if num < 0:
            print(abs(num))
        elif num == 0:
            print(1)
        else:
            print(num)
    except ValueError:
        print("Ошибка ввода.")
