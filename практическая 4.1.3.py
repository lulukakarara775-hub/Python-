print("2 целых сичла:")
def variant1_task3():
    try:
        num1 = int(input())
        num2 = int(input())      
        divisible1 = (num1 % 3 == 0)
        divisible2 = (num2 % 3 == 0)
        if divisible1 and divisible2:
            print(True)
        elif divisible1 or divisible2:
            print("Одно число делится на 3")
        else:
            print(False)
    except ValueError:
        print("Ошибка ввода.")
