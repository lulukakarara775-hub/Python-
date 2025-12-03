import math
def calculate_triangle_area():
    
        a = float(input())
        b = float(input())
        c = float(input())
        if a <= 0 or b <= 0 or c <= 0 or not (a + b > c and a + c > b and b + c > a):
            print("Ошибка:(")
            return
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        print(f"{area:.2f}")