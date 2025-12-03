import math
def calculate_room_area():
    PI = 3.14
    shape = input().lower()
    try:
        if shape == "треугольник":
            a = float(input())
            b = float(input())
            c = float(input())
            if a <= 0 or b <= 0 or c <= 0 or not (a + b > c and a + c > b and b + c > a):
                print("стороны некоректны")
                return
            s = (a + b + c) / 2
            area = math.sqrt(s * (s - a) * (s - b) * (s - c))
            print(f"{area:.2f}")
        elif shape == "прямоугольник":
            a = float(input())
            b = float(input())
            if a <= 0 or b <= 0:
                print("Положительный!!!")
                return
            area = a * b
            print(f"{area:.2f}")
        elif shape == "круг":
            r = float(input())
            if r <= 0:
                print("Радиус положительный!!!.")
                return
            area = PI * r**2
            print(f"{area:.2f}")
        else:
            print("неизвестная фигура")
    except ValueError:
        print("Ошибка.")