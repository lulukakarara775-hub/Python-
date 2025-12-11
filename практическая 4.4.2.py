side1 = float(input("Введите первую сторону: "))
side2 = float(input("Введите вторую сторону: "))
area = side1 * side2
if side1 == side2:
    print("Квадрат, площадь =", area)
else:
    print("Прямоугольник, площадь =", area)
